from rest_framework import serializers, viewsets

from course.models import Course
from disc.models import Disc


class DiscSerializer(serializers.ModelSerializer):
    course = serializers.SlugRelatedField(slug_field='name', queryset=Course.objects.all())

    class Meta:
        model = Disc
        fields = ['course', 'maker', 'model', 'color']


class DiscViewSet(viewsets.ModelViewSet):
    queryset = Disc.objects.all()
    serializer_class = DiscSerializer
