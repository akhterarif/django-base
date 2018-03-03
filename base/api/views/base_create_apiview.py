from rest_framework.generics import CreateAPIView

class BaseCreateAPIView(CreateAPIView):
	"""
	BaseCreateAPIView for the project
	"""
	def __init__(self,
				 *args,
				 **kwargs):
		super(BaseCreateAPIView, self).__init__(*args,
												**kwargs)