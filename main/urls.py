from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include


urlpatterns = [
    path('snippets/', include('myapp.urls')),
    # path('users/', include('user_auth.urls')),
    
    path('admin/', admin.site.urls),
]

urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]