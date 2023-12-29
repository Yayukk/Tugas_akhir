from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

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