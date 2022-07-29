from django.contrib import admin

# Register your models here.
from .models import Chapter, Contact, Material, Mathematics, Physics, Chemistry

admin.site.register(Chapter)
admin.site.register(Contact)
admin.site.register(Material)
admin.site.register(Mathematics)
admin.site.register(Physics)
admin.site.register(Chemistry)