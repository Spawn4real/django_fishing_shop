import adminapp.views as adminapp
from django.urls import path
from adminapp.views import user

app_name = 'adminapp'

urlpatterns = [
    path('users/create/', user.UserCreateView.as_view(), name='user_create'),
    path('users/read/', user.UserListView.as_view(), name='users'),
    path('users/update/<int:pk>/', user.UserUpdateView.as_view(), name='user_update'),
    path('users/delete/<int:pk>/', user.UserDeleteView.as_view(), name='user_delete'),
]
