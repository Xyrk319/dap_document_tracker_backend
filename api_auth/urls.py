from django.urls import path,include
from .views import RegisterView, LoginView, UserListView, UserDetailView, RoleListView, RoleDetailView, PermissionListView, PermissionDetailView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

urlpatterns = [
    path('auth/register', RegisterView.as_view(), name='register'),
    path('auth/login', LoginView.as_view(), name='login'),
    path('auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('users/', include('api_auth.routes.users_urls')),
    path('roles/', include('api_auth.routes.roles_urls')),
    path('permissions/', include('api_auth.routes.permissions_urls')),
]
