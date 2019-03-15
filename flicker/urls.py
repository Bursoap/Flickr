from django.urls import path
from .views import FlickerView

urlpatterns = [
    path('', FlickerView.as_view(), name='index')
]