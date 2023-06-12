from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def template_inheritance(request):
    return HttpResponse('<h1>Here we are performing template inheritance b/w parent.html and child.html</h1>')

def parent(request):
    return render(request,'parent.html')

def child(request):
    return render(request,'child.html')