from django.urls import path

from .views import UserDetailView

urlpatterns = [
    path('<uuid:pk>/', UserDetailView.as_view(), name='profile')   
]