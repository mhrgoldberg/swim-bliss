from django.test import TestCase

# Create your tests here.

class LocationTestCase(TestCase):
    def test_location_creation(self):
        location = Location.objects.create(name="Test Location", description="Test Description", coordinates="POINT(1 1)")
        self.assertEqual(location.name, "Test Location")
        self.assertEqual(location.description, "Test Description")
        self.assertEqual(location.coordinates, "POINT(1 1)")
