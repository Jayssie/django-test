from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(u"username", max_length=128)
    email = models.EmailField(u"email",db_index=True)
    password = models.CharField(u"password", max_length=256)
    reg_time =  models.DateTimeField(u"register_time", auto_now_add=True)
    def is_authenticated(self):
        return True
    def check_password(self, pwd):
        return self.password == pwd
    def __str__(self):
        return self.username
    class Meta:
        verbose_name_plural = u"user_info"
        ordering = ['-reg_time']

class Article(models.Model):
    user = models.ForeignKey(User, related_name="author")
    title = models.CharField(u"title", max_length=256, default="title")
    description = models.CharField(u"description", max_length=256)
    favorites_total = models.IntegerField(u"favorites_total", default=0)
    class Meta:
        verbose_name_plural = u"article_info"
        ordering = ['-favorites_total']

class Favorites(models.Model):
    user = models.ForeignKey(User, related_name="user")
    article = models.ForeignKey(Article, related_name="favorites")
    class Meta:
        unique_together = ('article', 'id')
        verbose_name_plural = u"favorites_info"
    def __str__(self):
        return '%d: %s' % (self.id, self.user)



