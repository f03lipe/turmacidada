# -*- coding: utf8 -*-

# IMPLEMENT:
#- search
#- cc? reg?

#- ex-alunos?
#- cache
#- permissions
#- email

# CONTENT:
#- languages?
#- filiais
#- imprensa (documentos)
#- clouds limit (animation, interact?)

from django.db import models
from django import forms
# from django.utils.translation import ugettext_lazy as _
# from cms.models import CMSPlugin
from cms.apphook_pool import apphook_pool

import os
from time import strftime
import datetime

def fileNameGenerator(fnbegin):
	return lambda instance, filename: fnbegin+filename

from cms_search.cms_app import HaystackSearchApphook
apphook_pool.register(HaystackSearchApphook)

### CAROUSEL ITEM
class CarouselItem(models.Model):
	
	# name = models.CharField(max_length=50, unique=False, help_text='Identify this carousel item.')
	title = models.CharField(max_length=80, blank=True, help_text='OPTIONAL! Insert the title to appear on the carousel. Watch out for the final format on the home page. 80 characters max.')
	description = models.TextField(max_length=500, blank=True, help_text='OPTIONAL! Text to apper on the carousel. 500 characters maximum.')
	link = models.URLField(blank=True, help_text='The link the user is to be sent to. This is usually a blog post or a projects\'s webpage.')
	image = models.ImageField(upload_to=fileNameGenerator('carousel/img_'), help_text='Insert a 960x360px banner to appear on the carousel.')
	is_published = models.BooleanField(default=True, help_text='Uncheck this to hide this carousel item.')
	date_added = models.DateTimeField(auto_now=True)

	# date_modified = models.DateField(auto_now=True)
	# Add times clicked? (or leave it to _GA?)

	def __unicode__(self):
		return '%s (id: %d)' % (self.title, self.id)


### NEWS FEED
class NewsFeedItem(models.Model):

	title = models.CharField(max_length=50)
	description = models.TextField(max_length=350, help_text='Maximum of 320 characters. Keep it simple.')
	thumbnail = models.ImageField(upload_to=fileNameGenerator('newsfeed/thumbnail_'), null=True, blank=True, help_text='May be left blank. Recommended resolution: 100x100.')
	date = models.DateField(help_text='The date the item was posted on.')
	link = models.URLField(help_text='The url to the news item.')

	def __unicode__(self):
		return 'news_item \'%s\' on %s (id:%s)' % (self.title, self.date, self.id)


### PROJECTS THUMBNAILS LIST
class ProjectItem(models.Model):

	name = models.CharField(max_length=50)
	small_desc = models.CharField(max_length=100, help_text='Write a small (max 100 chars) description of the project, for fast reading.')
	description = models.TextField(max_length=400, help_text='The project description for the reader. Maximum of 400 characters.')
	banner = models.ImageField(upload_to=fileNameGenerator('projects/banner_'), help_text='640x300px')
	thumbnail = models.ImageField(upload_to=fileNameGenerator('projects/thumbnail_'), help_text='175x100px.')
	link = models.URLField(help_text='The project\'s home url.')
	birth_date = models.DateField()
	
	def __unicode__(self):
		return 'project \'%s\' (id: %s)' % (self.name, self.id)

### TEAM
class TeamMember(models.Model):

	name = models.CharField(max_length=50, help_text='Use a two-word name.')
	avatar = models.ImageField(upload_to=fileNameGenerator('team/avatar_'), help_text='Upload the person\'s 140x185px avatar to appear on the website.')
	birth = models.DateField(default=datetime.date(2007, 1, 1), help_text='This person\'s date of birth.')
	job = models.CharField(max_length=30, help_text='The member\'s duty inside the organization. Be brief: 30 characters max.')
	member_since = models.DateField(default=datetime.date(2007, 1, 1), help_text='When did this person joined the team?')
	bio = models.TextField(max_length=240, blank=True, help_text='Place to insert a small bio of each member. 240 characters max.')

	# filial (key)
	# ... ?

	def __unicode__(self):
		return 'TeamMember %s (id: %s)' % (self.name, self.id)


### Background's
class PageBackground(models.Model):

	file = models.ImageField(upload_to=fileNameGenerator('backgrounds/'))
	date_added = models.DateField(auto_now_add=True)
	is_active = models.BooleanField(default=True, help_text="The wallpaper will show up.")
	header_color = models.CharField(max_length=20,
		choices=(
			('dark', 'dark body (for light backgrounds)'),
			('light', 'light body (for dark backgrounds)'),
		), default=('dark'))

	def __unicode__(self):
		return 'Background %s (id: %s)' % (self.file, self.id)