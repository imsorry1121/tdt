# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0002_news_timestamp'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='summary',
            field=models.TextField(default=datetime.datetime(2016, 1, 17, 8, 39, 12, 315611, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='news',
            name='title',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]
