from django.urls import path,include
from .views import *
from todo import views
urlpatterns = [
    path('addbug/', Addbug.as_view(), name='add_bug'),
    path('<int:pk>update/', Updatebug.as_view(), name='update_bug'),
    path('addproject/', Addproject.as_view(), name='add_project'),
    path('addteam/', Addteam.as_view(), name='add_team'),
    path('addstatus/', Addstatus.as_view(), name='add_status'),
    path('buglist/',Listbug.as_view(), name='list_bug'),
    path('projectlist/',Listproject.as_view(), name='list_project'),
    path('teamlist/',Listteam.as_view(), name='list_team'),
    path('home/',Listhome.as_view(), name='home'),
    path('<int:pk>view/', ProjectDetailView.as_view(), name='detail_project'),
    path('deletbug/<pk>', views.Deletebug , name='deletebug'),
    path('<int:pk>bugdetail/', bugDetail.as_view() , name='bugdetail'),
    

]