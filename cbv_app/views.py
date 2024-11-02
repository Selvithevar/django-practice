from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse

class Greetingview(View):
    def get(self,request):
        return HttpResponse("<b>hi i am selvi</b>")