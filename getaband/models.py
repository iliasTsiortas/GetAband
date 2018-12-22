from django.db import models

# Create your models here.
class User(models.Model):

    username = models.CharField(max_length=50,)
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=100)
    # change password to be secured/cryptoed
    password = models.CharField(max_length=50)
    age = models.IntegerField(default= 20)
    longitude = models.DecimalField(max_digits=20, decimal_places=12)
    latitude = models.DecimalField(max_digits=20, decimal_places=12)
    location_text = models.TextField(default="")
    aboutMe = models.TextField(default="")

    def __str__(self):
        return "%s %s %s %s %s %s %s" % (self.username , self.firstName, self.lastName ,
                                         self.password ,self.longitude, self.latitude, self.location_text)



class Instruments(models.Model):
    user =models.ForeignKey(User, on_delete=models.CASCADE)
    Instrument = models.CharField(max_length=200)
    experience = models.CharField(max_length=50)

    def __str__(self):
        return "%s %s %s" % (self.user, self.Instrument, self.experience)


class urls(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    url = models.URLField(null=True)
