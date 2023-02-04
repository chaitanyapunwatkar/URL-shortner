from django.db import models
import qrcode
# Create your models here.

class UrlData(models.Model):
    url = models.CharField(max_length=200)
    short = models.CharField(max_length=15)
    
    def __str__(self):
        return "URL {0} is shorten to {1}".format(self.url, self.short)
    