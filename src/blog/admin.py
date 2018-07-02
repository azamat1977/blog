from django.contrib import admin
from .models import Article, Category, TaggedArticle
# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('content', 'location', 'title', 'category', 'updated', 'timestamp', 'published', 'is_approved')

    def get_absolute_url(self):
        return "/article/{}/".format(self.id)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('comment', 'updated', 'title', 'timestamp', 'category')

    def get_absolute_url(self):
        return "/article/{}/".format(self.id)

class TaggedArticleAdmin(admin.ModelAdmin):
    list_display = ('user', 'email', 'article', 'timestamp')

    def get_absolute_url(self):
        return "/article/{}/".format(self.id)

admin.site.register(Article, ArticleAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(TaggedArticle, TaggedArticleAdmin)