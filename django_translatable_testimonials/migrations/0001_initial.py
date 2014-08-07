# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'TestimonialTranslation'
        db.create_table(u'django_translatable_testimonials_testimonial_translation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=250, blank=True)),
            ('quote', self.gf('django.db.models.fields.TextField')()),
            ('language_code', self.gf('django.db.models.fields.CharField')(max_length=15, db_index=True)),
            ('master', self.gf('django.db.models.fields.related.ForeignKey')(related_name='translations', null=True, to=orm['django_translatable_testimonials.Testimonial'])),
        ))
        db.send_create_signal('django_translatable_testimonials', ['TestimonialTranslation'])

        # Adding unique constraint on 'TestimonialTranslation', fields ['language_code', 'master']
        db.create_unique(u'django_translatable_testimonials_testimonial_translation', ['language_code', 'master_id'])

        # Adding model 'Testimonial'
        db.create_table(u'django_translatable_testimonials_testimonial', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50, blank=True)),
            ('org', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('django_translatable_testimonials', ['Testimonial'])


    def backwards(self, orm):
        # Removing unique constraint on 'TestimonialTranslation', fields ['language_code', 'master']
        db.delete_unique(u'django_translatable_testimonials_testimonial_translation', ['language_code', 'master_id'])

        # Deleting model 'TestimonialTranslation'
        db.delete_table(u'django_translatable_testimonials_testimonial_translation')

        # Deleting model 'Testimonial'
        db.delete_table(u'django_translatable_testimonials_testimonial')


    models = {
        'django_translatable_testimonials.testimonial': {
            'Meta': {'object_name': 'Testimonial'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'org': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'blank': 'True'})
        },
        'django_translatable_testimonials.testimonialtranslation': {
            'Meta': {'unique_together': "[('language_code', 'master')]", 'object_name': 'TestimonialTranslation', 'db_table': "u'django_translatable_testimonials_testimonial_translation'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language_code': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'master': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'translations'", 'null': 'True', 'to': "orm['django_translatable_testimonials.Testimonial']"}),
            'quote': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'})
        }
    }

    complete_apps = ['django_translatable_testimonials']