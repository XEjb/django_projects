from django.contrib import admin
from .models import Book, Shop, Publisher



@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'price',
        'get_publisher_name',
    )
    list_filter = (
        'title',
        'price',
    )

    search_fields = (
        'title',
    )

    fieldsets = (
        (
            'About', {
                'fields': ('title',)
            }
        ),
        (
            'Shop info', {
                'fields': ('price',)
            }
        )
    )


@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    pass


class BookInstance(admin.TabularInline):
    model = Book


@admin.register(Publisher)
class Publisher(admin.ModelAdmin):
    list_display = (
        'name',
    )
    inlines = [BookInstance]