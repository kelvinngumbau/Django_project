#from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Member

# Create your views here.

def members(request):
    mymembers = Member.objects.all().values()
    template = loader.get_template('myfirst.html')
    context = {
        'mymembers' : mymembers,
    }
    return  HttpResponse(template.render(context,request))

def details(request,id):
    
    mymember = Member.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
        "mymembers": mymember,
    }
    
    return HttpResponse(template.render(context,request))

def main(request):
    
    tempalate = loader.get_template("main.html")
    return HttpResponse(tempalate.render())

def testing(request):
    members = Member.objects.all().values()
    template = loader.get_template("template.html")
    context = {
        "firstname" : "van persie",
        "shoes" : "nike",
        "mymembers" : members
    
    }
    
    return HttpResponse(template.render(context,request))