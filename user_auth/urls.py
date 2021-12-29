from .views import UserList, UserDetail
from django.urls import path


urlpatterns = [
    path('', UserList.as_view()),
    path('<int:pk>/', UserDetail.as_view()),
]   