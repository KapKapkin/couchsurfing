from django.urls import reverse, path

from .views import HomePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home')
]
