from django.contrib import admin
from .models import Category,Complain,Like


class ComplainAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug': ('title',)}
    list_display=('title','category','is_featured', 'author', 'complain_status')
    search_fields=('title', 'id','category__Category_name','complain_status')
    list_editable=('is_featured',)

# Register your models here.
admin.site.register(Category)
admin.site.register(Like)

admin.site.register(Complain ,ComplainAdmin)