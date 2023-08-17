from django.test import TestCase
from collection_app.models import Genres, Artists, Client, Tracks, Albums
from collection_app.config import CF_DEFAULT
from django.db.utils import DataError


def creation_tests(cls_model, normal: dict, failing: dict):
    class Tests(TestCase):
        def test_successful_creation(self):
            cls_model.objects.create(**normal)

        def test_failing_creation(self):
            with self.assertRaises(DataError):
                cls_model.objects.create(**failing)

    return Tests


normal_name = 'a' * CF_DEFAULT
long_name = 'a' * (CF_DEFAULT + 1)

GenresTests = creation_tests(Genres, {'name': normal_name}, {'name': long_name})
ArtistsTests = creation_tests(Artists, {'full_name': normal_name}, {'full_name': long_name})
TracksTests = creation_tests(Tracks, {'title': normal_name}, {'title': long_name})
AlbumsTests = creation_tests(Albums, {'title': normal_name}, {'title': long_name})
ClientTests = creation_tests(Client, {'title': normal_name}, {'title': long_name})


