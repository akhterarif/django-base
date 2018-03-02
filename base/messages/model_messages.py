# All model's message's code strats with mdl_
# And all manager's code starts with mm_
# then the name of the class and then msg's highest number + 1
# add primarily english. but others language if needed
from django.utils.translation import ugettext_lazy as _

MODEL_MSG = {
    'mdl_test_1': {
        'en': _('Apiview Test msg.'),
        'bn': _('হ্যালো বাংলাদেশ')
    }
}

MANAGER_MSG = {
    'mm_test_1': {
        'en': _('Apiview Test msg {model_name}.'),
        'bn': _('হ্যালো বাংলাদেশ')
    }
}
