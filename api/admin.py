from django.contrib import admin

from .models import Tag,TagBookLink,Book
# Register your models here.

admin.site.register(Tag)
admin.site.register(TagBookLink)
admin.site.register(Book)


