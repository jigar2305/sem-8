from audioop import reverse
from distutils.command.config import config
from sre_constants import SUCCESS
from django.conf import settings
from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import  ListView, CreateView, UpdateView
from todo.forms import Formbug, Formbugupdate,Formproject,Formstatus,Formteam
from todo.models import *
from django.contrib import messages
from django.views import generic



# bug releted

class Addbug(CreateView):
    form_class = Formbug
    model = bugdetail
    template_name = 'todo/add_bugs.html'
    success_url = '/todo/buglist'


class Listbug(ListView):
    model = bugdetail
    bugs = model.objects.all()
    context_object_name = 'bugs'
    template_name = "todo/list_bug.html"

class Listhome(ListView):
    model = bugdetail
    bugs = model.objects.all()
    context_object_name = 'bugs'
    template_name = "todo/index.html"

def Deletebug(request, pk):
    bug = bugdetail.objects.get(pk=pk)
    bug.delete()
    return redirect('/todo/buglist')

class Updatebug(UpdateView):
    form_class = Formbugupdate
    model = bugdetail
    template_name = "todo/update_bug.html"
    success_url ="/todo/buglist"

class bugDetail(generic.DetailView):
    model = bugdetail
    context_object_name = 'bug'
    template_name = "todo/detail_bug.html"
# project releted

class Addproject(CreateView):
    form_class = Formproject
    model = Project
    template_name = 'todo/add_project.html'
    success_message = 'Success: project was created.'
    success_url = '/todo/projectlist'

class Listproject(ListView):
    model = Project
    projects = model.objects.all()
    context_object_name = 'projects'
    template_name = "todo/list_project.html"

class ProjectDetailView(generic.DetailView):
    model = Project
    context_object_name = 'projects'
    template_name = "todo/projectdetail.html"

    def get_context_data(self, **kwargs):
        context = super(ProjectDetailView, self).get_context_data(**kwargs)
        context['bugs'] = bugdetail.objects.all()
        return context

# team releted

class Addteam(CreateView):
    form_class = Formteam
    model = Project_team
    template_name = 'todo/add_team.html'
    success_url = '/todo/teamlist'

class Listteam(ListView):
    model = Project_team
    context_object_name = 'teams'
    template_name = "todo/list_team.html"

# status releted

class Addstatus(CreateView):
    form_class = Formstatus
    model = status
    template_name = 'todo/add_status.html'
    success_url = '/todo/statuslist'


# crud demo
