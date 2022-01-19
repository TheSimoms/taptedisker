from rest_framework import routers

from course.api import CourseViewSet
from disc.api import DiscViewSet


router = routers.DefaultRouter()

router.register(r'courses', CourseViewSet)
router.register(r'discs', DiscViewSet)
