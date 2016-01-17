# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 17, 7, 50, 27, 88224, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
