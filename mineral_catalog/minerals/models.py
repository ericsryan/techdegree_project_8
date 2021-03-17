from django.db import models
from django.utils.text import slugify


class Mineral(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, primary_key=True)
    caption = models.CharField(max_length=300)

    def __str__(self):
        return self.name

    def _get_unique_slug(self):
        slug = slugify(self.name)
        unique_slug = slug
        num = 2
        while Mineral.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._get_unique_slug()
        super().save(*args, **kwargs)


class Attribute(models.Model):
    name = models.CharField(max_length=255)
    content = models.CharField(max_length=300)
    order = models.IntegerField(default=0)
    mineral = models.ForeignKey(Mineral,
                                models.SET_NULL,
                                blank=True,
                                null=True)

    class Meta:
        ordering = ['order',]

    def __str__(self):
        return self.name + ": " + self.content
