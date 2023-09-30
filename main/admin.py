from django.contrib import admin
from users.models import Contact
from users.models import Join_us
from users.models import Book
# from main.models import Joinus
# Register your models here.
admin.site.register(Contact)
admin.site.register(Join_us)
admin.site.register(Book)