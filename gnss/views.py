from django.shortcuts import render
from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout
from django.http.response import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .models import *

# Create your views here.

def beidou(request):
    return render(request, "gnss/beidou.html", {
        'title': "BEIDOU"
    })


def gps_home(request):
    return render(request, 'gnss/gps_home.html')


def glonass(request):
    return render(request, "gnss/glonass.html", {
        'title': "GLONASS"
    })


def galileo(request):
    return render(request, "gnss/galileo.html", {
        'title': "GALILEO"
    })


def index(request):
    return render(request, "gnss/index.html", {
        'title': "Elena GNSS"
    })

def gnss(request):
    return render(request, "gnss/gnss.html", {
        'title': "GNSS"
    })

def gps(request):
    return render(request, "gnss/gps.html", {
        'title': "GPS"
    })

def irnss(request):
    return render(request, "gnss/irnss.html", {
        'title': "IRNSS"
    })


def login_view(request):
    if request.method == 'POST':
        username = request.POST["email"]
        password = request.POST["password"]
        user_authenticate = authenticate(
            request, 
            username=username,
            password=password
        )

        if user_authenticate is not None:
            login(request, user_authenticate)
            return HttpResponseRedirect(reverse("index"))
        
        else:
            return render(request, "gnss/login.html", {
                'err_message': "Invalid Username or Password",
                'title': "Login"
            })
    else:
        return render(request, "gnss/login.html", {
            'title': "Login"
        })


@login_required(login_url='/login')
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == 'POST':
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirm_password = request.POST["confirm_password"]

        if password != confirm_password:
            return render(request, "gnss/register.html", {
                'err_message': "Password do not match!",
                'title': "Register"
            })

        try:
            new_user = User.objects.create_user(
                username = email,
                email = email,
                password = password,
                first_name = first_name,
                last_name = last_name
            )
            new_user.save()
        except IntegrityError:
            return render(request, "gnss/register.html", {
                'err_message': "An account with the email already exists!", 
                'title': "Register"
            })
        login(request, new_user)

        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "gnss/register.html", {
            'title': "Register"
        })


def sbas(request):
    return render(request, "gnss/sbas.ejs")


def qzss(request):
    return render(request, "gnss/qzss.ejs")
        