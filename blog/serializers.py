from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import *


class DynamicFieldsModelSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        fields = kwargs.pop('fields', None)
        read_only_fields = kwargs.pop('read_only_fields', None)
        super(DynamicFieldsModelSerializer, self).__init__(*args, **kwargs)
        if fields is not None:
            allowed = set(fields)
            existing = set(self.fields.keys())
            for field_name in existing - allowed:
                self.fields.pop(field_name)
        if read_only_fields is not None:
            for field_name in read_only_fields:
                self.fields[field_name].read_only = True


class UserSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
    
    def validate(self, validated_data):
        try:
            user = User.objects.get(username=validated_data['username'])
        except User.DoesNotExist:
            return validated_data
        raise serializers.ValidationError("用户名已存在")

class UserSignInSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')

    def validate(self, validated_data):
        try:
            user = User.objects.get(**validated_data)
            self.context['request'].session['user_id'] = user.id
        except User.DoesNotExist:
            raise serializers.ValidationError('登录失败')
        return validated_data


class ArticleSerializer(DynamicFieldsModelSerializer):
    favorites = serializers.StringRelatedField(many=True,read_only=True)
    class Meta:
        model = Article
        fields = '__all__'
        read_only_fields = ('user', 'favorites_total')

class ArticleFavoriteSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'
        read_only_fields = ('user', 'title', 'description', 'favorites_total')

    def validate(self, validated_data):
        user = self.context['request'].user
        article = self.instance
        validated_data = {}
        try:
            favorite = Favorites.objects.get(user=user, article=article)
            validated_data['favorite'] = favorite
        except Favorites.DoesNotExist:
            pass
        validated_data.update(dict(
            user=user,
            article=article,
        ))
        return validated_data

    def save(self, **kwargs):
        article = self.validated_data['article']
        if 'favorite' in self.validated_data:
            # 取消点赞
            self.validated_data['favorite'].delete()
            article.favorites_total -= 1
        else:
            Favorites.objects.create(**self.validated_data)
            article.favorites_total += 1
        article.save()
