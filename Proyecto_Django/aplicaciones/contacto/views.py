from django.shortcuts import render, HttpResponse

def contacto(request):
    return render(request,"pages/contacto.html",)