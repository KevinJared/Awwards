from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save,post_delete
from django.dispatch import receiver
import datetime as dt

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30, blank=True)
    user_name = models.CharField(max_length=30,blank=True)
    prof_pic = models.ImageField(upload_to= 'profiles/', blank=True,default="profile/a.jpg")
    bio = models.TextField(default="Welcome Me!")


    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    def post(self, form):
        image = form.save(commit=False)
        image.user = self
        image.save()

    def comment(self, photo, text):
        Comment(text=text, photo=photo, user=self).save()
    
    @classmethod
    def search_by_user(cls,search_term):
        content = cls.objects.filter(user__username__icontains=search_term)
        return content


class Post(models.Model):
    sitename=models.CharField(max_length=50)
    url = models.CharField(max_length=50)
    Description=models.CharField(max_length=800)
    image = models.FileField(upload_to='posts/')
    post_date = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, related_name="posted_by", on_delete=models.CASCADE)
    Technology = models.CharField(max_length=50)
    country = models.CharField(max_length=50)

    @property
    def get_comments(self):
        return self.comments.all()

    class Meta:
        ordering = ["-pk"]

class Comment(models.Model):
    text = models.TextField()
    photo = models.ForeignKey(Post, related_name='comment')
    user = models.ForeignKey(Profile, related_name='comment')
                              