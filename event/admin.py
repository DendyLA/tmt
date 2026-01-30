from django.contrib import admin
from django.utils.html import format_html
from parler.admin import TranslatableAdmin

from . import models


@admin.register(models.Event)
class EventAdmin(TranslatableAdmin):
    list_display = ('preview', 'title', 'city','pub_date', 'event_date')
    list_display_links = ('preview', 'title')
    readonly_fields = ('preview', 'pub_date')  # Добавлено preview в readonly
    ordering = ('-pub_date',)
    list_per_page = 20  # Добавлено для пагинации
    search_fields = ('title', 'city')

    list_editable = ('event_date',)
    

    fieldsets = (
        (None, {
            'fields': ('image', 'title', 'text', 'city', 'event_date', 'event_end_date' )
        }),
        ('Дополнительно', {
            'fields': ('preview', 'pub_date', 'slug'),  # Добавлено preview
            'classes': ('collapse',)
        }),
    )

    def get_prepopulated_fields(self, request, obj = None):
        return {'slug': ('title',)}

    @admin.display(description="Превью")
    def preview(self, obj):
        if obj.image and hasattr(obj.image, 'url'):  # Добавлена проверка на наличие url
            return format_html(
                '<image src="{}" style="max-height: 100px; max-width: 150px; '
                'object-fit: contain; border: 1px solid #ddd; border-radius: 4px;"/>',
                obj.image.url
            )
        return "Нет изображения"  # Добавлен fallback



@admin.register(models.EventAbout)
class EventAboutAdmin(TranslatableAdmin):
    list_display = ('preview', )
    list_display_links = ('preview',)

    @admin.display(description='Превью')
    def preview(self, obj):
        if obj.image and hasattr(obj.image, 'url'):
            return format_html(
                '<image src="{}" style="max-height: 100px; max-width: 150px; '
                'object-fit: contain; border: 1px solid #ddd; border-radius: 4px;"/>',
                obj.image.url
            )
        return 'No image'


@admin.register(models.EventDirection)
class EventDirectionAdmin(TranslatableAdmin):
    list_display = ('preview', 'name')
    list_display_links = ('preview', 'name')

    @admin.display(description='Превью')
    def preview(self, obj):
        if obj.image and hasattr(obj.image, 'url'):
            return format_html(
                '<image src="{}" style="max-height: 100px; max-width: 150px; '
                'object-fit: contain; border: 1px solid #ddd; border-radius: 4px;"/>',
                obj.image.url
            )
        return 'No image'
    

@admin.register(models.EventPackb2b)
class EventPackb2bAdmin(TranslatableAdmin):
    list_display = ('name',)
    list_display_links = ('name',)
    
@admin.register(models.EventPackb2g)
class EventPackb2gAdmin(TranslatableAdmin):
    list_display = ('name',)
    list_display_links = ('name',)




@admin.register(models.Programme)
class ProgrammeAdmin(TranslatableAdmin):
    list_display = ('file',)
    list_display_links = ('file',)


@admin.register(models.Catalog)
class CatalogAdmin(TranslatableAdmin):
    list_display = ('file',)
    list_display_links = ('file',)
