from django.db import models
import random
import os


def get_filename_extension(filename):
	basename=os.path.basename(filename)
	name,ext=os.path.splitext(basename)
	return name,ext

def upload_poster1(instance,filename,):
	new_filename=random.randint(1,9999999999)
	name,ext=get_filename_extension(filename)
	final_filename=f"{new_filename}{ext}"
	return "videos/"+f"{new_filename}/{final_filename}"
def upload_poster(instance,filename,):
	new_filename=random.randint(1,9999999999)
	name,ext=get_filename_extension(filename)
	final_filename=f"{new_filename}{ext}"
	return "movies/"+f"{new_filename}/{final_filename}"

# Create your models here.
class Movies(models.Model):
	movie_title=models.CharField(max_length=100,null=True,blank=True)
	poster1=models.ImageField(upload_to=upload_poster1)
	link=models.URLField(blank=True)
	time=models.CharField(max_length=10,null=True,blank=True)
	description=models.TextField()
	produced_by=models.CharField(max_length=100,null=True,blank=True)
	def __str__(self):
		return self.movie_title

class Video(models.Model):
	video_title=models.CharField(max_length=100,null=True,blank=True)
	poster=models.ImageField(upload_to=upload_poster)
	link=models.URLField(blank=True)
	time=models.CharField(max_length=10,null=True,blank=True)
	size=models.CharField(max_length=15,null=True,blank=True)
	def __str__(self):
		return self.video_title


		
	

	