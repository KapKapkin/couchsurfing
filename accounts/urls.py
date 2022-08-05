from django.urls import path

from .views import (
    AccountView, 
    UserChangeView,
    UserSignUpView
    )
 
urlpatterns = [
    path('<uuid:pk>/', AccountView.as_view(), name='profile'),
    path('<uuid:pk>/edit', UserChangeView.as_view(), name='edit'),
    path('signup', UserSignUpView.as_view(), name='account_signup'),
]