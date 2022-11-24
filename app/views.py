from django.shortcuts import render

# Create your views here.
def first(request):
    return render(request,'first.html',context={'name':'jagadeesh','age':22})
