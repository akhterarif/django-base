from ..models import CategoryModel
from base.services import BaseService, BaseModelService


class CategoryService(BaseService, BaseModelService):
    """
    Category Service functions are enlisted here.
    """

    model = CategoryModel

    def __init__(self, user):
        self.user = user
        super(CategoryService, self).__init__(user=self.user, model=self.model)
