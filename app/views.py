from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from app.models import Profile, Operation_obj
from django.core.urlresolvers import reverse, reverse_lazy



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
        if request.user.is_authenticated:
            Operation_obj.objects.create(eq=stringify(number1, operation, number2), answer = equation(number1, number2, operation), user = request.user )
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
    success_url = "/"#reverse_lazy("profile_update_view")

class ProfileView(ListView):
    model = User
    template_name = "profile.html"
    def get_context_data(self):
        context = super().get_context_data()
        EQS = Operation_obj.objects.filter(user = self.request.user)
        EQS_owner = Operation_obj.objects.all()
        context['EQS_owner'] = EQS_owner
        context['EQS'] = EQS
        return context

class ProfileUpdateView(UpdateView):
    model = Profile
    success_url = "/"
    fields = ('access_level',)
