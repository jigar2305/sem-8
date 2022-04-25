from dataclasses import field
from todo.models import Project,Project_team,bugdetail,status
from django import forms

class Formbug(forms.ModelForm):
    class Meta:
        model = bugdetail
        fields = ('bugname','decsription','bugtype','status','project','startDate','completionDate','employee')

class Formbugupdate(forms.ModelForm):
    class Meta:
        model = bugdetail
        fields = ('bugname','decsription','bugtype','status','employee')

class Formproject(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('projectname','description','technology','startDate','completionDate')

class Formteam(forms.ModelForm):
    class Meta:
        model = Project_team
        fields = ('team_name','project','employee')

class Formstatus(forms.ModelForm):
    class Meta:
        model = status
        fields = ('statusName',)