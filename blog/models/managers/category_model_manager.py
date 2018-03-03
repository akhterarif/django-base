from base.models.managers import BaseModelManager

class CategoryModelManager(BaseModelManager):

    def __init__(self,
                 *args,
                 **kwargs):
        super(CategoryModelManager, self).__init__(*args,
                                                   **kwargs)
