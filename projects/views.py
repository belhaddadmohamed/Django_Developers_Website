from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib import messages

from .utils import searchProjects, paginateProjects
from .models import Project, Review, Tag
from .forms import ProjectForm, ReviewForm



def projects(request):
    # Search method in (utils.py)
    projects, search_query = searchProjects(request)
    # Paginator (utils.py)
    custom_range, projects_paginator = paginateProjects(request, projects, 6)

    context = {'projects': projects_paginator, 'search_query': search_query, 'custom_range': custom_range}

    return render(request, 'projects/projects.html', context)



def single_project(request, pk):
    project = Project.objects.get(id=pk)
    form = ReviewForm()

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.owner = request.user.profile
            review.project = project
            review.save()

            # Upvote/Downvote Calcutation
            project.getVoteCount

            messages.success(request, "Your comment is added successfully !")
            return redirect('single-project', pk=project.id)

    context = {'project': project, 'form':form}

    return render(request, 'projects/single_project.html', context)


@login_required(login_url="login")
def create_project(request):
    profile = request.user.profile
    form = ProjectForm()
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = profile
            project.save()
            messages.success(request, "Project was Added Successfully!")
            return redirect('user-account')     # The name of the url
        
    context = {'form': form}

    return render(request, 'projects/project_form.html', context)


@login_required(login_url="login")
def update_project(request, pk):
    # project = Project.objects.get(id=pk)
    profile = request.user.profile
    project = profile.project_set.get(id=pk)
    form = ProjectForm(instance=project)

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            messages.success(request, "Project was Updated Successfully!")
            return redirect('user-account')     # The name of the url
        
    context = {'form': form}

    return render(request, 'projects/project_form.html', context)


@login_required(login_url="login")
def delete_project(request, pk):
    # project = Project.objects.get(id=pk)
    profile = request.user.profile
    project = profile.project_set.get(id=pk)
    if request.method == 'POST':
        project.delete()
        messages.success(request, "Project was Deleted Successfully!")
        return redirect('user-account')

    context = {'object': project}

    return render(request, 'delete_template.html', context)