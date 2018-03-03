from django.urls import re_path
from blog.api.views import CategoryListAPIView, PostListAPIView

urlpatterns = [
    re_path(r'^category/$', CategoryListAPIView().as_view(), name='category'),
    re_path(r'^post/$', PostListAPIView().as_view(), name='post'),
]
