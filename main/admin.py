from django.contrib import admin
from django.utils.html import format_html

from .models import Subscriber, Slider, Slogan,Services, News, Feedbacks, Partners, Video, Info



admin.site.register(Slogan)
admin.site.register(Services)

@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('email', 'created_at')
    search_fields = ('email',)
    list_filter = ('created_at',)




@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ('preview', 'link', 'created_at')
    list_display_links = ('preview',)
    readonly_fields = ('created_at',)
    ordering = ('-created_at',)
    
    fieldsets = (
        (None, {
            'fields': ( 'image',  'link')
        }),
        ('Дополнительно', {
            'fields': ('created_at',),  # Запятая важна для кортежа!
            'classes': ('collapse',)
        }),
    )

    @admin.display(description="Превью")
    def preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="max-height: 100px; border: 1px solid #ddd; border-radius: 4px;"/>',
                obj.image.url
            )
        return "-"
    

class NewsAdmin(admin.ModelAdmin):
    list_display = ('image_preview', 'title', 'pub_date')  # отображаем поля title и pub_date в списке новостей
    search_fields = ('title',)  # добавляем возможность поиска по названию новости

    def image_preview(self, obj):
        # Создаем миниатюру изображения
        if obj.image:
            return format_html('<img src="{}" width="100" height="auto" />', obj.image.url)
        return "Нет изображения"
    
    image_preview.short_description = 'Превью изображения'  # Переименовываем заголовок колонки


admin.site.register(News, NewsAdmin)


@admin.register(Feedbacks)
class FeedbacksAdmin(admin.ModelAdmin):
    list_display = ('preview', 'author', 'created_at')
    list_display_links = ('preview', 'author')
    readonly_fields = ('created_at',)
    ordering = ('-created_at',)
    
    fieldsets = (
        (None, {
            'fields': ( 'image',  'author', 'text')
        }),
        ('Дополнительно', {
            'fields': ('created_at',),  # Запятая важна для кортежа!
            'classes': ('collapse',)
        }),
    )

    @admin.display(description="Превью")
    def preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="max-height: 100px; border: 1px solid #ddd; border-radius: 4px;"/>',
                obj.image.url
            )
        return "-"
    


@admin.register(Partners)
class PartnersAdmin(admin.ModelAdmin):
    list_display = ('preview', 'title','url', 'created_at')
    list_display_links = ('preview', 'title')
    readonly_fields = ('created_at',)
    ordering = ('-created_at',)
    
    fieldsets = (
        (None, {
            'fields': ( 'title' ,'image',  'url')
        }),
        ('Дополнительно', {
            'fields': ('created_at',),  # Запятая важна для кортежа!
            'classes': ('collapse',)
        }),
    )

    @admin.display(description="Превью")
    def preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="max-height: 100px; border: 1px solid #ddd; border-radius: 4px;"/>',
                obj.image.url
            )
        return "-"
    

class VideoAdmin(admin.ModelAdmin):
    list_display = ('preview', 'title')   
    list_display_links = ('preview', 'title')      # превью в списке
    readonly_fields = ('preview',)              # превью на странице редактирования

    fieldsets = (
        (None, {
            'fields': ( 'title' ,'file')
        }),
    )

admin.site.register(Video, VideoAdmin)


class InfoAdmin(admin.ModelAdmin):
    list_display = ('preview','previewImg', 'title')   
    list_display_links = ('preview', 'title', 'previewImg')      # превью в списке
    readonly_fields = ('preview',)              # превью на странице редактирования

    fieldsets = (
        (None, {
            'fields': ( 'title' ,'file', 'text', 'poster')
        }),
    )

    @admin.display(description="Превью")
    def previewImg(self, obj):
        if obj.poster:
            return format_html(
                '<img src="{}" style="max-height: 100px; border: 1px solid #ddd; border-radius: 4px;"/>',
                obj.poster.url
            )
        return "-"

admin.site.register(Info, InfoAdmin)