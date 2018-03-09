from rest_framework.generics import UpdateAPIView
from rest_framework.response import Response
from rest_framework import status

class BaseUpdateAPIView(UpdateAPIView):
	"""
	BaseUpdateAPIView for the project
	"""

	service_class = None
	output_serializer = None

	def __init__(self,
				 *args,
				 **kwargs):
		super(BaseUpdateAPIView, self).__init__(*args,
												**kwargs)
		assert self.output_serializer is not None, (
				"'%s' must include a `output_serializer` attribute."
				% self.__class__.__name__
		)

	def get_service_obj(self):
		return self.service_class()

	def get_output_serializer(self):
		return self.output_serializer

	def update(self,
			   request,
			   uuid,
			   *args,
			   **kwargs):
		serializer = self.get_serializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		updated_instance = self.get_service_obj().update(user=self.request.user,
														 uuid=uuid,
														 data=serializer.initial_data)
		output_serializer = self.output_serializer(updated_instance)
		return Response(output_serializer.data,
						status=status.HTTP_200_OK)