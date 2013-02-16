
from django.contrib import admin
from django.forms import ModelForm, ValidationError
from django.core.files.images import get_image_dimensions

from models import CarouselItem, NewsFeedItem, ProjectItem
from models import TeamMember, PageBackground

def inResolutionRange(range, image):
	width, height = get_image_dimensions(image)
	assert range['width'][0] <= range['width'][1], 'Badly formated arguments.'
	assert range['height'][0] <= range['height'][1], 'Badly formated arguments.'
	if not range['width'][0] <= width <= range['width'][1] or \
		not range['height'][0] <= height <= range['height'][1]:
		return False
	return True

def assertInResolution(fieldname, wrange, hrange):
	"""
	Generic decorator for methods that assert the passing of images in
	the right resolution ranges.
	Arguments:
		- wrange speficies the range in which the image's width may be.
		- hrange speficies the range in which the image's height may be.
		When a single integer is passed, the image must match exactly that dimension.
	"""

	# format wrange like (x, y)
	try: iter(wrange)
	except: wrange = (wrange, wrange)

	# format hrange like (x, y)
	try: iter(hrange)
	except: hrange = (hrange, hrange)

	def method (self):
		image = self.cleaned_data.get(fieldname)
		if not image:
			return image
		width, height = get_image_dimensions(image)
		if not inResolutionRange({
			'width': wrange,
			'height': hrange
			}, image):
			raise ValidationError('Wrong resolution: %sx%s image \
				should have width (minimum, maximum) %s\
				and height (min, max) %s' % (width, height, wrange, hrange))
		return image
	return method

def snippetGetter(attr, csize):
	""" Return a function that returns <csize> characters from self.<attr>. """
	def func(self):
		return getattr(self, attr)[:csize]
	func.__name__ = attr
	return func

def thumbnailDisplayer(attr, height=100):
	def func(self):
		return "<img height='%s' src='%s' />" % (height, getattr(self, attr).url)
	func.short_description = attr
	func.allow_tags = True
	return func

def sizeGetter(attr):
	def func(self):
		return '%.2f KB' % (float(getattr(self, attr).file.size)/1024)
	func.short_description = '%s size' % attr
	return func

###############################################################################
###############################################################################
# The main page's Carousel items are edited on the control panel.
def make_published(modelAdmin, request, queryset):
	queryset.update(is_published=True)
make_published.short_description = 'Make carousel items visible to the viewer'

def make_unpublished(modelAdmin, request, queryset):
	queryset.update(is_published=False)
make_unpublished.short_description = 'Hide these carousel items from the viewer'

class CarouselItemForm(ModelForm):
	class Meta:
		model = CarouselItem
	clean_image = assertInResolution('image', 960, 360)
	
class CarouselItemAdmin(admin.ModelAdmin):
	form = CarouselItemForm
	fieldsets = (
		(None, {
			'fields': ('title', 'is_published', 'description', 'image', 'link')
		}),
	)
	list_display = (thumbnailDisplayer('image'), 'title', snippetGetter('description', 40), 'link', 'date_added', 'is_published', )
	search_fields = ('title', 'date', 'description')
	ordering = ('-date_added',)
	can_delete = True
	actions = (make_published, make_unpublished) # Publish/unpublish multiple items at once.

###############################################################################
###############################################################################
# The main page's news items are edited on the control panel.

class NewsFeedItemForm(ModelForm):
	class Meta:
		model = NewsFeedItem
	clean_thumbnail = assertInResolution('thumbnail', (100, 300), (100, 300))

class NewsFeedItemAdmin(admin.ModelAdmin):
	form = NewsFeedItemForm
	fieldsets = (
		(None, {
			'fields': ('title', 'date', 'description', 'thumbnail', 'link'),
			'description': 'Create a news item to be displayed on the main page.'
		}),
	)
	list_display = ('title', 'date', snippetGetter('description', 40), 'link', thumbnailDisplayer('thumbnail'))
	search_fields = ('title', 'date', 'description')

###############################################################################
###############################################################################
class ProjectItemForm(ModelForm):
	class Meta:
		model = ProjectItem
	clean_thumbnail = assertInResolution('thumbnail', 175, 100)
	clean_banner = assertInResolution('banner', (0, 100000), (0, 100000))

class ProjectItemAdmin(admin.ModelAdmin):
	form = ProjectItemForm
	fieldsets = (
		(None, {
			'fields': ('name', 'small_desc', 'birth_date', 'description', 'thumbnail', 'banner', 'link',),
			'description': ()
		}),
	)
	ordering = ('-birth_date', )
	list_display = ('name', 'small_desc', 'link', 'birth_date', thumbnailDisplayer('banner'))
	search_fields = ('name', 'date', 'description', 'birth_date')

###############################################################################
###############################################################################

class TeamMemberForm(ModelForm):
	class Meta:
		model = TeamMember
	clean_avatar = assertInResolution('avatar', 140, 185)
	def clean_name(self):
		name = self.cleaned_data.get('name')
		if len(name.split(' ')) > 2:
			raise ValidationError('Please insert only two words for each member\'s name.')
		return name

class TeamMemberAdmin(admin.ModelAdmin):
	form = TeamMemberForm
	list_display = ('name', 'job', 'age', 'member_since', snippetGetter('bio', 40), thumbnailDisplayer('avatar'))
	search_fields = ('name', 'member_since', 'job', 'age', 'bio')
	ordering = ('member_since', )

###############################################################################
###############################################################################

class PageBackgroundForm(ModelForm):
	class Meta:
		mode = PageBackground
	clean_file = assertInResolution('file', (1000, 2000), (700, 1500))

class PageBackgroundAdmin(admin.ModelAdmin):
	form = PageBackgroundForm
	list_display = ('file', 'header_color', 'date_added', sizeGetter('file'), thumbnailDisplayer('file'))
	ordering = ('-date_added',)

admin.site.register(CarouselItem, CarouselItemAdmin)
admin.site.register(NewsFeedItem, NewsFeedItemAdmin)
admin.site.register(ProjectItem, ProjectItemAdmin)
admin.site.register(TeamMember, TeamMemberAdmin)
admin.site.register(PageBackground, PageBackgroundAdmin)