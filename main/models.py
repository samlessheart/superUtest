from typing import Iterable, Optional
from django.db import models
from django.contrib.auth.models import AbstractUser
from PIL import Image


def compress(image): #you can compress the images before upload into AWS
    im = Image.open(image)
    new_image = im.resize((400, 400))
    return new_image

class CustomUser(AbstractUser):
   picture = models.ImageField((), upload_to= "picture/" , blank=True ,null=True)
   bio = models.CharField(max_length=200, null=True, blank=True)





       