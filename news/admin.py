from django.contrib import admin
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.utils.safestring import mark_safe

from .models import *


@admin.register(Category)
class Category(admin.ModelAdmin):
    list_display = ('id', 'title')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Tag)
class Tag(admin.ModelAdmin):
    list_display = ('id', 'title')
    prepopulated_fields = {'slug': ('title',)}


class PostAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = News
        fields = '__all__'


@admin.register(News)
class News(admin.ModelAdmin):
    list_display = ('id', 'title', 'create_at', 'author', 'category', 'get_photo', 'is_published')
    list_editable = ("is_published",)
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    list_filter = ("category", 'tags')
    prepopulated_fields = {'slug': ('title',)}
    # fields = ('title', 'content', 'author', 'category', 'tags', 'image', 'is_published',)
    form = PostAdminForm
    save_as = True
    save_on_top = True

    def get_photo(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width=50>')
        return "-"

    get_photo.short_description = "IMAGE"
