import base64, os
from rest_framework.decorators import api_view
from .imports import *


def login_required(func):
    def inner_login(self, request, *args, **kwargs):
        id = request.META.get('HTTP_ID') or request.META.get('HTTPS_ID')
        password = request.META.get('HTTP_PASSWORD') or request.META.get('HTTPS_PASSWORD')
        user = User.objects.filter(id=id).first()

        if user and user.password == password and user.is_superuser:    
            return func(self, request, *args, **kwargs)
        return Response({'message':'please login again'},status=401)
        
    return inner_login


@api_view(['POST']) 
def login(request):
    username = request.data.get('username').strip()
    password = request.data.get('password').strip()
    user = User.objects.filter(username=username).first()
    if user and user.check_password(password) and user.is_superuser:
        if user.image:
            with open(user.image.path, "rb") as file:
                image = base64.b64encode(file.read()).decode('utf-8')
        else:
            image = ""
        return Response({
            'id':user.id,
            'fullName':user.username,
            'username':user.username,
            'password':user.password,
            'avatar':"data:image/jpeg;base64,"+image
            })
    return Response({"message":"username or password error"},status=401)











