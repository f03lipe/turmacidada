# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'TreeManager'
        db.delete_table(u'website_treemanager')

        # Deleting field 'TeamMember.age'
        db.delete_column(u'website_teammember', 'age')

        # Adding field 'TeamMember.birth'
        db.add_column(u'website_teammember', 'birth',
                      self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2007, 1, 1, 0, 0)),
                      keep_default=False)


    def backwards(self, orm):
        # Adding model 'TreeManager'
        db.create_table(u'website_treemanager', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'website', ['TreeManager'])

        # Adding field 'TeamMember.age'
        db.add_column(u'website_teammember', 'age',
                      self.gf('django.db.models.fields.CharField')(default=datetime.datetime(1993, 1, 1, 0, 0), max_length=20),
                      keep_default=False)

        # Deleting field 'TeamMember.birth'
        db.delete_column(u'website_teammember', 'birth')


    models = {
        u'website.carouselitem': {
            'Meta': {'object_name': 'CarouselItem'},
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'max_length': '500', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'is_published': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '80', 'blank': 'True'})
        },
        u'website.newsfeeditem': {
            'Meta': {'object_name': 'NewsFeedItem'},
            'date': ('django.db.models.fields.DateField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {'max_length': '350'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'thumbnail': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'website.pagebackground': {
            'Meta': {'object_name': 'PageBackground'},
            'date_added': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'file': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'header_color': ('django.db.models.fields.CharField', [], {'default': "'dark'", 'max_length': '20'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        u'website.projectitem': {
            'Meta': {'object_name': 'ProjectItem'},
            'banner': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'birth_date': ('django.db.models.fields.DateField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {'max_length': '400'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'small_desc': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'thumbnail': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'})
        },
        u'website.teammember': {
            'Meta': {'object_name': 'TeamMember'},
            'avatar': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'bio': ('django.db.models.fields.TextField', [], {'max_length': '240', 'blank': 'True'}),
            'birth': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2007, 1, 1, 0, 0)'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'job': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'member_since': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2007, 1, 1, 0, 0)'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['website']