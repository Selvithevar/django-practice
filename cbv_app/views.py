from django.shortcuts import render
from django.views.generic import View,ListView,DeleteView,CreateView,UpdateView,DeleteView
from django.http import HttpResponse
from cbv_app.models import *
from django.urls import reverse_lazy
from cbv_app.forms import Itemforms


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

    
# session managemnet (cookies)
def home(request):
    request.session.set_test_cookie()
    return HttpResponse("<b>hi this is test</b>")

def page2(request):
    if request.session.test_cookie_worked():
        print("cookies are enbaled")
    request.session.delete_test_cookie()
    return HttpResponse("<b>page2</b>")

def countView(request):
    if "count" in request.COOKIES:
        count = int(request.COOKIES['count']) + 1
    else:
        count = 1
    response = render(request,"cbv_app/count.html",{"count":count})
    response.set_cookie("count",count)
    return response

def index(request):
    return render(request,"cbv_app/index.html")

def addItem(request):
    form = Itemforms()
    response=render(request,"cbv_app/addItem.html",{"form":form})
    if request.method=="POST":
        form = Itemforms(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            quantity = form.cleaned_data['quantity']
            response.set_cookie(name,quantity,120)
    return response

def displayCart(request):
    return render(request,"cbv_app/display_items.html")

def pagecount(request):
    count = request.session.get('count',0)
    count=count+1
    request.session['count']=count
    return render(request,"cbv_app/count.html",{"count":count})