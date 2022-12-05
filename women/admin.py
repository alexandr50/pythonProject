from django.contrib import admin
from django.utils.safestring import mark_safe

from women.models import Women, Categories

class WomenAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'get_html_photo', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'created_at')
    prepopulated_fields = {'slug': ('title',)}
    fields = ('title', 'slug', 'cat', 'content', 'photo', 'get_html_photo', 'is_published', 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at', 'get_html_photo')
    save_on_top = True

    def get_html_photo(self, obj):
        if obj.photo:
            return mark_safe(f"<img src='{obj.photo.url}' width=50>")

    get_html_photo.short_description = 'Миниатюра'



class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Women, WomenAdmin)
admin.site.register(Categories, CategoriesAdmin)

admin.site.site_title = 'Админ парель сайта о женщинах'
admin.site.site_header = 'Админ парель сайта о женщинах2'

