from django.contrib import admin
from .models import Post
# Register your models here.
# admin.site.register(Post)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date_posted')
    search_fields = ('title', 'content')
    list_filter = ('author', 'date_posted' )
    date_hierarchy = ('date_posted')
