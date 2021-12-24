from django.urls import path
from . import views


urlpatterns = [
    path('', views.snippet_list),
    path('<int:pk>/', views.snippt_detail),
]