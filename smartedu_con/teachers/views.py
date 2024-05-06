from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic.list import ListView 
from django.views.generic.detail import DetailView
from teachers.models import Teacher
from courses.models import Course


class TeacherListView(ListView):
    model = Teacher
    template_name = 'teachers.html'
    context_object_name ='teachers'
    # paginate_by = 1
    # queryset = Teacher.objects.all()[:1]
    
    # def get_queryset(self):
    #     return Teacher.objects.all()[:2]

    
class TeacherDetailView(DetailView):
    model = Teacher
    template_name = 'teacher.html'
    context_object_name ='teacher'
    

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['courses'] = Course.objects.filter(avaliable=True,teacher = self.kwargs['pk'])
        return context