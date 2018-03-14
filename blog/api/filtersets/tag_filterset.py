from django_filters.rest_framework import CharFilter
from base.api.filtersets import BaseFilterSet
from ...models import TagModel

class TagFilterSet(BaseFilterSet):
	name = CharFilter(name="name", lookup_expr='icontains')
	name__exact = CharFilter(name="name", lookup_expr='exact')

	class Meta:
		model = TagModel
		fields = ['name', 'name__exact']