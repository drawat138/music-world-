from django.shortcuts import render
from django.http import HttpResponse
from .forms import RegistrationForm,LoginForm
from .models import Song,Artist,Movies
from videos.models import Movies,Video
from music.models import Godsong,Instrumental,Register
# Create your views here.
def index(request):
	return HttpResponse("<h1> Welcome to my website </h1>")

def songdetails(request):
	artists=Artist.objects.all()
	poster=Movies.objects.all()
	movies1=Movies.objects.all()
	songs=Song.objects.all()
	context={'artists':artists,'poster':poster,'songs':songs,'movies1':movies1}
	return render(request,'song/songdetails.html',context)


def download(request,id):
	songs=Song.objects.get(id=id)
	context={'songs':songs}
	return render(request,'song/download.html',context)

def videos(request):
	videos=Video.objects.all()
	context={'videos':videos}
	return render(request,'song/videos.html',context)

def player(request,id):
	video=Video.objects.get(id=id)
	context={'video':video}
	return render(request,'song/player.html',context)

def movies(request):
	movies1=Movies.objects.all()
	context={'movies1':movies1}
	return render(request,'song/movies.html',context)

def moviedownload(request,id):
	movies1=Movies.objects.get(id=id)
	context={'movies1':movies1}
	return render(request,'song/moviedownload.html',context)


def godsong(request):
	godsong=Godsong.objects.all()
	context={'godsong':godsong}
	return render(request,'song/godsong.html',context)

def instrumental(request):
	instrumental=Instrumental.objects.all()
	context={'instrumental':instrumental}
	return render(request,'song/instrumental.html',context)

def register(request):
	form=RegistrationForm(request.POST or None)
	if request.method=="POST":
		if form.is_valid():
			try:
				form.save()
				return redirect('/song/download.html')
			except:
				return redirect('/song/register')
	context={'form':form}
	return render(request,'song/register.html',context)
def login(request):
	form=LoginForm(request.POST or None)
	if request.method=="POST":
		if form.is_valid():
			username=form.cleaned_data.get('username')
			password=form.cleaned_data.get('password')
			try:
				user=Register.objects.get(email=username,password=password)
				request.session['username']=user.email

				return redirect('/song/songdetails')
			except:
				return HttpResponse("<p> Sorry, Login failed</p>")
	context={'form':form}
	return render(request,'song/login.html',context)
