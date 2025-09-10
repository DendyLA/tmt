from django.shortcuts import render, get_object_or_404
from .models import Event, EventAbout, EventDirection, EventPackb2b, EventPackb2g


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