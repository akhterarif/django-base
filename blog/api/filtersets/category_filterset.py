from django_filters.rest_framework import CharFilter
from base.api.filtersets import BaseFilterSet
from ...models import CategoryModel

class CategoryFilterSet(BaseFilterSet):
	name = CharFilter(name="name", lookup_expr='icontains')
	name__exact = CharFilter(name="name", lookup_expr='exact')

	class Meta:
		model = CategoryModel
		fields = ['name', 'name__exact']