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
        super(BaseModelService, self).__init__(*args,
                                               **kwargs)

        assert self.model is not None, (
                "'%s' must include a `model` attribute."
                % self.__class__.__name__
        )

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
        data_dict = {}
        related_fields_list = []
        non_related_fields_list = []
        fields_list = [field for field in self.model._meta.get_fields() \
                       if field.name in data.keys()]
        for field in fields_list:
            if field.name not in self.PREDEFINED_FIELD_LIST:
                if isinstance(field, ForeignKey) or \
                        isinstance(field, ManyToManyField) or \
                    isinstance(field, OneToOneField):
                    related_fields_list.append(field)
                else:
                    non_related_fields_list.append(field)
        for field in non_related_fields_list:
            data_dict[field.name] = data[field.name]
        data_dict['created_by'] = user
        created_obj = self.model.objects.create(**data_dict)
        for field in related_fields_list:
            if isinstance(field, ForeignKey):
                fields_instance, created = field.related_model.objects.get_or_create(**item)
                setattr(created_obj, field.name, fields_instance)
                created_obj.save()
            elif isinstance(field, OneToOneField):
                fields_instance= field.related_model.objects.create(**item)
                setattr(created_obj, field.name, fields_instance)
                created_obj.save()
            elif isinstance(field, ManyToManyField):
                for item in data[field.name]:
                    fields_instance, created = field.related_model.objects.get_or_create(**item)
                    getattr(created_obj, field.name).add(fields_instance)
        return created_obj

    def update(self,
               user,
               uuid,
               data,
               field_list=None):
        """
        Updates the data of given uuid

        :param uuid: uuid of the object which has to be updated
        :param data: data which has to be updated
        :param field_list: list of fields which have to update
        :return: ModelObject
        """
        data_dict = {}
        if field_list is None:
            field_list = [field.name for field in self.model._meta.get_fields(
            ) if field.name not in self.PREDEFINED_FIELD_LIST]
        updating_obj = self.model.objects.get_by_uuid(uuid=uuid)
        for field in field_list:
            value = data.get(field, None)
            if hasattr(updating_obj, field):
                setattr(updating_obj, field, value)
                updating_obj.save()
        updating_obj.updated_by = user
        updating_obj.save()
        return updating_obj

    def delete(self,
               user,
               uuid):
        """
        Deletes the data of given uuid

        :param uuid: uuid of the object which has to be deleted
        :return: ModelObject
        """
        deleting_obj = self.model.objects.get_by_uuid(uuid=uuid)
        deleting_obj.updated_by = user
        deleting_obj.save()
        ret_obj = deleting_obj
        deleting_obj.delete()
        return ret_obj
