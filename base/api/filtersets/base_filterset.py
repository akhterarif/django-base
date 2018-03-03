from django_filters.rest_framework import FilterSet, CharFilter

class BaseFilterSet(FilterSet):
	"""
	BaseFilterSet class for the project.
	"""
	uuid = CharFilter(name="uuid", lookup_expr='exact')

	def __init__(self, *args, **kwrgs):
		super(BaseFilterSet, self).__init__(*args, **kwrgs)

