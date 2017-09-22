from django.shortcuts import render, get_object_or_404
from django.views.generic import *
from rest_framework import mixins, generics, views, permissions, status, filters
from django.utils.timezone import now, timedelta, datetime
from rest_framework.response import Response
from django.http import *
from .permissions import IsOwner, IsAuthenticated
from .serializers import *
# Create your views here.

class UserView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = (permissions.AllowAny,)

class UserSignInView(generics.GenericAPIView):
    serializer_class = UserSignInSerializer
    permission_classes = (permissions.AllowAny,)
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response()
    
class ArticleView(generics.ListCreateAPIView):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all().order_by('-favorites_total')
    permission_classes = (IsAuthenticated,)
    def perform_create(self, serializer): 
        instance = serializer.save(user=self.request.user)

class ArticleDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all().order_by('-favorites_total')
    serializer_class = ArticleSerializer
    permissions_classes = (IsAuthenticated, IsOwner)
    search_fields = ('description','title',)

class AddFavoritesView(generics.UpdateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleFavoriteSerializer
    permission_classes = (IsAuthenticated,)
