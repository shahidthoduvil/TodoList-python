from django.shortcuts import render,redirect
from .forms import TodoForm
from .models import *
# Create your views here.

# listing the todo content 
def home(request):
   form =TodoForm()
   todos=Todo.objects.all()
   if request.method=='POST':
      form=TodoForm(request.POST)
      if form.is_valid:
         form.save()
         return redirect('home')
      
   return render(request,'home.html',{'form':form,'todos':todos})



# updating the todo content
def update(request,todo_id):
   todo=Todo.objects.get(id=todo_id)
   form=TodoForm(instance=todo)
   if request.method=='POST':
      form=TodoForm(request.POST,instance=todo)
      if form.is_valid():
        form.save()
        return redirect('home')

   return render(request,'update.html',{'form':form})





# deleting the todo content
def delete(request,todo_id):
   todo=Todo.objects.get(id=todo_id).delete()
   return redirect('home')
   