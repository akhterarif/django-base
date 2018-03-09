from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework import status

class BaseCreateAPIView(CreateAPIView):
	"""
	BaseCreateAPIView for the project
	"""
	service_class = None
	output_serializer = None

	def __init__(self,
				 *args,
				 **kwargs):
		super(BaseCreateAPIView, self).__init__(*args,
												**kwargs)
		assert self.output_serializer is not None, (
				"'%s' must include a `output_serializer` attribute."
				% self.__class__.__name__
		)

	def get_service_obj(self):
		return self.service_class()

	def get_output_serializer(self):
		return self.output_serializer

	def create(self, request, *args, **kwargs):
		serializer = self.get_serializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		created_instance = self.get_service_obj().create(user=self.request.user,
														 data=serializer.initial_data)
		output_serializer = self.output_serializer(created_instance)
		headers = self.get_success_headers(output_serializer.data)
		return Response(output_serializer.data,
						status=status.HTTP_201_CREATED,
						headers=headers)