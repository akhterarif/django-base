from ..models import TagModel
from base.services import BaseService, BaseModelService


class TagService(BaseModelService, BaseService):
    """
    TagService functions are enlisted here.
    """

    model = TagModel

    def __init__(self,
                 *args,
                 **kwargs):
        super(TagService, self).__init__(*args,
                                              **kwargs)
