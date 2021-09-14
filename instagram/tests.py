from django.test import TestCase
from .models import Image, Comments,Profile
from django.contrib.auth.models import User

# Create your tests here.
class CommentTestClass(TestCase):

    def setUp(self):
        self.sammie = User(username = "sammie", email = "sammie@gmail.com",password = "123345678")
        self.profile = Profile(bio = "cool",user = self.sammie)
        self.allan = Image(image = "imageurl",name = "allan",caption="cool",profile=self.profile)
        self.comment = Comments(image=self.allan, content= 'cool', user = self.sammie)

        self.sammie.save()
        self.profile.save()
        self.allan.save_image()
        self.comment.save_comment()

    def tearDown(self):
        Image.objects.all().delete()
        Comments.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.comments,Comments))   

    def test_save_comment(self):
        comments = Comments.objects.all()
        self.assertTrue(len(comments)>0)   

    def test_delete_comment(self):
        comments1 = Comments.objects.all()
        self.assertEqual(len(comments1),1)
        self.comment.delete_comment()
        comments2 = Comments.objects.all()
        self.assertEqual(len(comments2),0)      

class ProfileTestClass(TestCase):
    def setUp(self):
        self.sammie = User(username = "sam", email = "sam@gmail.com",password = "123423355465")
        self.profile = Profile(bio='bio', user= self.sammie)
        self.sammie.save()

    def tearDown(self):
        Profile.objects.all().delete()
        User.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.sammie, User))
        self.assertTrue(isinstance(self.profile, Profile))

    def test_search_user(self):
        user = Profile.search_user(self.sammie)
        self.assertEqual(len(user), 1)

class ImageTestClass(TestCase):
    def setUp(self):
        self.sammie = User(username = "sammie", email = "sammie@gmail.com",password = "12344576")
        self.profile = Profile(bio='bio', user= self.sammie)
        self.allan = Image(image = 'imageurl', name ='allan', caption = 'Chicken Taco', profile = self.profile)
        self.maua = Image(image = 'imageurl', name ='mustang', caption = 'muscle car', profile = self.profile)

        self.sammie.save()
        self.profile.save()
        self.allan.save_image()

    def tearDown(self):
        Image.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.allan, Image))

    def test_save_image_method(self):
        images = Image.objects.all()
        self.assertTrue(len(images)> 0)

    def test_delete_image(self):
        images1 = Image.objects.all()
        self.assertEqual(len(images1),1)
        self.allan.delete_image()
        images2 = Image.objects.all()
        self.assertEqual(len(images2),0)

    
   