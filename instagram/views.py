from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.http.response import Http404, HttpResponseRedirect
from instagram.models import Comments, Image, Profile
from django.shortcuts import redirect, render
from .forms import CreateProfileForm,UploadImageForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='/accounts/login/')
def create_profile(request):
    current_user = request.user
    if request.method == 'POST':
        form  = CreateProfileForm(request.POST,request.FILES)
        if form.is_valid():
            profile = form.save(commit = False)
            profile.user = current_user
            profile.save()
        return HttpResponseRedirect('/') 
    else:
        form = CreateProfileForm()
    return render(request,'create_profile.html',{"form":form})           


@login_required(login_url='/accounts/login/')
def home(request):
    images = Image.objects.all()
    comments = Comments.objects.all()
    photos = Profile.objects.all()
    comments_count = comments.count()
    return render(request,'index.html',{"images": images,"comments":comments,"photos":photos})


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

def comment(request,image_id):
    image = Image.objects.get(pk=image_id)
    content = request.GET.get("comment")
    print(content)   
    user = request.user
    comment = Comments(image = image,content = content,user = user)
    comment.save_comment() 
    return redirect('home')


def like_photo(request,image_id):
    image = Image.objects.get(pk=image_id)
    liked = False
    current_user = request.user
    try:
        profile = Profile.objects.get(user = current_user)
    except  Profile.DoesNotExist:
        raise Http404
    if image.likes.filter(id=profile.id).exists():
        image.likes.remove(profile)
        liked = False
    else:
        image.likes.add(profile)
        liked = True
    return HttpResponseRedirect(reverse('home')) 


def search_users(request):
    if 'username' in request.GET and request.GET["username"]:
        searched_user = request.GET.get("username")
        print(searched_user)  
        users = Profile.search_user(searched_user)
        print(users)
        message = f"{searched_user}"
        

        return render(request,'search.html',{"message":message,"users":users})

    else:
        message = "You have not searched for any user"
        return render(request,'search.html',{"message":message})   

@login_required(login_url='/accounts/login/')
def upload_image(request):
    current_user = request.user
    try:
        profile = Profile.objects.get(user = current_user)
    except Profile.DoesNotExist:
        raise Http404()
    if request.method == "POST":
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.profile = profile
            image.save()
        return redirect('home')
    else:
        form = UploadImageForm()
    return render(request, 'upload_image.html', {"form": form})                

