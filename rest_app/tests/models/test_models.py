from django.test import TestCase

from rest_app.models import FancyCat

class FancyCatTest(TestCase):

    def setUp(self):
        FancyCat.objects.create(name='Alex')
        FancyCat.objects.create(name='Oscar')

    def test_count_cats(self):
        self.assertEqual(FancyCat.objects.count(), 2)

    def test_create(self):
        c = FancyCat.objects.create(name='Sam')

        self.assertEqual(FancyCat.objects.count(), 3)
        self.assertEqual(c.name, 'Sam')
        self.assertEqual(c.id, 3)

    def test_edit_case(self):
        c = FancyCat.objects.create(name='Alex')

        c.name = 'Bob'
        c.age = 3
        c.save()
        
        c.refresh_from_db()
        self.assertEqual(c.name, 'Bob')
        self.assertEqual(c.age, 3)

    def test_delete_case(self):
        c = FancyCat.objects.get(id=1)
        c.delete()

        self.assertEqual(FancyCat.objects.count(), 1)
    
    def test_get_cat_method(self):
        c = FancyCat.objects.create(name='Alex', age=0)

        self.assertEqual(c.get_cat(), 'Alex - 0')
