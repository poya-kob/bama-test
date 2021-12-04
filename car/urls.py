from django.urls import path
from .views import AdList, CarRegistration

urlpatterns = [
    path('ads/', AdList.as_view(), name="adlist"),
    path('create-ad/', CarRegistration.as_view(), name="create-ad")
]
