from rest_framework.serializers import Serializer

class BaseSerializer(Serializer):
	"""
	BaseSerializer for the project
	"""
	def __init__(self,
				 *args,
				 **kwargs):
		super(BaseSerializer, self).__init__(*args,
											 **kwargs)