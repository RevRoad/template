from django.shortcuts import render

# Create your views here.

def home(request):
    context = {}
    return render(request, '<app_name>/home.html', context)
