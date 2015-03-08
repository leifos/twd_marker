# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('marker', '0005_auto_20150308_1428'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assessmentsheet',
            name='chapter10',
            field=models.CharField(default=b'N', help_text=b'', max_length=1, verbose_name=b'Chapter 10 - More Templates - 9th Feb', choices=[(b'N', b'Not Completed'), (b'A', b'Attempted'), (b'C', b'Completed but after check in date'), (b'P', b'Partially Completed'), (b'F', b'Fully Completed')]),
        ),
        migrations.AlterField(
            model_name='assessmentsheet',
            name='chapter11',
            field=models.CharField(default=b'N', help_text=b'', max_length=1, verbose_name=b'Chapter 11 - Cookies - 28th Feb', choices=[(b'N', b'Not Completed'), (b'A', b'Attempted'), (b'C', b'Completed but after check in date'), (b'P', b'Partially Completed'), (b'F', b'Fully Completed')]),
        ),
        migrations.AlterField(
            model_name='assessmentsheet',
            name='chapter12',
            field=models.CharField(default=b'N', help_text=b'', max_length=1, verbose_name=b'Chapter 12 - More User Auth - 28th Feb', choices=[(b'N', b'Not Completed'), (b'A', b'Attempted'), (b'C', b'Completed but after check in date'), (b'P', b'Partially Completed'), (b'F', b'Fully Completed')]),
        ),
        migrations.AlterField(
            model_name='assessmentsheet',
            name='chapter13',
            field=models.CharField(default=b'N', help_text=b'', max_length=1, verbose_name=b'Chapter 13 - Bootstrap - 28th Feb', choices=[(b'N', b'Not Completed'), (b'A', b'Attempted'), (b'C', b'Completed but after check in date'), (b'P', b'Partially Completed'), (b'F', b'Fully Completed')]),
        ),
        migrations.AlterField(
            model_name='assessmentsheet',
            name='chapter14',
            field=models.CharField(default=b'N', help_text=b'', max_length=1, verbose_name=b'Chapter 14 - Template Tags - 9th Mar', choices=[(b'N', b'Not Completed'), (b'A', b'Attempted'), (b'C', b'Completed but after check in date'), (b'P', b'Partially Completed'), (b'F', b'Fully Completed')]),
        ),
        migrations.AlterField(
            model_name='assessmentsheet',
            name='chapter15',
            field=models.CharField(default=b'N', help_text=b'', max_length=1, verbose_name=b'Chapter 15 - Bing Search - 9th Mar', choices=[(b'N', b'Not Completed'), (b'A', b'Attempted'), (b'C', b'Completed but after check in date'), (b'P', b'Partially Completed'), (b'F', b'Fully Completed')]),
        ),
        migrations.AlterField(
            model_name='assessmentsheet',
            name='chapter16',
            field=models.CharField(default=b'N', help_text=b'', max_length=1, verbose_name=b'Chapter 16-17 - Exercises - 9th Mar', choices=[(b'N', b'Not Completed'), (b'A', b'Attempted'), (b'C', b'Completed but after check in date'), (b'P', b'Partially Completed'), (b'F', b'Fully Completed')]),
        ),
        migrations.AlterField(
            model_name='assessmentsheet',
            name='chapter21',
            field=models.CharField(default=b'N', help_text=b'', max_length=1, verbose_name=b'Chapter 21 - Deployed - 9th Mar', choices=[(b'N', b'Not Completed'), (b'A', b'Attempted'), (b'C', b'Completed but after check in date'), (b'P', b'Partially Completed'), (b'F', b'Fully Completed')]),
        ),
        migrations.AlterField(
            model_name='assessmentsheet',
            name='chapter3',
            field=models.CharField(default=b'N', help_text=b'', max_length=1, verbose_name=b'Chapter 3 - Setting Up - 26th Jan', choices=[(b'N', b'Not Completed'), (b'A', b'Attempted'), (b'C', b'Completed but after check in date'), (b'P', b'Partially Completed'), (b'F', b'Fully Completed')]),
        ),
        migrations.AlterField(
            model_name='assessmentsheet',
            name='chapter4',
            field=models.CharField(default=b'N', help_text=b'', max_length=1, verbose_name=b'Chapter 4 - Django Basics - 26th Jan', choices=[(b'N', b'Not Completed'), (b'A', b'Attempted'), (b'C', b'Completed but after check in date'), (b'P', b'Partially Completed'), (b'F', b'Fully Completed')]),
        ),
        migrations.AlterField(
            model_name='assessmentsheet',
            name='chapter5',
            field=models.CharField(default=b'N', help_text=b'', max_length=1, verbose_name=b'Chapter 5 - Templates - 26th Jan', choices=[(b'N', b'Not Completed'), (b'A', b'Attempted'), (b'C', b'Completed but after check in date'), (b'P', b'Partially Completed'), (b'F', b'Fully Completed')]),
        ),
        migrations.AlterField(
            model_name='assessmentsheet',
            name='chapter6',
            field=models.CharField(default=b'N', help_text=b'', max_length=1, verbose_name=b'Chapter 6 - Models - 26th Jan', choices=[(b'N', b'Not Completed'), (b'A', b'Attempted'), (b'C', b'Completed but after check in date'), (b'P', b'Partially Completed'), (b'F', b'Fully Completed')]),
        ),
        migrations.AlterField(
            model_name='assessmentsheet',
            name='chapter7',
            field=models.CharField(default=b'N', help_text=b'', max_length=1, verbose_name=b'Chapter 7 - MTV - 26th Jan', choices=[(b'N', b'Not Completed'), (b'A', b'Attempted'), (b'C', b'Completed but after check in date'), (b'P', b'Partially Completed'), (b'F', b'Fully Completed')]),
        ),
        migrations.AlterField(
            model_name='assessmentsheet',
            name='chapter8',
            field=models.CharField(default=b'N', help_text=b'', max_length=1, verbose_name=b'Chapter 8 - Forms - 9th Feb', choices=[(b'N', b'Not Completed'), (b'A', b'Attempted'), (b'C', b'Completed but after check in date'), (b'P', b'Partially Completed'), (b'F', b'Fully Completed')]),
        ),
        migrations.AlterField(
            model_name='assessmentsheet',
            name='chapter9',
            field=models.CharField(default=b'N', help_text=b'', max_length=1, verbose_name=b'Chapter 9 - User Auth - 9th Feb', choices=[(b'N', b'Not Completed'), (b'A', b'Attempted'), (b'C', b'Completed but after check in date'), (b'P', b'Partially Completed'), (b'F', b'Fully Completed')]),
        ),
        migrations.AlterField(
            model_name='assessmentsheet',
            name='notes',
            field=models.CharField(default=b'', max_length=384, verbose_name=b'Please enter any exceptional circumstances that should be considered when marking your project (incidents need to be recorded in MyCampus for us to verify your claims).', blank=True),
        ),
    ]
