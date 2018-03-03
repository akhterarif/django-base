from rest_framework.generics import ListAPIView

class BaseListAPIView(ListAPIView):
	"""
	BaseListAPIView for the project
	"""
	def __init__(self):
		super(BaseListAPIView, self).__init__()