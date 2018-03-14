from django.utils.translation import ugettext_lazy as _
from .apiview_messages import API_VIEW_MSG
from .generic_messages import GENERIC_MSG
from .model_messages import MANAGER_MSG, MODEL_MSG
from .service_messages import SERVICE_MSG
from django.conf import settings


class MessageManager(object):
    """
    Class for manging the messages for different classes
    """

    def __init__(self,
                 *args,
				 **kwargs):
        self.apiview_messages = API_VIEW_MSG
        self.generic_messages = GENERIC_MSG
        self.model_messages = MODEL_MSG
        self.manager_messages = MANAGER_MSG
        self.service_messages = SERVICE_MSG
        self.all_messages = {**self.apiview_messages, **self.generic_messages,
                             **self.model_messages, **self.manager_messages, **self.service_messages}
        self.default_language = settings.DEFAULT_LANGUAGE
        super(MessageManager, self).__init__(*args,
                                             **kwargs)

    def get_msg(self, code, language_code=None, context_data={}):
        """
        Retrurns messages of a code

        :param code: message code
        :param language_code: message's language code
        :return str: message of corresponding code
        """
        if language_code is None:
            language_code = self.default_language
        return self.all_messages[code][language_code].format(**context_data)
