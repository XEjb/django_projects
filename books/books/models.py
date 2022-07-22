from django.db import models

# Create your models here.

class Publisher(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
            db_table = 'publishers'

class Book(models.Model):
    title = models.CharField(max_length=255)
    price = models.IntegerField()
    publisher = models.ForeignKey('Publisher', on_delete=models.CASCADE)

    class Meta:
        db_table = 'books'

    def get_publisher_name(self):
        return self.publisher.name

    get_publisher_name.short_description = 'publisher'

class Shop(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField('Book')

    class Meta:
        db_table = 'shops'



