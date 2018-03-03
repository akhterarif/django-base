from django_filters.rest_framework import CharFilter
from base.api.filtersets import BaseFilterSet
from ...models import CategoryModel

class CategoryFilterSet(BaseFilterSet):
	name = CharFilter(name="name", lookup_expr='icontains')

	class Meta:
		model = CategoryModel
		fields = ['name']