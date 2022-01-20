from django.contrib import admin

from course.models import Course

class CourseAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}
    search_fields = ('name', 'slug', )

admin.site.register(Course, CourseAdmin)
