from django.contrib import admin
from parler.admin import TranslatableAdmin

from .models import Tenders

@admin.register(Tenders)
class TendersAdmin(TranslatableAdmin):
	list_display = ('title', 'text', 'created_at', )
	list_display_links = ('title', 'text', 'created_at')

	readonly_fields = ('created_at', )
	
	def get_prepopulated_fields(self, request, obj = None):
		return {'slug': ('title',)}
	

	fieldsets = (
        (None, {
            'fields': ('title', 'text', 'slug')
        }),
        
    )

	search_fields = ('title',)

