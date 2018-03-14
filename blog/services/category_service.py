from ..models import CategoryModel
from base.services import BaseService, BaseModelService


class CategoryService(BaseModelService, BaseService):
    """
    Category Service functions are enlisted here.
    """

    model = CategoryModel

    def __init__(self,
                 *args,
                 **kwargs):
        super(CategoryService, self).__init__(*args,
                                              **kwargs)
