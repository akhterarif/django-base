from django.contrib.auth.models import User
from django.conf import settings

class BaseUtility(object):
    """
    This is BaseUtility class for the project.
    """

    def __init__(self,
                 *args,
				 **kwargs):
        super(BaseUtility, self).__init__(*args,
                                          **kwargs)

    def get_super_admin(self):
        user = User.objects.get(username=settings.DEFAULT_SUPER_ADMIN_NAME)
        return user