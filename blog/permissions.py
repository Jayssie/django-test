from rest_framework import permissions
from rest_framework.exceptions import PermissionDenied
from django.shortcuts import render, get_object_or_404
from .models import *


class IsOwner(permissions.BasePermission):
    message = u'非作者'

    def has_object_permission(self, request, view, obj):
        if request.user.is_authenticated() and obj.user == request.user:
            return True
        return False


class IsAuthenticated(permissions.IsAuthenticated):
    message = u'没有登录'
