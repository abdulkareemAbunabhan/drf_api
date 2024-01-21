from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Bucket


# Create your tests here.

class ThingTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(username='testuser1', password='pass')
        testuser1.save()

        test_bucket = Bucket.objects.create(name='ben', owner=testuser1, quantity="3")
        test_bucket.save()

    def thigs_model(self):
        bucket = Bucket.objects.get(id=1)
        actual_owner= str(bucket.owner)
        actual_name = str(bucket.name)
        actual_quantity = str(bucket.quantity)
        self.assertEqual(actual_owner,"testuser1")
        self.assertEqual(actual_name,"ben")
        self.assertEqual(actual_quantity,"3.")
