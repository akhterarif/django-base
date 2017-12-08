# All message's code strats with srvc
# then the name of the class and then msg's highest number + 1
# add primarily english. but others language if needed
from django.utils.translation import ugettext_lazy as _

SERVICE_MSG = {
    'srvc_test_1': {
        'en': _('Apiview Test msg.'),
        'bn': _('হ্যালো বাংলাদেশ')
    }
}
