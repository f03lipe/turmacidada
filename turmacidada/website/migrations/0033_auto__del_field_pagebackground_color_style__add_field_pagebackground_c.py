# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'PageBackground.color_style'
        db.delete_column('website_pagebackground', 'color_style')

        # Adding field 'PageBackground.color'
        db.add_column('website_pagebackground', 'color',
                      self.gf('django.db.models.fields.CharField')(default='dark', max_length=20),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'PageBackground.color_style'
        db.add_column('website_pagebackground', 'color_style',
                      self.gf('django.db.models.fields.CharField')(default='dark', max_length=20),
                      keep_default=False)

        # Deleting field 'PageBackground.color'
        db.delete_column('website_pagebackground', 'color')


    models = {
        'website.carouselitem': {
            'Meta': {'object_name': 'CarouselItem'},
            'date_added': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'max_length': '500', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'is_published': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '80', 'blank': 'True'})
        },
        'website.newsfeeditem': {
            'Meta': {'object_name': 'NewsFeedItem'},
            'date': ('django.db.models.fields.DateField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {'max_length': '350'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'thumbnail': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'website.pagebackground': {
            'Meta': {'object_name': 'PageBackground'},
            'color': ('django.db.models.fields.CharField', [], {'default': "'dark'", 'max_length': '20'}),
            'date_added': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'file': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'website.projectitem': {
            'Meta': {'object_name': 'ProjectItem'},
            'banner': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'birth_date': ('django.db.models.fields.DateField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {'max_length': '400'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'small_desc': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'thumbnail': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'})
        },
        'website.teammember': {
            'Meta': {'object_name': 'TeamMember'},
            'age': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'avatar': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'bio': ('django.db.models.fields.TextField', [], {'max_length': '240'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'job': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'member_since': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2007, 1, 1, 0, 0)'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['website']