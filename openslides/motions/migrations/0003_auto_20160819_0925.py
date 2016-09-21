# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-19 09:25
from __future__ import unicode_literals

import jsonfield.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('motions', '0002_motion_origin'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='motion',
            options={
                'default_permissions': (),
                'ordering': ('identifier',),
                'permissions': (
                    ('can_see', 'Can see motions'),
                    ('can_create', 'Can create motions'),
                    ('can_support', 'Can support motions'),
                    ('can_see_and_manage_comments', 'Can see and manage comments'),
                    ('can_manage', 'Can manage motions')),
                'verbose_name': 'Motion'},
        ),
        migrations.AddField(
            model_name='motion',
            name='comments',
            field=jsonfield.fields.JSONField(null=True),
        ),
    ]