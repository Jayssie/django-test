from django.conf.urls import url
from . import views

app_name = 'blog'
urlpatterns = [
    url(r'^users/$', views.UserView.as_view(), name='user'),
    url(r'^users/sign_in$', views.UserSignInView.as_view(), name='users_sign_in'),
    url(r'^articles/$', views.ArticleView.as_view(), name='articles'),
    url(r'^articles/(?P<pk>[0-9]+)/',views.ArticleDetailView.as_view(), name='article_detail'),
    url(r'^articles/favorites/(?P<pk>[0-9]+)/$',views.AddFavoritesView.as_view(), name='add_favorites'),
]
