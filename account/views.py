from django.shortcuts import reverse, redirect
from django.views import View
from django.contrib.auth import authenticate, login, logout
from .models import Customer


class LoginUser(View):
    def post(self, request):
        username = self.request.POST.get('username')
        password = self.request.POST.get('password')
        user = authenticate(request, password=password, username=username)
        print(user)
        if user:
            login(request, user)
        return redirect(reverse("home_page"))


class RegisterUsers(View):
    def post(self, request):
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = Customer.objects.create_user(username=username, password=password, is_staff=True, is_active=False)


def logout_page(request):
    logout(request)
    return redirect("/")
