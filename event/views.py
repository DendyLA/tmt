from django.shortcuts import render, get_object_or_404
from .models import Event, EventAbout, EventDirection, EventPackb2b, EventPackb2g, Programme, Catalog


def eventDetail(request, slug):

	event = get_object_or_404(Event, slug=slug)
	about = EventAbout.objects.last()
	direction = EventDirection.objects.all()
	b2b = EventPackb2b.objects.all()
	b2g = EventPackb2g.objects.all()

	context = {
		'event' : event,
		'about' : about,
		'direction' : direction,
		'b2b' : b2b,
		'b2g' : b2g
	}


	return render( request, 'event/event_detail.html', context)


def program(request):
	programme = Programme.objects.last()

	context = {
		"programme_en": programme.get_translation("en"),
		"programme_ru": programme.get_translation("ru"),
		"programme_tk": programme.get_translation("tk"),
	}

	


	return render(request, 'event/program.html', context)



def catalog(request):
	catalog = Catalog.objects.last()

	context = {
		'file' : catalog,
	}

	return render(request, 'event/catalog.html', context)