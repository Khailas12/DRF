from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


urlpatterns = [
    url('', views.snippet_list),
    url('<int:pk>/', views.snippt_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)       # http://127.0.0.1:8000/snippets/.json