from django.urls import path
from api_auth.views import UserListView, UserDetailView, UserAuthenticatedView

urlpatterns = [
    path('', UserListView.as_view(), name='user-list'),
    path('<int:pk>', UserDetailView.as_view(), name='user-detail'),
    path('authenticated', UserAuthenticatedView.as_view(), name='user-authenticated'),
]
