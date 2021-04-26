from django.shortcuts import render, redirect
from .models import Show
from datetime import datetime
def index(request):
    #return redirect("")
    return redirect("/shows")

def newShow(request):
    #return redirect("")
    return render(request,"newshow.html")

def addShow(request):
    title_post = request.POST["title"]
    release_date_post = request.POST["releasedate"]
    network_post = request.POST["network"]
    descripcion_post = request.POST["description"]
    Show.objects.create(title=title_post,release_date=release_date_post, network= network_post ,desc=descripcion_post)
    return redirect("/")

def shows(request):
    context={ 
             "shows": Show.objects.all()}
    return render(request,"shows.html", context)

def detalleshow(request,id_show):
    context={ 
             "show": Show.objects.get(id=id_show)}
    return render(request,"detalleshow.html", context)

def detalleditshow(request,id_show):
    context={ 
             "show": Show.objects.get(id=id_show)}
    return render(request,"editshow.html", context)

def editShow(request, id_show):
    show_update= Show.objects.get(id=id_show)
    show_update.title = request.POST["title"]
    show_update.release_date = request.POST["releasedate"]
    show_update.network = request.POST["network"]
    show_update.desc = request.POST["description"]
    show_update.updated_at = datetime.now()
    show_update.save()
    return redirect("/shows/"+str(id_show))

def destroy(request, id_show):
    
    show_to_delete = Show.objects.get(id=id_show)
    show_to_delete.delete()

    return redirect("/shows")