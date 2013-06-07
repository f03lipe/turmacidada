
from django import template

register = template.Library()

# KEEP AWAY!
# JUNKY CODE AHEAD!
# I MEAN IT!

@register.assignment_tag(takes_context=True)
def loadModelObjects(context, format_string):
	# Special tag to load model elements to the template.
	# Not quite "djangonic", but who cares?
	import turmacidada.website.models as models
	model = getattr(models, format_string) # DANGER, DANGER!
	return model.objects

@register.filter(name='order_by')
def order_by(obj, arg):
	# Order a manager (<model>.objects) object present in the template as <arg> dictates.
	return obj.order_by(arg)

@register.filter(name='filter')
def filter(obj, arg):
	# Filters objects from a manager object in the template.
	return obj.filter(**eval('dict(%s)' % arg))

@register.assignment_tag(takes_context=True)
def getBackgroundImage(context):
	# print dict(context['request'].session)
	import turmacidada.website.models as models
	# context['request'].session['idBgImg'] = 232
	try:
		return None
		idBg = context['request'].session.get('idBgImg')
		try:
			assert idBg
			return models.PageBackground.objects.get(id=idBg)
		except:
			bg = models.PageBackground.objects.filter(is_active=True).order_by('?')[0]
			context['request'].session['idBgImg'] = bg.id
			return bg
	except IndexError: # No background pages
		return None
