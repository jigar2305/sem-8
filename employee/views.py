from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render,redirect
from django.urls import reverse
from django.views.generic import  ListView,UpdateView, DeleteView, FormView, CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.views import redirect_to_login
from django.contrib import messages
from .forms import *
from django.views import View, generic
from django.contrib.auth.views import LoginView, LogoutView
from .models import User
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags


# Create your views here.

class BaseRegisterView(SuccessMessageMixin, FormView):

    form_class = UserForm
    template_name = 'employee/register.html'
    success_url ="/view"
  
    def form_valid(self, form):
        user = form.save()
        user.set_password(user.password)  
        user.save()
        username= form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        dict = {'username': username,'password': password}
        subject, from_email, to = 'login detail', settings.EMAIL_HOST_USER, form.cleaned_data.get('email')
        html_content = render_to_string('employee_mail.html', dict) # render with dynamic value
        text_content = strip_tags(html_content)
        msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
        msg.attach_alternative(html_content, "text/html")
        msg.send()
        return super().form_valid(form)


    def get_success_message(self, cleaned_data):
        username = cleaned_data["username"]
        return username + " - User Created Successfully..!!"


class Userlogin(LoginView):
    model = User   
    template_name = 'employee/login.html'
    success_url ="/home"

class logoutview(LogoutView):
    success_url ="/login"

class profileview(UpdateView):
    form_class = updateForm
    model = User
    template_name = "employee/profile.html"
    success_url ="/view"
    

class Listemployee(ListView):
    model = User
    users = model.objects.all()
    context_object_name = 'users'
    template_name = "employee/list_employee.html"


def Deleteemployee(request, pk):
    employee = User.objects.get(pk=pk)
    employee.delete()
    messages.success(request, "employee deleted successfully!")
    return redirect('/view')



class employeeDetail(generic.DetailView):
    model = User
    context_object_name = 'employee'
    template_name = "employee/detail_employee.html"