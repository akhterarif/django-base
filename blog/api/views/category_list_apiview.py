from base.api.views import BaseListAPIView
from ..serializers import CategoryModelSerializer
from ...services import CategoryService
from ..filtersets import CategoryFilterSet
from rest_framework.permissions import IsAuthenticated

class CategoryListAPIView(BaseListAPIView):
	"""
	CategoryListAPIView for the project
	"""
	service_class = CategoryService
	serializer_class = CategoryModelSerializer
	filter_class = CategoryFilterSet
	permission_classes = (IsAuthenticated,)

	def get(self, request, *args, **kwargs):
		return self.list(request, *args, **kwargs)