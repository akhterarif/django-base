from django.contrib import admin
from django.urls import path, include
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token
from rest_framework.documentation import include_docs_urls

urlpatterns = [
	path('docs/', include_docs_urls(title="Base app's Doc")),
    path('admin/', admin.site.urls),
    path('api-auth-token/', obtain_jwt_token),
    path('api-token-refresh/', refresh_jwt_token),
    path('api-token-verify/', verify_jwt_token),
    path('api/auth/', include('rest_framework.urls')),
    path('api/blog/', include('blog.api.urls'))
]
