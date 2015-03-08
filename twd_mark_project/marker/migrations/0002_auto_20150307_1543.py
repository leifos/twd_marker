# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('marker', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='assessmentsheet',
            name='chapter3',
            field=models.CharField(default=b'N', max_length=1, choices=[(b'N', b'Not Completed'), (b'P', b'Partially Completed'), (b'F', b'Fully Completed')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='assessmentsheet',
            name='lab',
            field=models.IntegerField(default=0, choices=[(1, b'Lab 1 - Mon 1-3'), (2, b'Lab 2 - Mon 3-5'), (3, b'Lab 3 - Tues 1-3'), (4, b'Lab 4 - Tues 3-5'), (5, b'Lab 5 - Wed 2-4'), (6, b'Lab 6 - Wed 4-6'), (7, b'Lab 7 - Thurs 1-3'), (8, b'Lab 8 - Thurs 1-3'), (9, b'Lab 9 - Fri 3-5'), (10, b'Lab 10 - Wed 4-6'), (11, b'Lab 11 - Wed 2-4')]),
            preserve_default=True,
        ),
        migrations.RemoveField(
            model_name='assessmentsheet',
            name='chapter1',
        ),
    ]
