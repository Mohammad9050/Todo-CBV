from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views.generic import (
    TemplateView,
    ListView,
    CreateView,
    DeleteView,
    UpdateView,
    View,
    FormView,
)
from .models import Task
from .forms import TaskForm

def first(request):
    return HttpResponse('Home page')


class TaskList(ListView):
    model = Task
    template_name = "home.html"

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)
    


class TaskComplete(View):
    model = Task
    success_url = reverse_lazy("list")

    def get(self, request, *args, **kwargs):
        object = self.model.objects.get(id=kwargs.get("pk"))
        object.complete = True
        object.save()
        return redirect(self.success_url)


class TaskDelete(View):
    model = Task
    success_url = reverse_lazy("list")

    def get(self, request, *args, **kwargs):
        object = self.model.objects.get(id=kwargs.get("pk"))
        object.delete()
        return redirect(self.success_url)
    


class TaskCreate(CreateView):
    model = Task
    fields = ["title"]
    #template_name = 'test2.html'
    success_url = reverse_lazy("list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form)
    
# def create_view(request):
#     if request.method == 'POST':
#         form = TaskForm(request.POST)
#         if form.is_valid():
#             form.save(commit=False)
#             form.instance.user = request.user
#             form.save()
#             return HttpResponseRedirect(reverse('list'))
#     else:
#         form = TaskForm()
#     return render(request, 'create.html', {'form':form})





