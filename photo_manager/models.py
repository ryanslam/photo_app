from django.db import models
from django.utils.safestring import mark_safe


class HomePagePhoto(models.Model):
    image = models.ImageField(upload_to='homepage/', blank=True, null=True)
    date = models.DateTimeField('date and time posted', blank=True, null=True)
    name = models.CharField(max_length=100, default=None, blank=True)

    def thumb(self):
        if self.image:
            return mark_safe(u'<img src="%s" width=60 height=60 />' % self.image.url)
        else:
            return mark_safe('No image file found')

    def __unicode__(self):
        return self.name


class AboutInfo(models.Model):
    image1 = models.ImageField(upload_to='about/', blank=True, null=True)
    image2 = models.ImageField(upload_to='about/', blank=True, null=True)
    body = models.TextField()
    title = models.CharField(max_length=100, default=None, blank=True)

    def __unicode__(self):
        return self.title


class PhotographyPhoto(models.Model):
    CATEGORY_CHOICES = (
        ('Ocean', 'Ocean'),
        ('Gadgets', 'Gadgets'),
        ('Sky', 'Sky'),
        ('Wildlife', 'Wildlife'),
        ('Portraits', 'Portraits'),
        ('Urban', 'Urban'),
        ('Product Design', 'Product Design'),
        ('Forest', 'Forest'),
        ('Flower', 'Flower'),
    )
    image = models.ImageField(upload_to='photography/', blank=True, null=True)
    category = models.CharField(max_length=25, choices=CATEGORY_CHOICES, default='Ocean')
    name = models.CharField(max_length=100, default=None, blank=True)
    cover = models.BooleanField(default=False)

    # IMPORTANT: ONLY ONE ITEM WITH COVER = TRUE

    def thumb(self):
        if self.image:
            return mark_safe(u'<img src="%s" width=60 height=60 />' % self.image.url)
        else:
            return mark_safe('No image file found')

    def __unicode__(self):
        return self.name


class PortfolioEntry(models.Model):
    RESUME_FIELDS = (
        ('Education', 'Education'),
        ('Experience', 'Experience'),
    )
    category = models.CharField(max_length=25, choices=RESUME_FIELDS, default='Education')
    year_start = models.CharField(max_length=10, default=None, blank=True)
    year_end = models.CharField(max_length=10, default=None, blank=True)
    name = models.CharField(max_length=150, default=None, blank=True)
    position = models.CharField(max_length=150, default=None, blank=True, null=True)
    location = models.CharField(max_length=150, default=None, blank=True, null=True)
    description = models.TextField()

    def __unicode__(self):
        return self.name
