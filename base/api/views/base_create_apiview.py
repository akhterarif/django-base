from rest_framework.generics import CreateAPIView
from rest_framework.mixins import CreateModelMixin

class BaseCreateAPIView(CreateAPIView, CreateModelMixin):
	"""
	BaseCreateAPIView for the project
	"""
	def __init__(self,
				 *args,
				 **kwargs):
		super(BaseCreateAPIView, self).__init__(*args,
												**kwargs)