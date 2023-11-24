from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, logout
from .forms import NewUserForm

# Create your views here.
def home(request):
    return render(request, 'core/index.html')



# register 
def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration successful")
            return redirect("login")
        messages.error(request, "Unsuccessful registration. Invalid Information")
    
    form = NewUserForm()
    context = {
        "form": form
    }

    return render(request, "core/register.html", context)



def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user is not None:
                messages.info(request, f"You are logged in as {username}")
                return redirect('success')
            else:
                messages.error(request, "Invalid username or password")
        else:
            messages.error(request, "Invalid username or password")

    form = AuthenticationForm()

    context = {
        "form": form
    }
    return render(request, 'core/login.html', context)


def logout_request(request):
    logout(request)
    messages.info(request, "You have succefully logged out")
    return redirect('homepage')



def success_view(request):
    context = {
        'message': 'Congratulations! Your Login was successful.',
    
    }
    return render(request, 'core/landpage.html', context)
