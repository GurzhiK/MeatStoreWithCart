from django.urls import path
from .views import UserDetail, UserList

urlpatterns = [
    path('users/', UserList.as_view(), name='user-list'),
    path('users/detail/<int:pk>/',
         UserDetail.as_view(), name='user-detail'),

]
