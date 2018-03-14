from rest_framework.generics import DestroyAPIView

class BaseDestroyAPIView(DestroyAPIView):
	"""
	BaseDestroyAPIView for the project
	"""
	def __init__(self,
				 *args,
				 **kwargs):
		super(BaseDestroyAPIView, self).__init__(*args,
												 **kwargs)