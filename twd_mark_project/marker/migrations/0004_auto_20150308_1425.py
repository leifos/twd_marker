# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('marker', '0003_auto_20150307_1637'),
    ]

    operations = [
        migrations.AddField(
            model_name='assessmentsheet',
            name='chapter10',
            field=models.CharField(default=b'N', help_text=b'Helpful hint', max_length=1, verbose_name=b'Chapter 10 - More Templates - 9th Feb', choices=[(b'N', b'Not Completed'), (b'A', b'Attempted'), (b'C', b'Completed but after check in date'), (b'P', b'Partially Completed'), (b'F', b'Fully Completed')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='assessmentsheet',
            name='chapter11',
            field=models.CharField(default=b'N', help_text=b'Helpful hint', max_length=1, verbose_name=b'Chapter 11 - Cookies - 28th Feb', choices=[(b'N', b'Not Completed'), (b'A', b'Attempted'), (b'C', b'Completed but after check in date'), (b'P', b'Partially Completed'), (b'F', b'Fully Completed')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='assessmentsheet',
            name='chapter12',
            field=models.CharField(default=b'N', help_text=b'Helpful hint', max_length=1, verbose_name=b'Chapter 12 - More User Auth - 28th Feb', choices=[(b'N', b'Not Completed'), (b'A', b'Attempted'), (b'C', b'Completed but after check in date'), (b'P', b'Partially Completed'), (b'F', b'Fully Completed')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='assessmentsheet',
            name='chapter13',
            field=models.CharField(default=b'N', help_text=b'Helpful hint', max_length=1, verbose_name=b'Chapter 13 - Bootstrap - 28th Feb', choices=[(b'N', b'Not Completed'), (b'A', b'Attempted'), (b'C', b'Completed but after check in date'), (b'P', b'Partially Completed'), (b'F', b'Fully Completed')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='assessmentsheet',
            name='chapter14',
            field=models.CharField(default=b'N', help_text=b'Helpful hint', max_length=1, verbose_name=b'Chapter 14 - Template Tags - 9th Mar', choices=[(b'N', b'Not Completed'), (b'A', b'Attempted'), (b'C', b'Completed but after check in date'), (b'P', b'Partially Completed'), (b'F', b'Fully Completed')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='assessmentsheet',
            name='chapter15',
            field=models.CharField(default=b'N', help_text=b'Helpful hint', max_length=1, verbose_name=b'Chapter 15 - Bing Search - 9th Mar', choices=[(b'N', b'Not Completed'), (b'A', b'Attempted'), (b'C', b'Completed but after check in date'), (b'P', b'Partially Completed'), (b'F', b'Fully Completed')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='assessmentsheet',
            name='chapter16',
            field=models.CharField(default=b'N', help_text=b'Helpful hint', max_length=1, verbose_name=b'Chapter 16-17 - Exercises - 9th Mar', choices=[(b'N', b'Not Completed'), (b'A', b'Attempted'), (b'C', b'Completed but after check in date'), (b'P', b'Partially Completed'), (b'F', b'Fully Completed')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='assessmentsheet',
            name='chapter21',
            field=models.CharField(default=b'N', help_text=b'Helpful hint', max_length=1, verbose_name=b'Chapter 21 - Deployed - 9th Mar', choices=[(b'N', b'Not Completed'), (b'A', b'Attempted'), (b'C', b'Completed but after check in date'), (b'P', b'Partially Completed'), (b'F', b'Fully Completed')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='assessmentsheet',
            name='chapter8',
            field=models.CharField(default=b'N', help_text=b'Helpful hint', max_length=1, verbose_name=b'Chapter 8 - Forms - 9th Feb', choices=[(b'N', b'Not Completed'), (b'A', b'Attempted'), (b'C', b'Completed but after check in date'), (b'P', b'Partially Completed'), (b'F', b'Fully Completed')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='assessmentsheet',
            name='chapter9',
            field=models.CharField(default=b'N', help_text=b'Helpful hint', max_length=1, verbose_name=b'Chapter 9 - User Auth - 9th Feb', choices=[(b'N', b'Not Completed'), (b'A', b'Attempted'), (b'C', b'Completed but after check in date'), (b'P', b'Partially Completed'), (b'F', b'Fully Completed')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='assessmentsheet',
            name='github_repo',
            field=models.URLField(default=b'', verbose_name=b'Github link to tango with django, i.e. https://github.com/leifos/tango_with_django'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='assessmentsheet',
            name='github_username',
            field=models.CharField(default=b'', max_length=64, verbose_name=b'Your GitHub Account name i.e. leifos'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='assessmentsheet',
            name='notes',
            field=models.CharField(default=b'', max_length=256, verbose_name=b'Please enter any exceptional circumstances that should be considered when marking your project (incidents need to be recorded in MyCampus for us to verify your claims).'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='assessmentsheet',
            name='pa',
            field=models.URLField(default=b'', verbose_name=b'PythonAnyhwere Link to your deployed app: i.e. http://<username>.pythonanywhere.com/rango/'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='assessmentsheet',
            name='chapter3',
            field=models.CharField(default=b'N', help_text=b'Helpful hint', max_length=1, verbose_name=b'Chapter 3 - Setting Up - 26th Jan', choices=[(b'N', b'Not Completed'), (b'A', b'Attempted'), (b'C', b'Completed but after check in date'), (b'P', b'Partially Completed'), (b'F', b'Fully Completed')]),
        ),
        migrations.AlterField(
            model_name='assessmentsheet',
            name='chapter4',
            field=models.CharField(default=b'N', help_text=b'Helpful hint', max_length=1, verbose_name=b'Chapter 4 - Django Basics - 26th Jan', choices=[(b'N', b'Not Completed'), (b'A', b'Attempted'), (b'C', b'Completed but after check in date'), (b'P', b'Partially Completed'), (b'F', b'Fully Completed')]),
        ),
        migrations.AlterField(
            model_name='assessmentsheet',
            name='chapter5',
            field=models.CharField(default=b'N', help_text=b'Helpful hint', max_length=1, verbose_name=b'Chapter 5 - Templates - 26th Jan', choices=[(b'N', b'Not Completed'), (b'A', b'Attempted'), (b'C', b'Completed but after check in date'), (b'P', b'Partially Completed'), (b'F', b'Fully Completed')]),
        ),
        migrations.AlterField(
            model_name='assessmentsheet',
            name='chapter6',
            field=models.CharField(default=b'N', help_text=b'Helpful hint', max_length=1, verbose_name=b'Chapter 6 - Models - 26th Jan', choices=[(b'N', b'Not Completed'), (b'A', b'Attempted'), (b'C', b'Completed but after check in date'), (b'P', b'Partially Completed'), (b'F', b'Fully Completed')]),
        ),
        migrations.AlterField(
            model_name='assessmentsheet',
            name='chapter7',
            field=models.CharField(default=b'N', help_text=b'Helpful hint', max_length=1, verbose_name=b'Chapter 7 - MTV - 26th Jan', choices=[(b'N', b'Not Completed'), (b'A', b'Attempted'), (b'C', b'Completed but after check in date'), (b'P', b'Partially Completed'), (b'F', b'Fully Completed')]),
        ),
        migrations.AlterField(
            model_name='assessmentsheet',
            name='firstname',
            field=models.CharField(max_length=64, verbose_name=b'Please enter your first name'),
        ),
        migrations.AlterField(
            model_name='assessmentsheet',
            name='lab',
            field=models.IntegerField(default=0, verbose_name=b'Please select the lab you are in', choices=[(1, b'Lab 1 - Mon 1-3'), (2, b'Lab 2 - Mon 3-5'), (3, b'Lab 3 - Tues 1-3'), (4, b'Lab 4 - Tues 3-5'), (5, b'Lab 5 - Wed 2-4'), (6, b'Lab 6 - Wed 4-6'), (7, b'Lab 7 - Thurs 1-3'), (8, b'Lab 8 - Thurs 1-3'), (9, b'Lab 9 - Fri 3-5'), (10, b'Lab 10 - Wed 4-6'), (11, b'Lab 11 - Wed 2-4')]),
        ),
        migrations.AlterField(
            model_name='assessmentsheet',
            name='lastname',
            field=models.CharField(max_length=64, verbose_name=b'Please enter your last name'),
        ),
        migrations.AlterField(
            model_name='assessmentsheet',
            name='studentno',
            field=models.CharField(unique=True, max_length=8, verbose_name=b'Please enter your student no (without the letter)'),
        ),
    ]
