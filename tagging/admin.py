from django.contrib import admin
from tagging.models import Tag, TaggedItem, TagType
from tagging.forms import TagAdminForm

class TagAdmin(admin.ModelAdmin):
    form = TagAdminForm
    search_fields = ('name', 'slug')
    list_display = ('name', 'url_link', 'usage_count', 'type')
    list_filter = ('type',)
    list_editable = ('type',)

class TagTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'no_index', 'created_at', 'updated_at')
    list_editable = ('no_index',)

class TaggedItemAdmin(admin.ModelAdmin):
    raw_id_fields = ('tag', 'user')
    list_display = ('tag', 'user', 'created_at', 'object', 'find_user',
        'object_link')
    
    list_filter = ('created_at',)

admin.site.register(TaggedItem, TaggedItemAdmin)
admin.site.register(TagType, TagTypeAdmin)
admin.site.register(Tag, TagAdmin)




