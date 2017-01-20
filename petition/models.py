from django.db import models

# Create your models here.
# https://docs.djangoproject.com/en/1.10/topics/db/models/
# https://docs.djangoproject.com/en/1.10/ref/models/fields/

class Petition(models.Model):
    title = models.CharField(max_length=255)
    def __str__(self):
        return self.title

class Signature(models.Model):
    petition = models.ForeignKey(Petition)
    first = models.CharField(max_length=100)
    last = models.CharField(max_length=100)
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    zip = models.CharField(max_length=5)
    def __str__(self):
        return '%s %s' % (self.first, self.last)
