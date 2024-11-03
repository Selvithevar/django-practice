from django.shortcuts import render
from django.views.generic import View,ListView,DeleteView,CreateView,UpdateView,DeleteView
from django.http import HttpResponse
from cbv_app.models import *
from django.urls import reverse_lazy
class Greetingview(ListView):
    

    model = students
    template_name = 'cbv_app/student_list.html'
    
class studentDetailview(DeleteView):
    model = students
    template_name = 'cbv_app/student_detail.html'

class studentCreateview(CreateView):
    model = students
    fields = ('__all__')
    template_name = 'cbv_app/student_form.html'
    
class studentUpdateview(UpdateView):
    model = students
    fields = ('__all__')
    template_name = 'cbv_app/student_form.html'
    

class studentDeleteview(UpdateView):
    model = students
    fields = ('__all__')
    template_name = 'cbv_app/stu_confirm_delete.html'
    success_url = reverse_lazy('students')

    
