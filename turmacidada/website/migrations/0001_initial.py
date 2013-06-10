# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'CarouselItem'
        db.create_table(u'website_carouselitem', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=80, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(max_length=500, blank=True)),
            ('link', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('is_published', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('date_added', self.gf('django.db.models.fields.DateField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'website', ['CarouselItem'])

        # Adding model 'NewsFeedItem'
        db.create_table(u'website_newsfeeditem', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('description', self.gf('django.db.models.fields.TextField')(max_length=350)),
            ('thumbnail', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('link', self.gf('django.db.models.fields.URLField')(max_length=200)),
        ))
        db.send_create_signal(u'website', ['NewsFeedItem'])

        # Adding model 'ProjectItem'
        db.create_table(u'website_projectitem', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('small_desc', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.TextField')(max_length=400)),
            ('banner', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('thumbnail', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('link', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('birth_date', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal(u'website', ['ProjectItem'])

        # Adding model 'TeamMember'
        db.create_table(u'website_teammember', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('avatar', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('age', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('job', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('member_since', self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2007, 1, 1, 0, 0))),
            ('bio', self.gf('django.db.models.fields.TextField')(max_length=240)),
        ))
        db.send_create_signal(u'website', ['TeamMember'])

        # Adding model 'TreeManager'
        db.create_table(u'website_treemanager', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'website', ['TreeManager'])

        # Adding model 'PageBackground'
        db.create_table(u'website_pagebackground', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('file', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('date_added', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('header_color', self.gf('django.db.models.fields.CharField')(default='dark', max_length=20)),
        ))
        db.send_create_signal(u'website', ['PageBackground'])


    def backwards(self, orm):
        # Deleting model 'CarouselItem'
        db.delete_table(u'website_carouselitem')

        # Deleting model 'NewsFeedItem'
        db.delete_table(u'website_newsfeeditem')

        # Deleting model 'ProjectItem'
        db.delete_table(u'website_projectitem')

        # Deleting model 'TeamMember'
        db.delete_table(u'website_teammember')

        # Deleting model 'TreeManager'
        db.delete_table(u'website_treemanager')

        # Deleting model 'PageBackground'
        db.delete_table(u'website_pagebackground')


    models = {
        u'website.carouselitem': {
            'Meta': {'object_name': 'CarouselItem'},
            'date_added': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
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
            'age': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'avatar': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'bio': ('django.db.models.fields.TextField', [], {'max_length': '240'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'job': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'member_since': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2007, 1, 1, 0, 0)'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'website.treemanager': {
            'Meta': {'object_name': 'TreeManager'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['website']