from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import SignupForm
from django.contrib.auth.models import User
from accounts.models import CustomUser
from django.contrib.auth.decorators import login_required

# Create your views here.

class SignupView(CreateView):
    form_class = SignupForm
    model = CustomUser
    template_name = 'signup.html'
    success_url = reverse_lazy('login')


@login_required
def profile(request, user_id):
    user = CustomUser.objects.get(id=user_id)
    context = {
        'user': user
    }
    return render(request, 'profile.html', context)