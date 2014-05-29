from django.contrib import admin

from catalog.models import Drug


class DrugAdmin(admin.ModelAdmin):
    # поле для поиска в админке
    search_fields = ['title', 'symptoms', 'contraindications', 'description']
    list_display = ('title',)

admin.site.register(Drug, DrugAdmin)
