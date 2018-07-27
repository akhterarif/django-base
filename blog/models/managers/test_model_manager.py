from base.models.managers import BaseModelManager


class TestModelManager(BaseModelManager):

    def __init__(self,
                 *args,
                 **kwargs):
        super(TestModelManager, self).__init__(*args,
                                              **kwargs)
