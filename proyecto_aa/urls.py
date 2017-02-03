from django.conf.urls import include, url
from django.contrib import admin

from rest_framework import routers


from editor.serializers import CodigoViewSet

router = routers.DefaultRouter()
router.register(r'codigos', CodigoViewSet)


urlpatterns = [
    # Examples:
    # url(r'^$', 'proyecto_aa.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^api/', include(router.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('editor.urls')),
    url(r'^users/', include('users.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
