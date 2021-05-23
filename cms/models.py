from django.db import models
import datetime
from django.urls import reverse
from django.contrib.auth.models import User
from markdown import markdown
# Create your models herei.

VIEWABLE_STATUS = [3, 4]
class Category(models.Model):
    label = models.CharField(blank=True, max_length=50)
    slug = models.SlugField()

    class Meta:
      verbose_name_plural = "categories"

    def __unicode__(self):
        return self.label

class ViewableManager(models.Manager):
    def get_queryset(self):
        default_queryset = super(ViewableManager, self).get_queryset()
        return default_queryset.filter(status__in=VIEWABLE_STATUS)

class Story(models.Model):
    STATUS_CHOICES = (
        (1, "Needs Edit"),
        (2, "Needs Approval"),
        (3, "Published"),
        (4, "Archived"),
    )

    title = models.CharField(max_length=200)
    slug = models.SlugField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    markdown_content = models.TextField()
    html_content = models.TextField(editable=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)
    created = models.DateTimeField(default=datetime.datetime.now)
    modified = models.DateTimeField(default=datetime.datetime.now)

    admin_objects = models.Manager()
    objects = ViewableManager()

    class Meta:
        ordering = ['modified']
        verbose_name_plural = "stories"

    def get_absolute_url(self):
        return reverse("cms:storydetail", args=[self.slug,])

    def save(self):
        self.html_content = markdown(self.markdown_content)
        self.modified = datetime.datetime.now()
        super(Story, self).save()
