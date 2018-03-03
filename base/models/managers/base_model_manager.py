from ..managers import SoftDeletionManager


class BaseModelManager(SoftDeletionManager):
    def __init__(self,
                 *args,
                 **kwargs):
        super(BaseModelManager, self).__init__(*args,
                                               **kwargs)

