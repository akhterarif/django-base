from rest_framework.serializers import Serializer

class BaseSerializer(Serializer):
	"""
	BaseSerializer for the project
	"""
	def __init__(self):
		super(BaseSerializer, self).__init__()