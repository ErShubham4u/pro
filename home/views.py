from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home/home.html')

def logout(request):
    return render(request, 'logout.html')

from django.http import HttpResponseRedirect
from .forms import SignUpForm
def signup(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.set_password(user.password)
            user.save()
            return HttpResponseRedirect('/accounts/login/')
    return render(request, 'signup.html', {'form': form})


