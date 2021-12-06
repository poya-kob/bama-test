from django.urls import path

from .views import LoginUser, logout_page, MyCars

urlpatterns = [
    path('login/', LoginUser.as_view(), name="login_page"),
    path('logout/', logout_page, name="logout_page"),
    path('my-cars/', MyCars.as_view(), name="my-cars"),
]
