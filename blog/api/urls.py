from django.urls import path
from blog.api import views


urlpatterns = [
    # path('category/create/', views.CategoryCreateAPIView().as_view(), name='category_create_list'),
    # path('category/update/<uuid:uuid>/', views.CategoryUpdateAPIView().as_view(), name='category_update'),
    # path('category/detail/<uuid:uuid>/', views.CategoryRetrieveAPIView().as_view(), name='category_detail'),
    path('category/', views.CategoryCreateListAPIView().as_view(), name='category'),
]
