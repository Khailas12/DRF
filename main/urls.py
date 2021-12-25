from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url


urlpatterns = [
    path('snippets/', include('myapp.urls')),
    url(r'^users/$', include('user_auth.urls')),
    
    path('admin/', admin.site.urls),
]
