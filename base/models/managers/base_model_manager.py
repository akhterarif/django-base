from django.db import models
from ..managers import SoftDeletionManager
from ...messages import MessageManager
from django.core.exceptions import ObjectDoesNotExist


class BaseModelManager(SoftDeletionManager):
    def __init__(self, *args, **kwargs):
        super(BaseManager, self).__init__(*args, **kwargs)

    def get_by_uuid(self, uuid):
        """
        Returns instance of a model according to given uuid
        :param uuid: UUID of the object
        :return ModelObject: instance of the model
        """
        try:
            model_obj = self.get(uuid=uuid)
        except self.model.DoesNotExist:
            message = MessageManager().get_msg(code='mm_test_1', context_data={
                'model_name': self.model.__name__})
            raise ObjectDoesNotExist(message)
        return model_obj
