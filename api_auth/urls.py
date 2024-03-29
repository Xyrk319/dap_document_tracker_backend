from django.urls import path
from .views import RegisterView, LoginView, UserListView, UserDetailView, RoleListView, RoleDetailView, PermissionListView, PermissionDetailView

urlpatterns = [
    path('auth/register', RegisterView.as_view(), name='register'),
    path('auth/login', LoginView.as_view(), name='login'),
    path('users', UserListView.as_view(), name='user-list'),
    path('users/<int:pk>', UserDetailView.as_view(), name='user-detail'),
    path('roles', RoleListView.as_view(), name='role-list'),
    path('roles/<int:pk>', RoleDetailView.as_view(), name='role-detail'),
    path('permissions', PermissionListView.as_view(), name='permission-list'),
    path('permissions/<int:pk>', PermissionDetailView.as_view(), name='permission-detail'),
]
