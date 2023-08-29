from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages

from .forms import CustomUserCreationForm, ProfileForm, SkillForm, MessageForm
from .models import Profile
from .utils import searchProfiles, paginateProfiles


def loginUser(request):
    page = 'login'
    context = {'page': page}

    if request.user.is_authenticated:
        return redirect('profiles')

    if request.method == 'POST':
        username = request.POST['username'].lower()
        password = request.POST['password']

        # If the username doesn't exist return the message
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, "username does't exist")

        # User exists => Authenticate (Check in the database + Create a Session for this user)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(request.GET['next'] if 'next' in request.GET else 'user-account')
        else:
            messages.error(request, "username OR password is incorrect")

    return render(request, 'users/login_register.html', context)
 

 
def logoutUser(request):
    logout(request)
    messages.info(request, "User was successfully logged out!")
    return redirect('login')



def registerUser(request):
    if request.user.is_authenticated:
        return redirect('profiles')

    page = 'register'
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            # Before saving check some conditions (we can do that also in the front-end)
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            # Success message if the user is created
            messages.success(request, "An account was created Successfully!!")
            # Login the user
            login(request, user)
            return redirect('edit-account')
        else:
            messages.error(request, "An error has occured during registration!!")

    context = {'page':page, 'form':form}

    return render(request, 'users/login_register.html', context)



def profiles(request):
    # Get the profiles based on search method in 'Utils.py'
    profiles, search_query = searchProfiles(request)
    # Pagination (utils.py)
    custom_range, profiles_paginator = paginateProfiles(request, profiles, 6)

    context = {'profiles': profiles_paginator, 'search_query': search_query, 'custom_range':custom_range}

    return render(request, 'users/profiles.html', context)



def userProfile(request, pk):
    profile = Profile.objects.get(id=pk)
    topSkills = profile.skill_set.exclude(description__exact="")
    otherSkills = profile.skill_set.filter(description="")

    context = {'profile': profile, 'topSkills':topSkills, 'otherSkills':otherSkills}

    return render(request, 'users/user-profile.html', context)



@login_required(login_url='login')
def userAccount(request):
    # profile = Profile.objects.get(id=pk)
    profile = request.user.profile
    skills = profile.skill_set.all()

    context = {'profile': profile, 'skills':skills}

    return render(request, 'users/account.html', context)



@login_required(login_url='login')
def editAccount(request):
    profile = request.user.profile
    form = ProfileForm(instance=profile)
    context = {'form': form}

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('user-account')

    return render(request, 'users/edit-account.html', context)



@login_required(login_url='login')
def create_skill(request):
    profile = request.user.profile
    form = SkillForm()

    if request.method == 'POST':
        form = SkillForm(request.POST)
        if form.is_valid():
            skill = form.save(commit=False)
            skill.owner = profile
            skill.save()
            messages.success(request, "Skill was added Successfully!!")
            return redirect('user-account')
        
    context = {'form': form}

    return render(request, 'users/skill_form.html', context)



@login_required(login_url='login')
def update_skill(request, pk):
    profile = request.user.profile
    skill = profile.skill_set.get(id=pk)
    form = SkillForm(instance=skill)

    if request.method == 'POST':
        form = SkillForm(request.POST, instance=skill)
        if form.is_valid():
            form.save()
            messages.success(request, "Skill updated Successfully!!")
            return redirect('user-account')

    context = {'form': form}

    return render(request, 'users/skill_form.html', context)



@login_required(login_url='login')
def delete_skill(request, pk):
    profile = request.user.profile
    skill = profile.skill_set.get(id=pk)

    if request.method == 'POST':
        skill.delete()
        messages.success(request, "Skill deleted Successfully!!")
        return redirect('user-account')

    context = {'object': skill}

    return render(request, 'delete_template.html', context)



@login_required(login_url='login')
def inbox(request):
    profile = request.user.profile
    messagesRequests = profile.messages.all()   # 'messages' is the 'related_name' in the Message class of recipient
    unreadCount = messagesRequests.filter(is_read=False).count()

    context = {'messagesRequests': messagesRequests, 'unreadCount': unreadCount}

    return render(request, 'users/inbox.html', context)



@login_required(login_url='login')
def viewMessage(request, pk):
    profile = request.user.profile
    message = profile.messages.get(id=pk)
    if not message.is_read:
        message.is_read = True
        message.save()

    context = {'message': message}

    return render(request, 'users/message.html', context)



def createMessage(request, pk):
    recipient = Profile.objects.get(id=pk)
    # The sender can send a message without login (sender=None) (we can also verify it by .is_authenticated)
    try:
        sender = request.user.profile
    except:
        sender = None

    form = MessageForm()

    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = sender
            message.recipient = recipient
            if sender:
                message.name_sender = sender.name
                message.email = sender.email

            message.save()
            messages.success(request, "Your message was successfullly sent !")
            return redirect('user-profile', pk=recipient.id)

    context = {'form': form, 'recipient': recipient}

    return render(request, 'users/message_form.html', context)


