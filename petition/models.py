from django.db import models

# Create your models here.
# https://docs.djangoproject.com/en/1.10/topics/db/models/
# https://docs.djangoproject.com/en/1.10/ref/models/fields/

class Petition(models.Model):
    title = models.CharField(max_length=255)
    hero_image = models.URLField(default='')
    created_by = models.CharField(max_length=255)
    address_to = models.CharField(max_length=255)
    description = models.TextField(max_length=5000)
    letter = models.TextField(max_length=10000)
    goal = models.PositiveIntegerField(default=1000)
    region_city = models.CharField(max_length=255)
    region_state = models.CharField(max_length=2)
    def __str__(self):
        return self.title

class Signature(models.Model):
    petition = models.ForeignKey(Petition)
    first = models.CharField(max_length=100)
    last = models.CharField(max_length=100)
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=2)
    email = models.EmailField()
    dont_show_name = models.BooleanField(verbose_name="Don't display my name")
    opt_in = models.BooleanField(verbose_name="Keep me updated on this issue", default=True)
    def __str__(self):
        return '%s %s' % (self.first, self.last)
