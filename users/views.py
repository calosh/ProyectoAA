from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import FormView
from django.contrib.auth import authenticate, login, logout

from .forms import LoginForm
from .forms import UserForm


class LoginView(FormView):
    form_class = LoginForm
    template_name = 'login.html'
    success_url = '/'


    def form_valid(self, form):
        user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
        
        if user is not None:
            if user.is_active:
                login(self.request, user)
                 

        return super(LoginView, self).form_valid(form)



def salir(request):
    logout(request)
    return redirect('/')




class RegisterView(FormView):
    form_class = UserForm
    template_name = 'register.html'
    success_url = '/users/login'

    print "Aqui 0"

    def form_valid(self, form):
        print "Aqui"
        user = form.save()
        user.email = form.cleaned_data['email']
        user.save()
        return super(RegisterView, self).form_valid(form)
