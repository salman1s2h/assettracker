from django.shortcuts import render,redirect 
## This is Parent home page which are extended by other 

def home_page(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            return render(request, 'dashboard/home_pi.html')
        # else:
        #     # Redirect regular users to a different page or perform other actions
        #     return render(request, 'regular_user_home.html')
    else:
        return render(request, 'authentication/login.html')

##This home page which return chart extended from home 
def home_page_pi(request):
    
    if request.user.is_authenticated:
        if request.user.is_superuser:
            return render(request, 'dashboard/home_pi.html')
        
    return render(request, 'authentication/login.html') 