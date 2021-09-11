from instagram.models import Image
from django.shortcuts import render

# Create your views here.
def home(request):
    images = Image.objects.all()
    return render(request,'index.html',{"images": images})

