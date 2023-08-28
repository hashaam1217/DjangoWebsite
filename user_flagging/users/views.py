from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def index(request):
    if not request.user.is_authenticated: 
        return HttpResponseRedirect(reverse("login"))
    return HttpResponseRedirect("/")

def login_view(request):
    if request.method == "POST":
        #Accessing form data
        username = request.POST["username"]
        password = request.POST["password"]

        #Check if correct, returning none or user object
        user = authenticate(request, username=username, password=password)

        # logging in if correct
        if user: 
            login(request, user)
            return HttpResponseRedirect(reverse("index"))

        #Failed
        else:
            return render(request, "users/login_view.html", 
                    {
                        "message": "Invalid Credentials"
                        })
    else:
        return render(request, "users/login_view.html")

def logout_view(request):
    logout(request)
    return render(request, "users/login_view.html", { 
        "message": "Logged Out"
        })
