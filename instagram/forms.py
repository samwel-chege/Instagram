from .models import Image,Profile,Comments
from django.forms import ModelForm

class CreateProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ['created','account_holder','folloers','following']

class UploadImageForm(ModelForm):
    class Meta:
        model = Image
        exclude =['user']
        
                