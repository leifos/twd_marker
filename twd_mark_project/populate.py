__author__ = 'leif'
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE','twd_mark_project.settings')


import django
django.setup()

from marker.models import AssessmentSheet

def populate():

    studSheet = AssessmentSheet.objects.get_or_create(studentno='12345677')[0]
    studSheet.firstname = 'Jane'
    studSheet.lastname = 'Doe'
    studSheet.chapter1 = True
    studSheet.save()



if __name__ == '__main__':
    print "Start pop script"
    populate()