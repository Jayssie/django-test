from django.contrib import admin
from .models import *
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    model = User
    extra = 3
    list_display = ('username', 'email', 'reg_time')
    list_filter = ['reg_time']
    search_fields = ['username']

class ArticleAdmin(admin.ModelAdmin):
    model = Article
    extra = 3
    list_display = ('user', 'description')
    search_fields = ['description']

class FavoritesAdmin(admin.ModelAdmin):
    model = Favorites
    extra = 3


admin.site.register(User, UserAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Favorites, FavoritesAdmin)