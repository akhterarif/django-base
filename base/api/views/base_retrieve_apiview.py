from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response

class BaseRetrieveAPIView(RetrieveAPIView):
	"""
	BaseRetrieveAPIView for the project
	"""

	service_class = None

	def __init__(self,
				 *args,
				 **kwargs):
		super(BaseRetrieveAPIView, self).__init__(*args,
												  **kwargs)

		assert self.service_class is not None, (
				"'%s' must include a 'service' attribute."
				% self.__class__.__name__
		)

	def get_queryset(self,
					 *args,
					 **kwargs):
		model_instance = self.service_class().get(*args,
											**kwargs)
		return model_instance

	def get(self, request, uuid, *args, **kwargs):
		data = {
			'uuid' : uuid
		}
		instance = self.service_class().get(**data)
		serializer = self.get_serializer(instance)
		return Response(serializer.data)
