from ..models import CategoryModel
from base.services import BaseService


class CategoryService(BaseService):
    """
    This model used for categories business logics
    """

    model = CategoryModel

    def __init__(self, user):
        self.user = user
        super(CategoryService, self).__init__(user=self.user, model=self.model)
