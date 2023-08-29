from django.db.models import Q
from .models import Profile, Skill
from django.core.paginator import Paginator


# NOTE: PageNotAnInteger(ex:None) or EmptyPage(ex:2000) Exceptions -> in Django_4.x is already hundled.

def paginateProfiles(request, profiles, results):
    # Create a Paginator with "results" is the number of profiles in each page
    paginator = Paginator(profiles, results)
    page_number = request.GET.get("page")
    profiles_paginator = paginator.get_page(page_number)

    # Get the page number after Error Exceptions (Check the content of get_page() to understand)     
    page_number = profiles_paginator.number
    
    # Create a custom_range instead of using page_range (Imagine you have 1000 page!!)
    leftIndex = (int(page_number) - 3)
    if leftIndex < 1:
        leftIndex = 1

    rightIndex = (int(page_number) + 3)
    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages + 1

    custom_range = range(leftIndex, rightIndex)

    return custom_range, profiles_paginator



def searchProfiles(request):
    # Variable to capture the search input <form> by 'name'
    search_query = ''        

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    skills = Skill.objects.filter(name__icontains=search_query)

    # profiles = Profile.objects.all()
    profiles = Profile.objects.distinct().filter(Q(name__icontains=search_query) |
                                                 Q(short_intro__icontains=search_query) |
                                                 Q(skill__in=skills))
    
    return profiles, search_query

