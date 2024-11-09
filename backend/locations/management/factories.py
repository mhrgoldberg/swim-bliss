import factory
from factory.django import DjangoModelFactory
from django.contrib.gis.geos import Point
from locations.models import Location
from faker import Faker

fake = Faker()


class LocationFactory(DjangoModelFactory):
    class Meta:
        model = Location

    name = factory.Faker('city')
    description = factory.Faker('text', max_nb_chars=200)
    # For GeoDjango Point field
    coordinates = factory.LazyFunction(
        lambda: Point(
            float(fake.longitude()),
            float(fake.latitude())
        )
    )
    # If you have other fields like:
    is_public = factory.Faker('boolean')
