from django.contrib import admin

# Register your models here.
from tone.models import Tone

class ToneModelAdmin(admin.ModelAdmin):
	lsit_display = ["__unicode__","content","id"]
	class Meta:
		model = Tone
admin.site.register(Tone, ToneModelAdmin)