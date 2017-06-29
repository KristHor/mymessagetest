# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_extensions.db.fields
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ChatMessage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(verbose_name='created', blank=True, default=django.utils.timezone.now, editable=False)),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(verbose_name='modified', blank=True, default=django.utils.timezone.now, editable=False)),
                ('username', models.CharField(max_length=255, blank=True, null=True)),
                ('message', models.TextField()),
            ],
            options={
                'ordering': ('-modified', '-created'),
                'get_latest_by': 'modified',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserEvent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(verbose_name='created', blank=True, default=django.utils.timezone.now, editable=False)),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(verbose_name='modified', blank=True, default=django.utils.timezone.now, editable=False)),
                ('user_name', models.CharField(max_length=255, blank=True, null=True)),
                ('message', models.TextField()),
            ],
            options={
                'ordering': ('-modified', '-created'),
                'get_latest_by': 'modified',
                'abstract': False,
            },
        ),
    ]
