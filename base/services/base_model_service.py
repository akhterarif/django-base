from django.db.models.fields.related import ForeignKey, ManyToManyField, OneToOneField

class BaseModelService(object):
    """
    This is the base service
    """
    PREDEFINED_FIELD_LIST = ['id', 'deleted_at', 'uuid', 'is_active',
                             'is_archived', 'created_by', 'updated_by',
                             'created_at', 'updated_at', ]
    model = None

    def __init__(self,
                 *args,
                 **kwargs):
        self.data = {}
        super(BaseModelService, self).__init__(*args,
                                               **kwargs)

        assert self.model is not None, (
                "'%s' must include a `model` attribute."
                % self.__class__.__name__
        )

    def _get_fields_list(self):
        """
        Returns related_fields_list, non_related_fields_list of a model
        :return: tuple of related_fields_list, non_related_fields_list
        """
        related_fields_list = []
        non_related_fields_list = []
        fields_list = [field for field in self.model._meta.get_fields() \
                       if field.name in self.data.keys()]
        for field in fields_list:
            if field.name not in self.PREDEFINED_FIELD_LIST:
                if isinstance(field, ForeignKey) or \
                        isinstance(field, ManyToManyField) or \
                        isinstance(field, OneToOneField):
                    related_fields_list.append(field)
                else:
                    non_related_fields_list.append(field)
        return related_fields_list, non_related_fields_list

    def _get_save_data(self,
                       fields_list):
        """
        Returns data dict of the values which has to be created or updated

        :param fields_list: list of fields
        :return: data_dict
        """
        data_dict = {}
        for field in fields_list:
            data_dict[field.name] = self.data[field.name]
        return data_dict

    def _set_related_fields_value(self,
                                  model_obj,
                                  fields_list):
        """
        Creates or Updates the model_obj's related(ForeignKey, OneToOne, ManyToMany) fields.

        :param model_obj: object of the assigned model
        :param fields_list: list of fields to be created or updated in model object
        :return: model_obj
        """
        for field in fields_list:
            if isinstance(field, ForeignKey):
                fields_instance = field.related_model.objects.get(uuid=self.data[field.name]['uuid'])
                setattr(model_obj, field.name, fields_instance)
                model_obj.save()
            elif isinstance(field, OneToOneField):
                fields_instance = field.related_model.objects.get_or_create(**self.data[field.name])
                setattr(model_obj, field.name, fields_instance)
                model_obj.save()
            elif isinstance(field, ManyToManyField):
                new_creating_uuid_list = [item['uuid'] for item in self.data[field.name]]
                all_m2m_related_obj_qs = getattr(model_obj, field.name).all()
                new_creating_related_obj_qs = field.related_model.objects.filter(
                        uuid__in=new_creating_uuid_list)
                old_m2m_deleting_objects_uuid_list = [item.uuid for item in all_m2m_related_obj_qs if item not in new_creating_related_obj_qs]
                getattr(model_obj, field.name).filter(uuid__in=old_m2m_deleting_objects_uuid_list).delete()
                present_m2m_objects_qs = getattr(model_obj, field.name).all()
                for obj in new_creating_related_obj_qs:
                    if obj not in present_m2m_objects_qs:
                        getattr(model_obj, field.name).add(obj)
        return model_obj

    def get(self,
            *args,
            **kwargs):
        """
        Returns a object of corresponding model by given filters
        :param kwargs:
        :return: QuerySet
        """
        result = self.model.objects.get(*args,
                                        **kwargs)
        return result

    def list(self,
             *args,
             **kwargs):
        """
        Returns a List of objects of corresponding model by given filters
        :param kwargs:
        :return: QuerySet
        """
        result_qs = self.model.objects.filter(*args,
                                              **kwargs)
        return result_qs

    def create(self,
               user,
               data):
        """
        Creates an object of given data in db

        :param data: data which has to be created
        :param field_list: list of fields which have to create
        :return: ModelObject
        """
        self.data = data
        related_fields_list, non_related_fields_list = self._get_fields_list()
        data_dict = self._get_save_data(fields_list=non_related_fields_list)
        data_dict['created_by'] = user
        created_obj = self.model.objects.create(**data_dict)
        res = self._set_related_fields_value(model_obj=created_obj,
                                             fields_list=related_fields_list)
        return res

    def update(self,
               user,
               uuid,
               data):
        """
        Updates the data of given uuid

        :param uuid: uuid of the object which has to be updated
        :param data: data which has to be updated
        :param field_list: list of fields which have to update
        :return: ModelObject
        """
        self.data = data
        related_fields_list, non_related_fields_list = self._get_fields_list()
        data_dict = self._get_save_data(fields_list=non_related_fields_list)
        data_dict['updated_by'] = user
        updating_obj = self.model.objects.get(uuid=uuid)
        for key, val in data_dict.items():
            setattr(updating_obj, key, val)
            updating_obj.save()
        res = self._set_related_fields_value(model_obj=updating_obj,
                                             fields_list=related_fields_list)
        return updating_obj

    def delete(self,
               user,
               uuid):
        """
        Deletes the data of given uuid

        :param uuid: uuid of the object which has to be deleted
        :return: ModelObject
        """
        deleting_obj = self.model.objects.get(uuid=uuid)
        deleting_obj.updated_by = user
        deleting_obj.save()
        ret_obj = deleting_obj
        deleting_obj.delete()
        return ret_obj
