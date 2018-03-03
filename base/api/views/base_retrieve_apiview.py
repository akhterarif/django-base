from rest_framework.generics import RetrieveAPIView

class BaseListAPIView(RetrieveAPIView):
	"""
	BaseRetrieveAPIView for the project
	"""
	def __init__(self):
		super(BaseListAPIView, self).__init__()