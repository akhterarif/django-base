from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'api/auth/', include('rest_framework.urls')),
    path(r'api/blog/', include('blog.api.urls'))
]
