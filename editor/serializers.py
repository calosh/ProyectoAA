from django.conf.urls import url, include
from .models import Codigo
from rest_framework import routers, serializers, viewsets

from django.conf import settings


# Serializers define the API representation.
class CodigoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Codigo
        fields = ('url','nombre', 'tipo',)


# ViewSets define the view behavior.
class CodigoViewSet(viewsets.ModelViewSet):
    queryset = Codigo.objects.all()
    serializer_class = CodigoSerializer


'''
# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = settings.AUTH_USER_MODEL
        fields = ('username', 'email', 'first_name',)


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = settings.AUTH_USER_MODEL.objects.all()
    serializer_class = UserSerializer

'''