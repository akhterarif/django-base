from rest_framework.generics import RetrieveAPIView

class BaseRetrieveAPIView(RetrieveAPIView):
	"""
	BaseRetrieveAPIView for the project
	"""
	def __init__(self,
				 *args,
				 **kwargs):
		super(BaseRetrieveAPIView, self).__init__(*args,
												  **kwargs)