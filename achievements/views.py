from django.shortcuts import render
from .models import Achievements
# Create your views here.

def myachievements(request):

	ach=Achievements.objects.all()

	return render (request, 'achievements/achievements.html',{'y':ach})
