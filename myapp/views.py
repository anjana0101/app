from django.shortcuts import render
from.models import task
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView
from  django.urls import reverse_lazy
# Create your views here.
class TaskListView(ListView):
    model=task

    template_name='task_view.html'
    context_object_name = 'obj1'



class TaskDetailView(DetailView):
    model= task
    template_name='detail.html'
    context_object_name='i'

class TaskUpdateView(UpdateView):
    model = task
    template_name = 'edit.html'
    context_object_name = 'new'
    fields=('name','priority')
    def get_success_url(self):
        return  reverse_lazy('cbvdetail',kwargs={'pk':self.object.id})
class TaskDeleteView(DeleteView):
    model = task
    template_name = 'delete.html'
    success_url = reverse_lazy('cbvtask')





