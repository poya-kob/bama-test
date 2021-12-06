from .forms import UserRegisterForm


def register_form(request):
    return {
        'register_form': UserRegisterForm()
    }
