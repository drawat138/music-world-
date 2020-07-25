from django.db import models
import random
import os

# Create your models here.
def get_filename_extension(filename):
	basename=os.path.basename(filename)
	name,ext=os.path.splitext(basename)
	return name,ext

def upload_picture(instance,filename,):
	new_filename=random.randint(1,9999999999)
	name,ext=get_filename_extension(filename)
	final_filename=f"{new_filename}{ext}"
	return "bhajan/"+f"{new_filename}/{final_filename}"


class Godsong(models.Model):
	title=models.CharField(max_length=100,null=True,blank=True)
	singer=models.CharField(max_length=100,null=True,blank=True)
	picture=models.ImageField(upload_to=upload_picture)
	link=models.URLField(blank=True)
	size=models.CharField(max_length=20,null=True, blank=True)
	time=models.CharField(max_length=20,null=True,blank=True)

class Instrumental(models.Model):
	title=models.CharField(max_length=100,null=True,blank=True)
	songname=models.CharField(max_length=100,null=True,blank=True)
	artist=models.CharField(max_length=100,null=True,blank=True)
	link=models.URLField(blank=True)
	size=models.CharField(max_length=20,null=True, blank=True)
	time=models.CharField(max_length=20,null=True,blank=True)

class Register(models.Model):
	name=models.CharField(max_length=50)
	email=models.EmailField(max_length=35,unique=True)
	phone=models.CharField(max_length=10,unique=True)
	password=models.CharField(max_length=15)
	confirm_password=models.CharField(max_length=10)




