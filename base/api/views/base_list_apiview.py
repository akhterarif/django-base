from rest_framework.generics import ListAPIView
from rest_framework.mixins import ListModelMixin

class BaseListAPIView(ListAPIView, ListModelMixin):
	"""
	BaseListAPIView for the project
	"""
	service_class = None

	def __init__(self,
				 *args,
				 **kwargs):
		super(BaseListAPIView, self).__init__(*args,
											  **kwargs)

		assert self.service_class is not None, (
				"'%s' must include a 'service' attribute."
				% self.__class__.__name__
		)

	def get_queryset(self,
					 *args,
					 **kwargs):
		model_qs = self.service_class().list(*args,
											 **kwargs)
		return model_qs