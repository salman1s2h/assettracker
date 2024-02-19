
from django.shortcuts import render,redirect
from django.contrib.auth import login ,authenticate,logout
from  .forms import SignUpForm ,LoginForm
from django.contrib import messages
from django.urls import reverse



def signup(request):
    if request.user.is_authenticated:
        return redirect('dashboard:home_pi')
    
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            # messages.success(request, "Congratulations, you are now a registered user!")
            return redirect('dashboard:home_pi')

    else:
        form = SignUpForm()
    return render(request, 'authentication/signup.html', {'form': form})


def log_in(request):

    if request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            remember_me = form.cleaned_data['remember_me']

            # We check if the data is correct
            user = authenticate(email=email, password=password)
            if user:
                login(request, user)  
                if remember_me:
                    request.session.set_expiry(50)
                else:
                    request.session.set_expiry(0) 

                return redirect('dashboard:home_pi')
            else:  
                messages.error(request, 'Invalid email or password')
  
    else:
        if request.user.is_authenticated:
            return redirect('dashboard:home_pi')
                    
        form = LoginForm()

    return render(request, 'authentication/login.html', {'form': form})

def log_out(request):
    logout(request)
    return redirect(reverse('authentication:login'))
