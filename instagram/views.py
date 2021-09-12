from django.contrib.auth.models import User
from instagram.models import Image, Profile
from django.shortcuts import render

# Create your views here.
def home(request):
    images = Image.objects.all()

    return render(request,'index.html',{"images": images})


def profile(request,id):
    profile = Profile.objects.get(id=id)

    if request.method == 'POST':
        if 'new_user_id' in request.POST:
            new_user_id = request.POST.get('new_user_id')#getting the user id
            new_user = User.objects.get(id=new_user_id)# getting the new user

            my_profile = Profile.objects.get(user=request.user) #my profile
            my_profile.following.add(new_user)# add the new user to my following
            my_profile.save()

            new_user_profile = Profile.objects.get(user=new_user)
            new_user_profile.followers.add(request.user)#add my profile to their followers
            new_user_profile.save()
    return render(request,'profile.html',locals())
