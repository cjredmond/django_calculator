from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from app.models import Profile


def equation(a,b,c):
    if c == "+":
        return int(a) + int(b)
    elif c == "-":
        return int(a) - int(b)
    elif c == "x":
        return int(a) * int(b)
    elif c == "/":
        if b == "0":
            return "Cant divide by 0"
        return int(a) / int(b)
    else:
        return "HELP"

def stringify(a,b,c):
    return a + b + c +" ="


def index_view(request):
    numbers = request.GET
    if request.GET:
        number1 = numbers["number1"]
        number2 = numbers["number2"]
        operation = numbers["operation"]
    else:
        number1 = "1"
        number2 = "1"
        operation = "+"

    context = {
    "answer" : equation(number1, number2, operation),
    "EQ" : stringify(number1, operation, number2)
    }
    return render(request, "index.html", context)

class UserCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = "/"

class ProfileView(ListView):
    model = User
    template_name = "profile.html"

class ProfileUpdateView(UpdateView):
    model = Profile
    success_url = "/"
    fields = ('access_level',)
