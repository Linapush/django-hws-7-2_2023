from django.test import TestCase
from collection_app.models import Genres
# Books, Author --> у тебя же нету таких моделей
from collection_app.config import CF_DEFAULT
from django.db.utils import DataError


def creation_tests(cls_model, normal: dict, failing: dict):
    class Tests(TestCase):
        def test_successful_creation(self):
            cls_model.objects.create(**normal)

    return Tests


normal_name = 'a' * CF_DEFAULT
long_name = 'a' * (CF_DEFAULT + 1)

GenreTests = creation_tests(Genres, {'title': normal_name}, {'title': long_name}) # --> поле в модели называется title, а не name
# AuthorTests = creation_tests(Author, {'full_name': normal_name}, {'full_name': long_name})
# BookTests = creation_tests(Book, {'title': normal_name}, {'title': long_name})
