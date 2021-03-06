# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-12-13 14:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True)),
                ('name', models.CharField(blank=True, max_length=255)),
                ('slug', models.SlugField(blank=True, help_text='Updates itself on name change.')),
                ('org', models.TextField(blank=True, verbose_name='Organization')),
            ],
            managers=[
                ('objects', django.db.models.manager.Manager()),
                ('_plain_manager', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='TestimonialTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=250)),
                ('quote', models.TextField()),
                ('language_code', models.CharField(db_index=True, max_length=15)),
                ('master', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='django_translatable_testimonials.Testimonial')),
            ],
            options={
                'managed': True,
                'abstract': False,
                'db_table': 'django_translatable_testimonials_testimonial_translation',
                'db_tablespace': '',
                'default_permissions': (),
            },
        ),
        migrations.AlterUniqueTogether(
            name='testimonialtranslation',
            unique_together=set([('language_code', 'master')]),
        ),
    ]
