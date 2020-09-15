from django.shortcuts import render
from .models import Project
# Create your views here.

def myhomepage(request):

	myproject=Project.objects.all()

	return render(request, 'portfolio/myhomepage.html',{'project':myproject})