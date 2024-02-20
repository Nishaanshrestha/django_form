from django.shortcuts import redirect, render

from user.auth_form import LoginForm, SignupForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

# Create your views here.
def login_view(request):
    if request.method == "POST":
        
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user = authenticate(username = username, password = password)

            if user:
                login(request, user)
                return redirect('home')
            else:
                login_form.add_error('username', 'username or password is incorrect')
                return render(request, 'login.html', {'form':login_form})
    login_form = LoginForm()
    return render(request, 'login.html', {'form':login_form})

def signup_view(request):
    # signup_form = SignupForm()
    if request.method == "POST":
    
        signup_form = SignupForm(request.POST)
        if signup_form.is_valid():
            username = signup_form.cleaned_data['username']
            email = signup_form.cleaned_data['email']
            password = signup_form.cleaned_data['password']

            user = User.objects.create_user(username = username , email = email , password = password)
            if user:
                user.save()
                return redirect('login')
            else:
                signup_form.add_error('username' , 'something went wrong, please try again.')
                return render(request, 'signup.html', {'form':signup_form})
            
    signup_form = SignupForm()
    return render(request, 'signup.html', {'form':signup_form})


def home(request):
    return render(request, 'home.html')
