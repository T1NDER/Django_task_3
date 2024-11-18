from django.db import models
from django.urls import reverse
from django.utils.text import slugify

class Phone(models.Model):
    name = models.CharField(max_length=40)
    price = models.FloatField()
    image = models.ImageField(upload_to='phones_images')
    release_date = models.DateField()
    lte_exists = models.BooleanField()

    slug = models.SlugField(max_length=200, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify.slufify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url_(self):
        return reverse('phone_detail', kwargs={'slug': self.slug})
