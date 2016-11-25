# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='ListUser',
            fields=[
                ('password', models.CharField(verbose_name='password', max_length=128)),
                ('last_login', models.DateTimeField(null=True, blank=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(verbose_name='superuser status', default=False, help_text='Designates that this user has all permissions without explicitly assigning them.')),
                ('email', models.EmailField(serialize=False, primary_key=True, max_length=254)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', verbose_name='groups', to='auth.Group', related_name='user_set', related_query_name='user')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', verbose_name='user permissions', to='auth.Permission', related_name='user_set', related_query_name='user')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Token',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('email', models.EmailField(max_length=254)),
                ('uid', models.CharField(max_length=255)),
            ],
        ),
    ]
