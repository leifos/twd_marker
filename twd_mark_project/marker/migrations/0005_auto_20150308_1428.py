# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('marker', '0004_auto_20150308_1425'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assessmentsheet',
            name='notes',
            field=models.CharField(default=b'', max_length=384, verbose_name=b'Please enter any exceptional circumstances that should be considered when marking your project (incidents need to be recorded in MyCampus for us to verify your claims).'),
        ),
    ]
