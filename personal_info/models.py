from django.db import models

# creating table and rows, using models

class Project(models.Model):
	title=models.CharField(max_length=50)
	description=models.CharField(max_length=300)
	image=models.ImageField(upload_to='personal_info/images',blank=True)
	url=models.URLField(blank=True)
		




