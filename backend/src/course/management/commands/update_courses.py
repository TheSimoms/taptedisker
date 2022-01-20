import datetime
import requests
from decimal import Decimal
from django.core.management.base import BaseCommand
from django.db.utils import IntegrityError
from course.models import Course

class Command(BaseCommand):
    help = 'Fetches latest course information'
    URL = 'https://discgolfmetrix.com/api.php?content=courses_list&country_code={country_code}'

    def add_arguments(self, parser):
        parser.add_argument('country_code')

    def handle(self, *args, **options):
        url = self.URL.format(country_code=options['country_code'])
        response = requests.get(url)
        courses = filter(self._filter_courses, response.json()['courses'])

        Course.objects.all().update(is_active=False)

        for course in courses:
            try:
                area = course['Area']
                city = course['City']

                Course.objects.update_or_create(
                    mextrix_id=course['ID'],
                    defaults={
                        'mextrix_id': course['ID'],
                        'name': course['Fullname'],
                        'longitude': Decimal(course['Y']),
                        'latitude': Decimal(course['X']),
                        'area': area if area else None,
                        'city': city if city else None,
                        'is_active': True,
                    },
                )
            except IntegrityError:
                pass

    @staticmethod
    def _filter_courses(course):
        if course['ParentID'] is not None:
            return False

        if course['Enddate'] is not None:
            end_date = datetime.datetime.strptime(course['Enddate'], '%Y-%m-%d')

            if end_date.date() <= datetime.date.today():
                return False

        if not (course['X'] and course['Y']):
            return False

        if 'ikke i bruk' in course['Fullname'].lower():
            return False

        return True
