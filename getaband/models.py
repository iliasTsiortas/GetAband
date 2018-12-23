from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField(default= 20)
    longitude = models.DecimalField(max_digits=20, decimal_places=12,default=0)
    latitude = models.DecimalField(max_digits=20, decimal_places=12, default=0)
    location_text = models.TextField(default="")
    aboutMe = models.TextField(default="")


@receiver(post_save, sender= User)
def create_user_profile(sender,instance,created, **kwargs):
     if created:
         UserProfile.objects.create(user= instance)

@receiver(post_save, sender= User)
def save_user_profile(sender,instance,**kwargs):
    instance.userprofile.save()


class Instruments(models.Model):
    user =models.ForeignKey(User, on_delete=models.CASCADE)
    Instrument = models.CharField(max_length=200)
    experience = models.CharField(max_length=50)

    def __str__(self):
        return "%s %s %s" % (self.user, self.Instrument, self.experience)


class urls(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    url = models.URLField(null=True)
