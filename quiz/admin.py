from django.contrib import admin

from .models import Techniques, Belt_group

# admin.site.register(Techniques)
admin.site.register(Belt_group)
# Register your models here.



class TechniquesAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['belt_group']}),
        ('Techinc info', {'fields': ['name', 'photo']}),

        ]

admin.site.register(Techniques, TechniquesAdmin)