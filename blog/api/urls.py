from django.urls import re_path
from blog.api.views import CategoryListAPIView, CategoryCreateAPIView, PostListAPIView

urlpatterns = [
    re_path(r'^category/create/$', CategoryCreateAPIView().as_view(), name='category_create'),
    re_path(r'^category/$', CategoryListAPIView().as_view(), name='category'),
    re_path(r'^post/$', PostListAPIView().as_view(), name='post'),
]
