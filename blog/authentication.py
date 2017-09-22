from django.db import transaction
from django.middleware.csrf import CsrfViewMiddleware
from django.contrib.auth.models import AnonymousUser
from django.utils.timezone import now, timedelta,datetime
from rest_framework import authentication
from rest_framework import exceptions
import time
from blog.models import *

class UserAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        user_id = request.session.get('user_id')
        if not user_id:
            return None
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            raise exceptions.AuthenticationFailed('No such user')
        return (user,None)