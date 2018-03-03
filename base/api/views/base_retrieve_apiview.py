from rest_framework.generics import RetrieveAPIView

class BaseRetrieveAPIView(RetrieveAPIView):
	"""
	BaseRetrieveAPIView for the project
	"""
	def __init__(self):
		super(BaseRetrieveAPIView, self).__init__()