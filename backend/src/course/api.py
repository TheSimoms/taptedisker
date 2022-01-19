from rest_framework import serializers, viewsets

from course.models import Course


class CourseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Course
        fields = ['url', 'name', 'longitude', 'latitude']
        extra_kwargs = {
            'url': {'lookup_field': 'slug'},
        }


class CourseViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    lookup_field = 'slug'
