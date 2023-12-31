from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect, render
from .models import Member

def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())
def restaurant(request):
    template = loader.get_template('restaurant.html')
    return HttpResponse(template.render())
def menu(request):
    template = loader.get_template('menu.html')
    return HttpResponse(template.render())
def reservasi(request):
    template = loader.get_template('reservasi.html')
    return HttpResponse(template.render())
def lokasi(request):
    template = loader.get_template('lokasi.html')
    return HttpResponse(template.render())

def make(request):
    mem=Member.objects.all()
    return render(request,'make.html',{'mem':mem})

def add(request):
    return render(request,'add.html')

def addrec(request):
    x=request.POST['first']
    y=request.POST['last']
    z=request.POST['country']
    mem=Member(firstname=x,lastname=y,country=z)
    mem.save()
    return redirect("/")

def delete(request,id):
    mem=Member.objects.get(id=id)
    mem.delete()
    return redirect("/")

def update(request,id):
    mem=Member.objects.get(id=id)
    return render(request,'update.html',{'mem':mem})

def uprec(request,id):
    x=request.POST['first']
    y=request.POST['last']
    z=request.POST['country']
    mem=Member.objects.get(id=id)
    mem.firstname=x
    mem.lastname=y
    mem.country=z
    mem.save()
    return redirect("/")