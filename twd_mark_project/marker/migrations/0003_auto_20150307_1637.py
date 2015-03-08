# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('marker', '0002_auto_20150307_1543'),
    ]

    operations = [
        migrations.AddField(
            model_name='assessmentsheet',
            name='chapter4',
            field=models.CharField(default=b'N', help_text=b'Helpful hint', max_length=1, verbose_name=b'Chapter 4', choices=[(b'N', b'Not Completed'), (b'A', b'Attempted'), (b'C', b'Completed but after check in date'), (b'P', b'Partially Completed'), (b'F', b'Fully Completed')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='assessmentsheet',
            name='chapter5',
            field=models.CharField(default=b'N', help_text=b'Helpful hint', max_length=1, verbose_name=b'Chapter 4', choices=[(b'N', b'Not Completed'), (b'A', b'Attempted'), (b'C', b'Completed but after check in date'), (b'P', b'Partially Completed'), (b'F', b'Fully Completed')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='assessmentsheet',
            name='chapter6',
            field=models.CharField(default=b'N', help_text=b'Helpful hint', max_length=1, verbose_name=b'Chapter 4', choices=[(b'N', b'Not Completed'), (b'A', b'Attempted'), (b'C', b'Completed but after check in date'), (b'P', b'Partially Completed'), (b'F', b'Fully Completed')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='assessmentsheet',
            name='chapter7',
            field=models.CharField(default=b'N', help_text=b'Helpful hint', max_length=1, verbose_name=b'Chapter 4', choices=[(b'N', b'Not Completed'), (b'A', b'Attempted'), (b'C', b'Completed but after check in date'), (b'P', b'Partially Completed'), (b'F', b'Fully Completed')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='assessmentsheet',
            name='chapter3',
            field=models.CharField(default=b'N', help_text=b'Helpful hint', max_length=1, verbose_name=b'Chapter 3', choices=[(b'N', b'Not Completed'), (b'A', b'Attempted'), (b'C', b'Completed but after check in date'), (b'P', b'Partially Completed'), (b'F', b'Fully Completed')]),
        ),
    ]
