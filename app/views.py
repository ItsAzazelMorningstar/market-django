from django.shortcuts import render

# Create your views here.

def index(self):
    return render(self,'app/index.html')