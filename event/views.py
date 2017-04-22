from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Event , Person

# Create your views here.
def home(request):
    event_list = Event.objects.order_by('event_name')
    person_count = Person.objects.all()
    context = {'event_list': event_list}
    context2 = {'person': person_count}
    return render(request, 'home.html', context, context2)


def new_event(request):
    if request.method == 'POST':
        Event.objects.create(event_name=request.POST['name'], event_detail=request.POST['detail'],
            event_numset=request.POST['numset'], event_location=request.POST['location'])
        return HttpResponseRedirect(reverse('event:home',))

    event = Event.objects.all()
    return render(request, 'create_event.html', {'event': event})