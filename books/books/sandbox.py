from .models import Publisher, Book, Shop
from random import randint


def add_publishers():
    Publisher.objects.bulk_create(
        [
            Publisher(name=f'Publisher{i}')
            for i in range(1, 11)
        ]
    )


def add_books():
    publishers = Publisher.objects.all()
    books = list()

    for publisher in publishers:
        books.extend(
            [
                Book(title=f"Book{i}", publisher=publisher, price=randint(100, 1000))
                for i in range(0, 10)
            ]
        )

    Book.objects.bulk_create(books)


def add_shops():
    books = list(Book.objects.all())

    for i in range(0, 10):
        shop = Shop.objects.create(
            name=f"Shop{i}"
        )
        shop.books.set([books.pop(0) for _ in range(0, 10)])
        shop.save()

from time import perf_counter
from django.db import connection, reset_queries

def check(func):

    def inner(*args, **kwargs):
        reset_queries()

        start_time = perf_counter()
        begin_number = len(connection.queries)

        func(*args, **kwargs)

        end_number = len(connection.queries)
        end_time = perf_counter()

        print(
            "Time: ", end_time - start_time,
            "Queries number: ", end_number - begin_number,
            sep='\n'
        )
    return inner

@check
def get_all_books():
    books = Book.objects.all()
    for book in books:
        f"title= {book.title}, publisher - {book.publisher.name}, price - {book.price}"

@check
def get_all_books_short():
    books = Book.objects.all()
    for book in books:
        f"title= {book.title}, price - {book.price}"

@check
def get_all_books_optimized():
    books = Book.objects.select_related("publisher")
    for book in books:
        f"title= {book.title}, publisher - {book.publisher.name}, price - {book.price}"


@check
def all_shops_books():
    shops = Shop.objects.all()
    for shop in shops:
        for book in shop.books.all():
            book.title


