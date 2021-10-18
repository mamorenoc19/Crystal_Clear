from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "Crystal_Clear_App/home.html")