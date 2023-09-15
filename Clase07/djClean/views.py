from django.shortcuts import render

# Create your views here.

def inicio(request):
    return render(request,"pages/index.html",{})
def inicio02(request):
    return render(request,"pages/index02.html",{})