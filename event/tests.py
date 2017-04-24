from django.test import TestCase
from event.models import Event, Person


class HomePageTest(TestCase):

    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    def test_displays_event_name(self):
        Event.objects.create(event_name='Event 1', event_detail='Detail 1',
            event_numset=2, event_location='Location 1', pcount=0,)

        response = self.client.get('/')

        self.assertIn('Event 1', response.content.decode())

    def test_only_saves_items_when_necessary(self):
        self.client.get('/')
        self.assertEqual(Event.objects.count(), 0)


class CreateEventPageTest(TestCase):

    def test_uses_template(self):
        response = self.client.get('/new_event')
        self.assertTemplateUsed(response, 'create_event.html')

    def test_can_save_a_POST_request(self):
        self.client.post('/new_event', data={'name': 'event name' , 'detail': 'event detail', 'location': 'event location', 'number': 10})

        self.assertEqual(Item.objects.count(), 1)
        new_event = Event.objects.first()
        self.assertEqual(new_event.event_name, 'event name')
        self.assertEqual(new_event.event_detail, 'event detail')
        self.assertEqual(new_event.event_numset, '10')
        self.assertEqual(new_event.event_location, 'event location')
        self.assertEqual(new_event.pcount, '0')
        


class DetailEventPageTest(TestCase):

    def test_uses_template(self):
        Event.objects.create(event_name='Event 1', event_detail='Detail 1',
            event_numset=2, event_location='Location 1', pcount=0,)

        response = self.client.get('/1/')
        self.assertTemplateUsed(response, 'detail.html')



class EventModelTest(TestCase):

    def test_saving_and_retrieving_event(self):

        event = Event.objects.create(event_name='Event 1', event_detail='Detail 1',
            event_numset=2, event_location='Location 1', pcount=0,)
        
        person1 = event.person_set.create(fname='John', lname='Farmer')
        person1.save()

        person2 = event.person_set.create(fname='Gaben', lname='L')
        person2.save()

        saved_person = Person.objects.all()
        self.assertEqual(saved_person.count(), 2)

        first_person = saved_person[0]
        second_person = saved_person[1]
        self.assertEqual(first_person.fname, 'John')
        self.assertEqual(first_person.lname, 'Farmer')
        self.assertEqual(second_person.fname, 'Gaben')
        self.assertEqual(second_person.lname, 'L')