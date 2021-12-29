from django.http.response import HttpResponse

from django.shortcuts import (get_object_or_404,
                              render,
                              HttpResponseRedirect)
from django.shortcuts import render,redirect
from .models import Project
from .forms import ProjectsForm
from .utils import searchProjects

# Create your views here.

def projects(request):
    projects, search_query = searchProjects(request)

    context = {'projects': projects,
               'search_query': search_query}
    # all_project = Project.objects.all()
    # context = {'projects':all_project}
    return render(request,'projects/projects.html',context)
    
def project_detail(request,project_id):
    project = Project.objects.get(id=project_id)
    context = {'project' : project}
    return render(request,'projects/single-project.html',context)

def create_project(request):
    form = ProjectsForm()
    context = {'form': form}

    if request.method == 'POST':
        form = ProjectsForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('projects')
    return render(request,'projects/project-form.html',context)

def edit_project(request,project_id):
    project = Project.objects.get(id=project_id)
    form = ProjectsForm(instance=project)
    context = {'form':form}

    if request.method == 'POST':
        form = ProjectsForm(request.POST,request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects')
    return render(request,'projects/project-form.html',context)


def delete_project(request,project_id):
    obj = get_object_or_404(Project, id = project_id)
    all_project = Project.objects.all()
    context = {'projects':all_project}

    if request.method == 'POST':
        
        obj.delete()
        return redirect('projects')
    return render(request,'projects/delete-project.html',context)

