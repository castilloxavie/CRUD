from http.client import HTTPResponse
from django.shortcuts import render
from.models import task
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import  reverse
#from django.template import loader
# Create your views here.

def index(request):
    #template = loader.get_template("appxa/index.html")
    db_data = task.objects.all()
    context={
        "db_data": db_data[::-1],
        "update": None
    }
    
    #return HttpResponse(template.render(context, request))
    return render(request, "appxa/index.html", context)

def insert(request):
    try:
        task_subject = request.POST["subject"]
        task_descriptions = request.POST["descriptions"]
        if task_subject == "" or task_descriptions =="":
            raise ValueError("el texto no puede ir vacio")
        db_data = task(
             subject=task_subject, 
             description=task_descriptions
        )
 
        db_data.save()
        return HttpResponseRedirect(reverse("index"))
    except ValueError as  err:
        print(err)
        return HttpResponseRedirect(reverse("index")) 


# def update(request):
#     task_id = request.POST["id"]
#     task_subject = request.POST["subject"]
#     task_descriptions= request.POST["descriptions"]
#     db_data = task.objects.get(pk=task_id)
#     db_data.subject = task_subject
#     db_data.description =task_descriptions
#     db_data.save()
#     return HttpResponseRedirect(reverse("index"))

def update(request):
    task_id = request.POST["id"]
    task_subject = request.POST["subject"]
    task_description = request.POST["descriptions"]
    db_data = task.objects.get(pk=task_id)
    db_data.subject = task_subject
    db_data.description = task_description
    db_data.save()
    return HttpResponseRedirect(reverse("index")) 


def update_form(request, task_id):
    db_data = task.objects.all()
    db_data_only = task.objects.get(pk=task_id)
    print(db_data_only)
    context={
        "db_data": db_data[::-1],
        "update": db_data_only
    }
    return render(request, "appxa/index.html", context)


def delete(request, task_id):
    db_data = task.objects.filter(id=task_id)
    db_data.delete()
    return HttpResponseRedirect(reverse("index"))

