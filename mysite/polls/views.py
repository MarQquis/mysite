from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello My name is Pattarapoll")
