from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Event , Person

# Create your views here.
def home(request):
    event_list = Event.objects.order_by('event_name')
    context = {'event_list': event_list}
    return render(request, 'home.html', context)


def new_event(request):
    if request.method == 'POST':
        Event.objects.create(event_name=request.POST['name'], event_detail=request.POST['detail'],
            event_numset=request.POST['numset'], event_location=request.POST['location'], pcount=0,)
        return HttpResponseRedirect(reverse('event:home',))

    event = Event.objects.all()
    return render(request, 'create_event.html', {'event': event})


def event_detail(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    if request.method == 'POST':
        event.person_set.create(fname=request.POST['firstname'], lname=request.POST['lastname'])
        event.pcount += 1
        event.save()
        return HttpResponseRedirect(reverse('event:event_detail',args=(event.id,)))
        
    return render(request, 'detail.html', {'event':event},)

def sign_name(request, event_id):
    pass
    #return HttpResponseRedirect(reverse('event_detail',kwargs={'event_id':event_id}))
        #return HttpResponseRedirect(reverse('event:event_detail',args=(event.id,)))

def delete_name(request, event_id):    #, person_id
    event = get_object_or_404(Event, pk=event_id)
    person_name = event.person_set.get(pk=request.POST['del_btn'])#request.POST['del_btn']
    person_name.delete()
    event.pcount -= 1
    event.save()
    return HttpResponseRedirect(reverse('event:event_detail',args=(event.id,)))

def delete_event(password, event_id):
    event = get_object_or_404(Event, pk=event_id)
    del_event = event.objects.all()
    del_event.delete()  