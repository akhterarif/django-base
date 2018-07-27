from django.urls import path
from blog.api import views


urlpatterns = [
    path('category/', views.CategoryCreateListAPIView().as_view(), name='category'),
]
