from . import views
from django.urls import path


urlpatterns = [
    path('', views.UserList.as_view()),
    path('<int:pk>/', views.UserDetail.as_view())
]