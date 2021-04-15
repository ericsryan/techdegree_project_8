from django.db import models
from django.utils.text import slugify


class Mineral(models.Model):
    name = models.TextField()
    slug = models.SlugField(max_length=255, unique=True, primary_key=True)
    caption = models.TextField()
    category = models.TextField(blank=True, null=True)
    group = models.TextField(blank=True, null=True)
    formula = models.TextField(blank=True, null=True)
    strunz_classification = models.TextField(blank=True, null=True)
    crystal_system = models.TextField(blank=True, null=True)
    mohs_scale_hardness = models.TextField(blank=True, null=True)
    luster = models.TextField(blank=True, null=True)
    color = models.TextField(blank=True, null=True)
    specific_gravity = models.TextField(blank=True, null=True)
    cleavage = models.TextField(blank=True, null=True)
    diaphaneity = models.TextField(blank=True, null=True)
    crystal_habit = models.TextField(blank=True, null=True)
    streak = models.TextField(blank=True, null=True)
    optical_properties = models.TextField(blank=True, null=True)
    refractive_index = models.TextField(blank=True, null=True)
    unit_cell = models.TextField(blank=True, null=True)
    crystal_symmetry = models.TextField(blank=True, null=True)

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
        return self
