from django.db import models
from generic.models import BaseField
from employee.models import User

# Create your models here.

class Project(BaseField):
    projectname = models.CharField(max_length=30)
    description = models.CharField(max_length=500)
    technology = models.CharField(max_length=100)
    startDate = models.DateField()
    completionDate = models.DateField()

    class meta:
        db_table = 'Project'

    def __str__(self):
        return self.projectname

class Project_team(BaseField):
    team_name = models.CharField(max_length=30)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    employee = models.ForeignKey(User, on_delete=models.CASCADE)

    class meta:
        db_table = 'Project_team'

class status(BaseField):
    statusName = models.CharField(max_length=50)

    class meta:
        db_table = 'status'

    def __str__(self):
        return self.statusName

class bugdetail(BaseField):
    bugname = models.CharField(max_length=100)
    decsription = models.CharField(max_length=100, null=True)
    bugtype = models.CharField(max_length=50)
    status = models.ForeignKey(status, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    startDate = models.DateField()
    completionDate = models.DateField()
    employee = models.ForeignKey(User, on_delete=models.CASCADE)


    class meta:
        db_table ='bugdetail'

    def __str__(self):
        return self.bugname


# def update_status(self):
#     if self.status == 'reported':
#         self.status = 'pending'
#     elif self.status == 'pending':
#         self.status = 'done'
#     elif self.status == 'done':
#         self.status = 'deley'
#     self.save()
