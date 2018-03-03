from base.api.views import BaseCreateAPIView
from ..serializers import CategoryModelSerializer
from ...services import CategoryService
from ..filtersets import CategoryFilterSet

class CategoryCreateAPIView(BaseCreateAPIView):
	"""
	CategoryCreateAPIView for the project
	"""
	service_class = CategoryService
	serializer_class = CategoryModelSerializer
	filter_class = CategoryFilterSet

	def post(self,
			 request,
			 *args,
			 **kwargs):
		return self.create(request,
						   *args,
						   **kwargs)