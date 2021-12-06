from django.shortcuts import reverse, redirect
from django.views import View
from django.views.generic import ListView
from django.contrib.auth import authenticate, login, logout

from .models import Customer
from car.models import Cars
from .forms import UserRegisterForm


class LoginUser(View):
    def post(self, request):
        username = self.request.POST.get('username')
        password = self.request.POST.get('password')
        user = authenticate(request, password=password, username=username)
        if user:
            login(request, user)
        return redirect(reverse("home_page"))


class RegisterUsers(View):
    def post(self, request):
        register_form = UserRegisterForm(request.POST)
        if register_form.is_valid():
            username = register_form.cleaned_data.get("username")
            password = register_form.cleaned_data.get("password")
            user = Customer.objects.create_user(username=username, password=password, is_staff=True, is_active=True)
            login(request, user)
        return redirect(reverse("home_page"))


def logout_page(request):
    logout(request)
    return redirect("/")


class MyCars(ListView):
    template_name = "account/my_cars.html"
    context_object_name = 'cars'

    def get_queryset(self):
        return Cars.objects.filter(user_id=self.request.user_obj.id).order_by("-id")

    def post(self, request):
        Cars.objects.filter(id=self.request.POST.get('car_id')).delete()
        return super().get(self.request)
