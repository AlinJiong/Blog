import jwt
from rest_framework import exceptions
from rest_framework.authentication import BaseAuthentication
from rest_framework_jwt.settings import api_settings

from api import models


class BlogRequestUserAuthentication(BaseAuthentication):

    def authenticate(self, request):
        token = request.COOKIES.get('token')
        if not token:
            # return (None, None)
            raise exceptions.AuthenticationFailed({'code': 1001, 'error': '登录过后才可以操作'})

        jwt_decode_handler = api_settings.JWT_DECODE_HANDLER
        try:
            payload = jwt_decode_handler(token)
        except jwt.ExpiredSignature:
            raise exceptions.AuthenticationFailed({'code': '1002', 'error': 'token已过期'})
        except jwt.DecodeError:
            raise exceptions.AuthenticationFailed({'code': '1003', 'error': 'token格式错误'})
        except jwt.InvalidTokenError:
            raise exceptions.AuthenticationFailed({'code': '1004', 'error': '认证失败'})

        jwt_get_username_from_payload_handler = api_settings.JWT_PAYLOAD_GET_USERNAME_HANDLER
        username = jwt_get_username_from_payload_handler(payload)
        user = models.User.objects.filter(username=username).first()
        print(user, username)
        return (user, token)


from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user
