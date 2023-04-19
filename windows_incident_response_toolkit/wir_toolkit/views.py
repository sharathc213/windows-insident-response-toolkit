from django.shortcuts import render


from django.http import HttpResponse
from django.shortcuts import render
import json
from django.http import JsonResponse
from django.template.loader import get_template
from django.template import Context, Template
import json


# Create your views here.
def Signin(request):
    return render(request,'Signin.html')

def Dashboard(request):
    return render(request,'Dashboard.html')

def Form(request):
    return render(request,'Form.html')

def Settings(request):
    context = {}
    f = open('config.json')
    data = json.load(f)
    context["data"] = data['API']
    return render(request,'Settings.html',context)