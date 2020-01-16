from django.test import TestCase
from django.utils import timezone
import pytz

from freezegun import freeze_time
from rest_app.serializers import FancyCatListSerilizer, FancyCatSerilizer
from rest_app.models import FancyCat


class FancyCatListSerilizerTest(TestCase):

    def setUp(self):
        self.cat = FancyCat.objects.create(
            name='Oscar', age=2, is_active=False, description='Active cat'
        )

    def test_serializer(self):
        serializer = FancyCatListSerilizer(self.cat)

        self.assertEqual(serializer.data, {'id': 1, 'name': 'Oscar'})

class FancyCatSerilizerTest(TestCase):

    @freeze_time()
    def setUp(self):
        timezone.activate(pytz.timezone('UTC'))
        self.cat = FancyCat.objects.create(
            name='Alex', age=2, is_active=False, description='Fluffy cat'
        )
        self.now = timezone.now().strftime('%Y-%m-%dT%H:%M:%S.%fZ')
    
    def test_serializer(self):
        serializer = FancyCatSerilizer(self.cat)
        
        self.assertEqual(serializer.data, {
            'name': 'Alex', 'age': 2, 'is_active': False, 
            'description': 'Fluffy cat',
            'date_added': self.now
        })


