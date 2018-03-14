from base.models.managers import BaseModelManager

class TagModelManager(BaseModelManager):

    def __init__(self,
                 *args,
                 **kwargs):
        super(TagModelManager, self).__init__(*args,
                                                   **kwargs)
