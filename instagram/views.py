from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.http.response import Http404, HttpResponseRedirect
from instagram.models import Comments, Image, Profile
from django.shortcuts import redirect, render
from django.urls import reverse

# Create your views here.
def home(request):
    images = Image.objects.all()
    comments = Comments.objects.all()
    comments_count = comments.count()
    return render(request,'index.html',{"images": images,"comments":comments})


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

