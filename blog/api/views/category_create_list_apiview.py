from base.api.views import BaseCreateAPIView, BaseListAPIView
from ..serializers import CategoryCreateSerializer, CategoryOutputSerializer
from ...services import CategoryService
from ..filtersets import CategoryFilterSet
from rest_framework.permissions import IsAuthenticated


class CategoryCreateListAPIView(BaseCreateAPIView, BaseListAPIView):
    """
    CategoryCreateAPIView for the project
    """
    service_class = CategoryService
    serializer_class = CategoryOutputSerializer
    output_serializer = CategoryOutputSerializer
    filter_class = CategoryFilterSet
    permission_classes = (IsAuthenticated,)

    def get(self,
            request,
            *args,
            **kwargs):
        return self.list(request,
                         *args,
                         **kwargs)

    def post(self,
             request,
             *args,
             **kwargs):
        return self.create(request,
                           *args,
                           **kwargs)
