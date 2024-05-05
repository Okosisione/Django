from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request,'frontApp/index.html')

def about(request):
    return render(request, 'frontApp/about.html')






