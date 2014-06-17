from django.db import models


class Category(models.Model):
    title       = models.CharField(max_length=100)
    slug        = models.SlugField(max_length=100, unique=True)
    description = models.TextField()
    created     = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ( '-created' , 'title' )

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title

    def published_entries(self):
        import datetime
        now = datetime.datetime.now()
        return self.entries.filter( publish_date__lte=now ).order_by( '-publish_date' )

class Entry(models.Model):
    category     = models.ForeignKey(Category, related_name='entries')
    title        = models.CharField(max_length=100)
    slug         = models.SlugField(max_length=100, unique=True)
    description  = models.TextField()
    image        = models.ImageField(upload_to='blog')
    content      = models.TextField()
    publish_date = models.DateTimeField(auto_now_add=True)
    update_date  = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ( '-publish_date' , 'title' )

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title

    def get_url(self):
        from django.core.urlresolvers import reverse
        return reverse('sitelight.views.entry', args=[str(self.category.slug), str(self.slug)])
