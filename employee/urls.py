from django.urls import path,include
from employee import views
from .views import *


urlpatterns = [
    path('login/', Userlogin.as_view(), name='userlogin'),
    path('<int:pk>profile/', profileview.as_view(), name='profilepage'),
    path('register/',BaseRegisterView.as_view() , name='add_employee'),
    path('view/', Listemployee.as_view(), name='list_employee'),
    path('deleteemployee/<pk>', views.Deleteemployee , name='delete_employee'),
    # path('delete/<int:pk>/', deleteemployee.as_view(), name='delete_employee'),
    path('logout/', logoutview.as_view(), name='logout'),
    path('<int:pk>detail/', employeeDetail.as_view(), name='employeedetail'),

   
]