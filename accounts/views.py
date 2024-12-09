from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.http import HttpResponse
from .forms import CustomUserCreationForm

# Create your views here.
def register_view(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Account created succesfully")
            return redirect("login")
    else:
        form = CustomUserCreationForm()
    return render(request,'accounts/register.html',{'form':form})

def login_view(request):
    # if request.user.is_authenticated:
    #     return redirect('tasklistings')
    
    form = AuthenticationForm(request, data=request.POST or None)
    if request.method == "POST" and form.is_valid():
        login(request, form.get_user())
        return redirect('tasklistings')
    
    return render(request, 'accounts/login.html', {'form': form})


#if a user is not logged in our login_decorator will redirect back to the login page
#else we allow user to see the homepage
@login_required
def home_view(request):
    return render(request,'accounts/home.html')


# def logout_view(request):
#     logout(request)
#     return redirect("login")















