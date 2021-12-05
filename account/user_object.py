from django.utils.deprecation import MiddlewareMixin

from .models import Customer


class UserObject(MiddlewareMixin):
    def process_request(self, request):
        if request.user.is_authenticated and not request.user.is_superuser:
            request.user_obj = Customer.objects.get(username=request.user.username, password=request.user.password)
