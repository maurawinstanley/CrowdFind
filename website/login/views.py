from django.shortcuts import render_to_response, render
from .forms import UserForm, LoginForm
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login
from .models import User

# Create your views here.
def index(request):
    c = {}
    return render(request, 'register.html', c)

def login(request):
    c = {}
    return render(request, 'login.html', c)

def register(request):
    if request.POST:
        form = UserForm(request.POST)

        if form.is_valid():
            form.save()
            form = UserForm()
            args = {}
            args['form'] = form
            return render(request, 'register.html', args)
        else:
            form = UserForm()

        args = {}
        args['form'] = form

        # return render_to_response('register.html', args)
        return render(request, 'register.html', args)
    else:
        form = UserForm()
        args = {}
        args['form'] = form
        return render(request, 'register.html', args)

def login(request):
    if request.POST:
        form = LoginForm(request.POST)

        if form.is_valid():
            user = User.objects.filter(email=form.cleaned_data.get('email'))
            if user:
                #redirect user to main page
                args = {}
                return HttpResponseRedirect('/login/main/')
            else:
                form = LoginForm()
                args = {}
                args['form'] = form
                return render(request, 'login.html', args)
        else:
            form = LoginForm()
    else:
        form = LoginForm()
        args = {}
        args['form'] = form
        return render(request, 'login.html', args)