from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, HttpRequest
# Create your views here.
from .models import Tone
from .forms import ToneForm
from .temp import analyze_my_tone

def tone_in(request):
	form = ToneForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		return HttpResponseRedirect(instance.get_absolute_url())

	context = {
		"form":form
	}
	return render(request, "index2.html", context)



def tone_update(request):
	form = ToneForm(request.POST or None)
	
	instance = Tone.objects.order_by("-id").first()
	if instance != None:
		result = analyze_my_tone(instance.content)
	else:
		result = []
	context = {
		"form" : form,
		"ins" : instance,
		"res" : result
		
	}
	
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		return HttpResponseRedirect(instance.get_absolute_url())

	return render(request, "index.html", context)

