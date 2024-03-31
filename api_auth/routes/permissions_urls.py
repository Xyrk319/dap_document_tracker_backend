from django.urls import path
from api_auth.views import PermissionListView, PermissionDetailView

urlpatterns = [
    path('', PermissionListView.as_view(), name='permission-list'),
    path('<int:pk>', PermissionDetailView.as_view(), name='permission-detail'),
]
