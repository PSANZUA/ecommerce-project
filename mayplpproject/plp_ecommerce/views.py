# from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
     return HttpResponse("<h2>my first webpage with python Django</h2>")