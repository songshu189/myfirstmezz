from django.contrib import admin
from mezzanine.pages.admin import PageAdmin
from .models import InterestPage

admin.site.register(InterestPage, PageAdmin)
