from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse


class Website(models.Model):
    website_name = models.CharField(max_length=200)
    website_url = models.CharField(max_length=1000)
    website_cms = models.CharField(max_length=100)

    def __str__(self):
        return self.website_name


class Categories(models.Model):
    website_name = models.ForeignKey(Website, on_delete=models.CASCADE)
    title = models.CharField(max_length=500)
    author = models.ForeignKey('auth.User')
    text = models.TextField(blank = True, null = True)
    published_date = models.DateTimeField(default=timezone.now)

    def get_absolute_url(self):
        return reverse('wiki:detail', kwargs={'pk': self.pk})

    def publish(self):
        self.published_date -timezone.now()
        self.save()

    def __str__(self):
        return self.title
