from django.contrib import messages
from django.contrib.auth import authenticate, get_user, login, logout
from django.shortcuts import redirect, render

from api.models import Request

from .forms import LoginForm


# Create your views here.
def index(request):
    """
    If user is authenticated, show admin interface
    Else, show login interface
    """

    if get_user(request).is_authenticated:
        context = {
            "no_requests": Request.objects.count(),
            "no_failed": Request.objects.filter(status='F').count(),
            "no_positive": Request.objects.filter(status='P').count(),
            "no_negative": Request.objects.filter(status='N').count(),
        }  
        return render(request, 'admin.html', context)
    else:
        login_form = LoginForm()
        context = {"login_form": login_form}
        return render(request, 'login.html', context)



def login_view(request):
    """
    Login user
    """
    _next = request.GET.get("next", "admin_panel:index")
    login_form = LoginForm(request.POST)
    if request.method == "POST" and login_form.is_valid():
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
        else:
            messages.error(request, f"User not found!", extra_tags="danger")
    return redirect(_next)


def logout_view(request):
    logout(request)
    return redirect('admin_panel:index')