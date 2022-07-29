from django.shortcuts import render,HttpResponse
topics=[
{'id':1,'title':'routing','body':'Routing is..'},
{'id':2,'title':'view','body':'View is..'},
{'id':3,'title':'Model','body':'Model is..'},
]

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
        
def create(request):
    return HttpResponse('Create')
def read(request,id):
    return HttpResponse('Read!'+id)