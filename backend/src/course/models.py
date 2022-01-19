from django.db import models
from django.utils.translation import gettext_lazy as _


class Course(models.Model):
    name = models.CharField(_('name'), max_length=255, unique=True, null=False, db_index=True)
    slug = models.SlugField(_('slug'), max_length=255, unique=True, null=False, db_index=True)

    longitude = models.DecimalField(_('longitude'), max_digits=9, decimal_places=6)
    latitude = models.DecimalField(_('latitude'), max_digits=9, decimal_places=6)

    class Meta:
        ordering = ['slug']
        verbose_name = _('course')
        verbose_name_plural = _('courses')

    def __str__(self):
        return f'{self.name}'
