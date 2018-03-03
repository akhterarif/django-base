from base.api.views import BaseListAPIView

class CategoryListAPIView(BaseListAPIView):
	"""
	CategoryListAPIView for the project
	"""
	def __init__(self):
		super(CategoryListAPIView, self).__init__()