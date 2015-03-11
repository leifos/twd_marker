from django.db import models
from django import forms



CHAPTER_CHOICES = (
    ('N','Not Completed'),('A','Attempted'),('C','Completed but after check in date'), ('P','Partially Completed'), ('F','Fully Completed')
)

LAB_CHOICES = ( (1,'Lab 1 - Mon 1-3'),
                (2,'Lab 2 - Mon 3-5'),
                (3,'Lab 3 - Tues 1-3'),
                (4,'Lab 4 - Tues 3-5'),
                (5,'Lab 5 - Wed 2-4'),
                (6,'Lab 6 - Wed 4-6'),
                (7,'Lab 7 - Thurs 1-3'),
                (8,'Lab 8 - Thurs 1-3'),
                (9,'Lab 9 - Fri 3-5'),
                (10,'Lab 10 - Wed 4-6'),
                (11,'Lab 11 - Wed 2-4'),
)


# Create your models here.
class AssessmentSheet(models.Model):

    firstname = models.CharField(max_length=64, verbose_name='First Name')
    lastname = models.CharField(max_length=64, verbose_name='Last Name')
    studentno = models.CharField(max_length=8, unique=True, verbose_name='Student Number')
    lab = models.IntegerField(default=0, choices=LAB_CHOICES, verbose_name='Please select the lab you are in')
    pa = models.URLField(verbose_name='PythonAnywhere Link',default='')
    github_username = models.CharField(max_length=64, verbose_name='GitHub Account',default='')
    github_repo = models.URLField(verbose_name='Github Repo Link',default='', unique=True)
    chapter3 = models.CharField(max_length=1, default='N', choices = CHAPTER_CHOICES, verbose_name='Chapter 3 - Setting Up - 26th Jan', help_text='')
    chapter4 = models.CharField(max_length=1, default='N', choices = CHAPTER_CHOICES, verbose_name='Chapter 4 - Django Basics - 26th Jan', help_text='')
    chapter5 = models.CharField(max_length=1, default='N', choices = CHAPTER_CHOICES, verbose_name='Chapter 5 - Templates - 26th Jan', help_text='')
    chapter6 = models.CharField(max_length=1, default='N', choices = CHAPTER_CHOICES, verbose_name='Chapter 6 - Models - 26th Jan', help_text='')
    chapter7 = models.CharField(max_length=1, default='N', choices = CHAPTER_CHOICES, verbose_name='Chapter 7 - MTV - 26th Jan', help_text='')
    chapter8 = models.CharField(max_length=1, default='N', choices = CHAPTER_CHOICES, verbose_name='Chapter 8 - Forms - 9th Feb', help_text='')
    chapter9 = models.CharField(max_length=1, default='N', choices = CHAPTER_CHOICES, verbose_name='Chapter 9 - User Auth - 9th Feb', help_text='')
    chapter10 = models.CharField(max_length=1, default='N', choices = CHAPTER_CHOICES, verbose_name='Chapter 10 - More Templates - 9th Feb', help_text='')
    chapter11 = models.CharField(max_length=1, default='N', choices = CHAPTER_CHOICES, verbose_name='Chapter 11 - Cookies - 28th Feb', help_text='')
    chapter12 = models.CharField(max_length=1, default='N', choices = CHAPTER_CHOICES, verbose_name='Chapter 12 - More User Auth - 28th Feb', help_text='')
    chapter13 = models.CharField(max_length=1, default='N', choices = CHAPTER_CHOICES, verbose_name='Chapter 13 - Bootstrap - 28th Feb', help_text='')
    chapter14 = models.CharField(max_length=1, default='N', choices = CHAPTER_CHOICES, verbose_name='Chapter 14 - Template Tags - 9th Mar', help_text='')
    chapter15 = models.CharField(max_length=1, default='N', choices = CHAPTER_CHOICES, verbose_name='Chapter 15 - Bing Search - 9th Mar', help_text='')
    chapter16 = models.CharField(max_length=1, default='N', choices = CHAPTER_CHOICES, verbose_name='Chapter 16-17 - Exercises - 9th Mar', help_text='')
    chapter21 = models.CharField(max_length=1, default='N', choices = CHAPTER_CHOICES, verbose_name='Chapter 21 - Deployed - 9th Mar', help_text='')
    notes = models.CharField(max_length=384, verbose_name='Please enter any exceptional circumstances that should be considered when marking your project (incidents need to be recorded in MyCampus for us to verify your claims).',default='',blank=True)

    def __unicode__(self):
        return self.firstname + " " + self.lastname


class AssessmentSheetForm(forms.ModelForm):
    studentno = forms.CharField(label='Student No.',max_length=7, min_length=7, help_text='Please enter your student no (without the letter)', required=True)
    lab = forms.ChoiceField(choices=LAB_CHOICES, help_text='Please select the lab you are in')
    pa = forms.URLField(label='PythonAnywere Link', help_text='If deployed, add your PythonAnyhwere Link: i.e. http://<username>.pythonanywhere.com/rango/', required=False)
    github_username = forms.CharField(max_length=64, help_text='Your GitHub Account name i.e. leifos', required=True)
    github_repo = forms.URLField(help_text='Github link to tango with django, i.e. https://github.com/leifos/tango_with_django', required=True)

    notes = forms.CharField(widget=forms.Textarea(attrs={'cols': 120, 'rows': 5}), help_text='Please enter any exceptional circumstances that should be considered when marking your project (incidents need to be recorded in MyCampus for us to verify your claims).', required=False)

    class Meta:
        # Provide an association between the ModelForm and a model
        model = AssessmentSheet
        fields = ('firstname','lastname','studentno','lab','pa','github_username','github_repo',
                  'chapter3','chapter4','chapter5','chapter6','chapter7',
                  'chapter8','chapter9','chapter10','chapter11','chapter12','chapter13','chapter14','chapter15','chapter16','chapter21',
                  'notes'
        )