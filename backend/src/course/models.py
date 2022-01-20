from email.policy import default
from django.db import models
from django.template.defaultfilters import slugify
from django.utils.translation import gettext_lazy as _


class Course(models.Model):
    mextrix_id = models.PositiveIntegerField(unique=True, null=False, blank=False)
    name = models.CharField(_('name'), max_length=255, unique=True, null=False, blank=False, db_index=True)
    slug = models.SlugField(_('slug'), max_length=255, unique=True, null=False, blank=False, db_index=True)
    image = models.ImageField(_('image'), upload_to='courses', null=True, blank=False, default='courses/default_image_flying_disc.png')

    longitude = models.DecimalField(_('longitude'), max_digits=18, decimal_places=15, null=False, blank=False)
    latitude = models.DecimalField(_('latitude'), max_digits=18, decimal_places=15, null=False, blank=False)
    area = models.CharField(_('area'), max_length=255, db_index=True, null=True, blank=False)
    city = models.CharField(_('city'), max_length=255, db_index=True, null=True, blank=False)

    is_active = models.BooleanField(_('is_active'), default=True)

    class Meta:
        ordering = ['slug']
        verbose_name = _('course')
        verbose_name_plural = _('courses')

    def __str__(self):
        return f'{self.name}'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)

        return super().save(*args, **kwargs)
