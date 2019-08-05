from django.contrib import admin
from .models import Question, Choice, Author
import re

admin.site.register(Question)
admin.site.register(Choice)

""" 
5. Adjust the Django admin panel for the Author model that IP addresses
are displayed but the last 8 bits are masked with asterisk
"""


def encrypted_inet(obj):
    ip = obj.inet.ip.exploded
    encrypted = re.sub(r'[0-9]+\.[0-9]+$',
                       r'*.*', ip)
    return encrypted


class AuthorAdmin(admin.ModelAdmin):
    fields = ('name', 'inet')
    list_display = ('name', encrypted_inet)


admin.site.register(Author, AuthorAdmin)
