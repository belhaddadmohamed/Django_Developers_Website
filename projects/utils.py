from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import Project, Tag


def paginateProjects(request, projects, results):
    paginator = Paginator(projects, results)
    page_number = request.GET.get("page")
    projects_paginator = paginator.get_page(page_number)

    # Get the page number after Error Exceptions (Check the content of get_page() to understand)     
    page_number = projects_paginator.number
    
    # Create a custom_range instead of using page_range (Imagine you have 1000 page!!)
    leftIndex = (int(page_number) - 3)
    if leftIndex < 1:
        leftIndex = 1

    rightIndex = (int(page_number) + 3)
    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages + 1

    custom_range = range(leftIndex, rightIndex)

    return custom_range, projects_paginator




def searchProjects(request):
    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    tags = Tag.objects.filter(name__icontains=search_query)

    projects = Project.objects.distinct().filter(Q(title__icontains=search_query) |
                                                 Q(description__icontains=search_query) |
                                                 Q(owner__name__icontains=search_query) |
                                                 Q(tags__in=tags))

    return projects, search_query