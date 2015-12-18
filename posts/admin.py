from django.contrib import admin

from .models import Post
from .models import Category
from .models import Tag


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at',)
    list_display_links = ('id', 'title',)
    ordering = ('-id', '-created_at')
    list_fliter = ('title', )
    search_fields = ('content',)
    date_hierarchy = 'created_at'


admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Tag)
