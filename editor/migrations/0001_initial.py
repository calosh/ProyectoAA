# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Codigo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(unique=True, max_length=100)),
                ('codigo', models.TextField()),
                ('tipo', models.CharField(max_length=10, choices=[(b'java', b'Java'), (b'python', b'Python'), (b'c', b'C'), (b'cpp', b'C++')])),
                ('publ_priv', models.BooleanField(default=False)),
                ('slug', models.SlugField(max_length=100)),
                ('usuario', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
