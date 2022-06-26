from django.urls import path

from .views import (
    UserDetailView, 
    UserChangeView,
    )

urlpatterns = [
    path('<uuid:pk>/', UserDetailView.as_view(), name='profile'),
    path('<uuid:pk>/edit', UserChangeView.as_view(), name='edit'),
]