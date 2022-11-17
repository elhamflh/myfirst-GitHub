from django.contrib import admin
from .models import Article,Authur

# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display= ("title","slug","publish","status")
    list_filter = ("publish","status")
    search_fields=("title","des")
    prepopulated_fields={"slug": ("title",)}
    ordering = ["-status","publish"]

admin.site.register(Article,ArticleAdmin)
admin.site.register(Authur)







