from rest_framework.serializers import ModelSerializer

class BaseModelSerializer(ModelSerializer):
	"""
	BaseModelSerializer for the project
	"""
	def __init__(self):
		super(BaseModelSerializer, self).__init__()