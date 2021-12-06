from django.urls import path

from .views import LoginUser, logout_page, MyCars, RegisterUsers

urlpatterns = [
    path('login/', LoginUser.as_view(), name="login_page"),
    path('logout/', logout_page, name="logout_page"),
    path('register/', RegisterUsers.as_view(), name="register_page"),
    path('my-cars/', MyCars.as_view(), name="my-cars"),
]
