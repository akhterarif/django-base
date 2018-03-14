class BaseService(object):
    """
    This is the base service.
    Common service-methods for the project are enlisted here
    """

    def __init__(self,
                 *args,
                 **kwargs):
        super(BaseService, self).__init__(*args,
                                          **kwargs)