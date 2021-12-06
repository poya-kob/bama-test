from django.urls import path
from .views import AdList, CarRegistration, AdDetail

urlpatterns = [
    path('ads/', AdList.as_view(), name="adlist"),
    path('ads/<int:pk>/', AdDetail.as_view(), name="addetail"),
    path('create-ad/', CarRegistration.as_view(), name="create-ad")
]
