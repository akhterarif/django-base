from django.urls import re_path, path
from blog.api.views import CategoryListAPIView, CategoryCreateAPIView, CategoryUpdateAPIView, PostListAPIView, PostCreateAPIView, PostUpdateAPIView

urlpatterns = [
	path(r'category/create/', CategoryCreateAPIView().as_view(), name='category_create'),
	path(r'category/update/<uuid:uuid>/', CategoryUpdateAPIView().as_view(), name='category_update'),
	path(r'category/', CategoryListAPIView().as_view(), name='category'),
    path('post/create/', PostCreateAPIView().as_view(), name='post_create'),
    path('post/update/<uuid:uuid>/', PostUpdateAPIView().as_view(), name='post_update'),
    path(r'post/', PostListAPIView().as_view(), name='post'),
]
