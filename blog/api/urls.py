from django.urls import re_path
from blog.api.views import CategoryListAPIView

urlpatterns = [
    re_path(r'^category/$', CategoryListAPIView().as_view(), name='category'),
]
