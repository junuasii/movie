from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import MovieForm
import movie
from movieapp.models import Movie


# Create your views here.
def index(request):
    movie=Movie.objects.all()
    context={
        'movie_list':movie
    }
    return render(request,'index.html',context)

def details(request,movie_id):
    movie=Movie.objects.get(id=movie_id)
    return render(request,"details.html",{'movie':movie})

def add_movie(request):
    if request.method=="POST":
        name=request.POST.get('name',)
        dis= request.POST.get('dis',)
        year = request.POST.get('year',)
        img = request.FILES['img']
        movie=Movie(name=name,dis=dis,year=year,img=img)
        movie.save()
        return redirect('/')
    return render(request,'add.html')

def update(request,id):
    movie=Movie.objects.get(id=id)
    form=MovieForm(request.POST or None,request.FILES,instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'movie':movie})

def delete(request,id):
    if request.method=='POST':
        movie=Movie.objects.get(id=id)
        movie.delete()
        return redirect('/')
    return render(request,'delete.html')