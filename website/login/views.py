from django.shortcuts import render_to_response, render
from .forms import UserForm
from django.http import HttpResponseRedirect, HttpResponse
#from django.core.context_processors import csrf

# Create your views here.
def index(request):
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
            return render(request, 'login.html', args)
        else:
            form = UserForm()

        args = {}
        args['form'] = form

        # return render_to_response('register.html', args)
        return render(request, 'login.html', args)
    else:
        form = UserForm()
        args = {}
        args['form'] = form
        return render(request, 'login.html', args)
