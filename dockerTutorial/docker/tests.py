from django.test import TestCase
from .models import Book, Author
# Create your tests here.


class Dockertest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.author = Author.objects.create(
            name="Ledum", title="Mr", sex="M"
        )

        cls.book1 = Book.objects.create(
            name="Game of Thrones",
            number=23,
            author=cls.author
        )

        cls.book2 = Book.objects.create(
            name="The One",
            number=32,
            author=cls.author
        )

    def test_book_name_matches(self):
        self.assertEqual(self.book1.name, "Game of Thrones")

    def test_failing_method(self):
        self.assertEqual(self.book2.number, 32)
