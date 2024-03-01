from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')
def login(request):
    return render(request,'login.html')  
def registre(request):
    return render(request,'registre.html')
def visitez(request):
    return render(request,'visitez.html')
def visite(request):
    return render(request,'visite.html')
def vise(request):
    return render(request,'vise.html')   
