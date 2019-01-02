from django.shortcuts import render,render_to_response
from django.http import HttpResponseRedirect
from django.contrib import messages
from django import forms
import hashlib
from  .models import User, Etudiant


class UserForm(forms.Form):
    username = forms.CharField(label='Username',max_length=100)
    password = forms.CharField(label='Password',widget=forms.PasswordInput())

def login(request):
    if request.method == 'POST':
        uf = UserForm(request.POST)
        if uf.is_valid():
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            user = User.objects.filter(username__exact=username, password__exact= hashlib.sha3_256(password.encode("utf-8")).hexdigest())
            if user:
                response = HttpResponseRedirect('index')
                response.set_cookie('username', username, 3600)
                return response
            else:
                messages.error(request, 'Username or password error')
                return HttpResponseRedirect('login')
    else:
        uf = UserForm()
    # return render_to_response('login.html', {'uf': uf})
    return render(request,'login.html', {'uf': uf})


def index(req):
    username = req.COOKIES.get('username','')
    etudiants = Etudiant.objects.all()

    return render_to_response('index.html' ,{'username':username, 'etudiants':etudiants})
