from rest_framework import serializers, viewsets

from course.models import Course


class CourseListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Course
        fields = ['slug', 'name', 'image']

class CourseDetailSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Course
        fields = ['name', 'image', 'longitude', 'latitude']
        extra_kwargs = {
            'url': {'lookup_field': 'slug'},
        }


class CourseViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Course.objects.filter(is_active=True)
    lookup_field = 'slug'
    search_fields = ('name', 'slug', 'area', 'city')

    def get_serializer_class(self):
        if self.action == 'list':
            return CourseListSerializer
        else:
            return CourseDetailSerializer
