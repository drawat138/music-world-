from django.db import models
import random
import os

# Create your models here.
def get_filename_extension(filename):
	basename=os.path.basename(filename)
	name,ext=os.path.splitext(basename)
	return name,ext

def upload_songimage(instance,filename,):
	new_filename=random.randint(1,9999999999)
	name,ext=get_filename_extension(filename)
	final_filename=f"{new_filename}{ext}"
	return "download/"+f"{new_filename}/{final_filename}"

def upload_poster(instance,filename,):
	new_filename=random.randint(1,9999999999)
	name,ext=get_filename_extension(filename)
	final_filename=f"{new_filename}{ext}"
	return "songdetails/"+f"{new_filename}/{final_filename}"
	
def upload_singerimage(instance,filename,):
	new_filename=random.randint(1,9999999999)
	name,ext=get_filename_extension(filename)
	final_filename=f"{new_filename}{ext}"
	return "songdetails/"+f"{new_filename}/{final_filename}"

class Song(models.Model):
	title=models.CharField(max_length=80,null=True,blank=True)
	movie=models.CharField(max_length=50,null=True,blank=True)
	genre=models.CharField(max_length=60,null=True,blank=True)
	singer=models.CharField(max_length=50,null=True,blank=True)
	music=models.CharField(max_length=50,null=True,blank=True)
	duration=models.CharField(max_length=80,null=True,blank=True)
	download=models.URLField()
	songimage=models.ImageField(upload_to=upload_songimage,null=True,blank=True)

class Artist(models.Model):
	singerimage=models.ImageField(upload_to=upload_singerimage,null=True,blank=True)
	songtitle=models.CharField(max_length=80,null=True,blank=True)
	song_by=models.CharField(max_length=50,null=True,blank=True)
	song=models.CharField(max_length=60,null=True,blank=True)
	songurl=models.URLField( null=True,blank=True)
	size=models.CharField(max_length=15,null=True,blank=True)
	duration=models.CharField(max_length=15,null=True,blank=True)


class Movies(models.Model):
	poster=models.ImageField(upload_to=upload_poster,null=True,blank=True)
