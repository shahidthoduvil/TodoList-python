from django.urls import path

from .views import *
urlpatterns = [
 
 path('',home,name='home'),
 path('udpate/<int:todo_id>/',update,name='update'),
 path('delete/<int:todo_id>/',delete,name='delete')

]
