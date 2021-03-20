from django.db import models
from django.utils.text import slugify


class Mineral(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, primary_key=True)
    caption = models.CharField(max_length=300)
    category = models.CharField(max_length=300, blank=True, null=True)
    group = models.CharField(max_length=300, blank=True, null=True)
    formula = models.CharField(max_length=300, blank=True, null=True)
    strunz_classification = models.CharField(max_length=300, blank=True, null=True)
    crystal_system = models.CharField(max_length=300, blank=True, null=True)
    mohs_scale_hardness = models.CharField(max_length=300, blank=True, null=True)
    luster = models.CharField(max_length=300, blank=True, null=True)
    color = models.CharField(max_length=300, blank=True, null=True)
    specific_gravity = models.CharField(max_length=300, blank=True, null=True)
    cleavage = models.CharField(max_length=300, blank=True, null=True)
    diaphaneity = models.CharField(max_length=300, blank=True, null=True)
    crystal_habit = models.CharField(max_length=300, blank=True, null=True)
    streak = models.CharField(max_length=300, blank=True, null=True)
    optical_properties = models.CharField(max_length=300, blank=True, null=True)
    refractive_index = models.CharField(max_length=300, blank=True, null=True)
    unit_cell = models.CharField(max_length=300, blank=True, null=True)
    crystal_symmetry = models.CharField(max_length=300, blank=True, null=True)

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
