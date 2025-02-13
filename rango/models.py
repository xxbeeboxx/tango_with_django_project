from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    slug = models.SlugField()

    class Meta:
        verbose_name_plural = 'Categories'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)


    def __str__(self):
        return self.name

class Page(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE) #one to many relationship for each category and pages
    title = models.CharField(max_length=128)    #title of the page
    url = models.URLField() #stores webpage url
    views = models.IntegerField(default=0)  #tracks how many times the page has been viewed

    def __str__(self):
        return self.title
