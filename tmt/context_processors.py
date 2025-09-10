from event.models import Event  

def event_url(request):
    try:
        # Берём "главное событие", или по своей логике
        event = Event.objects.first()
        if event:
            return {"event_url": event.get_absolute_url()}
    except Event.DoesNotExist:
        pass
    return {}