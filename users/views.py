from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import CustomUserCreationForm, ProfileForm
from .models import Profile


def loginUser(request):
    page = 'login'
    context = {'page': page}

    if request.user.is_authenticated:
        return redirect('profiles')

    if request.method == 'POST':
        username = request.POST['username']
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
            return redirect('profiles')
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
    profiles = Profile.objects.all()
    context = {'profiles': profiles}

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