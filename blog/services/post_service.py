from ..models import PostModel
from base.services import BaseService, BaseModelService


class PostService(BaseModelService, BaseService):
    """
    PostService functions are enlisted here.
    """

    model = PostModel

    def __init__(self,
                 *args,
                 **kwargs):
        super(PostService, self).__init__(*args,
                                          **kwargs)
