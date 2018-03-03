from rest_framework.generics import UpdateAPIView

class BaseUpdateAPIView(UpdateAPIView):
	"""
	BaseUpdateAPIView for the project
	"""
	def __init__(self):
		super(BaseUpdateAPIView, self).__init__()