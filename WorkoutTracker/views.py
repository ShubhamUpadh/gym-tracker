from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import UserLoginForm

# Create your views here.

def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(request,data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                # Redirect to home page
                return redirect('home')
    else:
        form = UserLoginForm()
    return render(request,'login.html',{'form':form})