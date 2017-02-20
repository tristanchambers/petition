from django.db import models

# Create your models here.
# https://docs.djangoproject.com/en/1.10/topics/db/models/
# https://docs.djangoproject.com/en/1.10/ref/models/fields/

class Petition(models.Model):
    title = models.CharField(max_length=255)
    hero_image = models.URLField(default='')
    created_by = models.CharField(max_length=255)
    address_to = models.CharField(max_length=255)
    teaser_text = models.CharField(max_length=255, help_text="Appears in search results, and social media shares.")
    description = models.TextField(max_length=5000)
    letter = models.TextField(max_length=10000)
    thank_you_message = models.TextField(max_length=1000)
    goal = models.PositiveIntegerField(default=1000)
    region_city = models.CharField(max_length=255)
    region_state = models.CharField(max_length=2)
    slug = models.SlugField(unique=True)
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return "/%s/" % self.slug

    # Make property for current number of signatures
    @property
    def signatures_num(self):
        signatures = Signature.objects.filter(petition=self.pk)
        return(len(signatures))

class Signature(models.Model):
    petition = models.ForeignKey(Petition, editable=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    street_address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=2)
    email = models.EmailField()
    comment = models.TextField(max_length=500, blank=True)
    dont_show_name = models.BooleanField(verbose_name="Don't display my name")
    opt_in = models.BooleanField(verbose_name="Keep me updated on this issue", default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    def __str__(self):
        if not self.dont_show_name:
            return '%s %s' % (self.first_name, self.last_name[0] + '.')
        else:
            return "name not displayed"
