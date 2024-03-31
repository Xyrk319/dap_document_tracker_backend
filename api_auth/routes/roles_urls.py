from django.urls import path
from api_auth.views import RoleListView, RoleDetailView

urlpatterns = [
    path('', RoleListView.as_view(), name='role-list'),
    path('<int:pk>', RoleDetailView.as_view(), name='role-detail'),
]
