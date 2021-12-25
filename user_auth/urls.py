from . import views
from django.conf.urls import url
from django.urls import path


urlpatterns = [
    path('', views.UserList.as_view()),
    url(r'^(?P<pk>[0-9]+)/$', views.UserDetail.as_view())
]