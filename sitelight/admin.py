from django.contrib import admin
from models import Category , Entry
from forms import EntryForm

class EntryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    form = EntryForm

admin.site.register(Entry, EntryAdmin)
admin.site.register(Category)
