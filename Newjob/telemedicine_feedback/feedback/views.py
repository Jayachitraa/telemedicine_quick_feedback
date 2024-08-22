from django.shortcuts import render
from .models import Feedback

def index(request):
    feedback = Feedback.objects.all()
    return render(request , "index.html",{"feedback":feedback})

