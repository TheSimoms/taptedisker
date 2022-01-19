from django.contrib import admin

from course.models import Course

class CourseAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}

admin.site.register(Course, CourseAdmin)
