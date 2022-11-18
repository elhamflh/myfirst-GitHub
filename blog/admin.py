from django.contrib import admin
from . import models
# Register your models here.

# class ArticleAdmin(admin.ModelAdmin):
#     list_display= ("title","slug","publish","status")
#     list_filter = ("publish","status")
#     search_fields=("title","des")
#     prepopulated_fields={"slug": ("title",)}
#     ordering = ["-status","publish"]
#  ArticleAdmin
admin.site.register(models.Article)
admin.site.register(models.Authur)







