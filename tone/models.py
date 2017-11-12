from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse
# Create your models here.

class Tone(models.Model):
	content = models.TextField()

	def __unicode__(self):
		return self.content
	def __str__(self):
		return self.content

	def get_absolute_url(self):
		return reverse("update")

	def get_absolute_url1(self):
		return reverse("home")

