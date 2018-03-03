class BaseModelService(object):
    """
    This is the base service
    """
    PREDEFINED_FIELD_LIST = ['id', 'deleted_at', 'uuid', 'is_active',
                             'is_archived', 'created_by', 'updated_by', 'created_at', 'updated_at', ]
    model = None

    def __init__(self, user):
        self.user = user
        super(BaseModelService, self).__init__()

        assert self.model is not None, (
                "'%s' should either include a `model` attribute"
                % self.__class__.__name__
        )

    def get(self, **kwargs):
        """
        Returns a object of corresponding model by given filters
        :param kwargs:
        :return: QuerySet
        """
        result = self.model.objects.get(**kwargs)
        return result

    def list(self, **kwargs):
        """
        Returns a List of objects of corresponding model by given filters
        :param kwargs:
        :return: QuerySet
        """
        result_qs = self.model.objects.filter(**kwargs)
        return result_qs

    def create(self,
               data,
               field_list=None):
        """
        Creates an object of given data in db

        :param data: data which has to be created
        :param field_list: list of fields which have to create
        :return: ModelObject
        """
        data_dict = {}
        if field_list is None:
            field_list = [field.name for field in self.model._meta.get_fields(
            ) if field.name not in self.PREDEFINED_FIELD_LIST]
        for field in field_list:
            data_dict[field] = data.get(field, None)
        data_dict['created_by'] = self.user
        return self.model.objects.create(**data_dict)

    def update(self,
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
        updating_obj.updated_by = self.user
        updating_obj.save()
        return updating_obj

    def delete(self,
               uuid):
        """
        Deletes the data of given uuid

        :param uuid: uuid of the object which has to be deleted
        :return: ModelObject
        """
        deleting_obj = self.model.objects.get_by_uuid(uuid=uuid)
        deleting_obj.updated_by = self.user
        deleting_obj.save()
        ret_obj = deleting_obj
        deleting_obj.delete()
        return ret_obj
