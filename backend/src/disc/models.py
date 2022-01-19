from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

from course.models import Course


class Disc(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_('user'), on_delete=models.CASCADE, related_name='discs', null=False)
    course = models.ForeignKey(Course, verbose_name=_('course'), on_delete=models.CASCADE, related_name='discs', null=False)

    maker = models.CharField(max_length=255, null=False)
    plastic = models.CharField(max_length=255, null=True)
    model = models.CharField(max_length=255, null=False)
    color = models.CharField(max_length=255, null=False)

    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)

    is_found = models.BooleanField(null=False, default=False)

    class Meta:
        ordering = ['course', 'maker', 'model', 'color']
        verbose_name = _('disc')
        verbose_name_plural = _('discs')

    def __str__(self):
        return '{plastic}{model} ({color}) - {maker} - {course}'.format(
            maker=self.maker,
            plastic=self.plastic + ' ' if self.plastic else '',
            model=self.model,
            color=self.color,
            course=self.course,
        )
