from base.models.managers import BaseModelManager

class PostModelManager(BaseModelManager):

    def __init__(self,
                 *args,
                 **kwargs):
        super(PostModelManager, self).__init__(*args,
                                                   **kwargs)
