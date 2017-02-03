from django.conf.urls import patterns, url

urlpatterns = patterns('editor.views',
    url(r'^$', 'index', name='index'),
    url(r'codigos/(?P<usuario>\d+)/$', 'codigos_usuario', name='codigos_usuario'),
    url(r'codigo/(?P<usuario>\d+)/(?P<codigo>\d+)$', 'codigo_usuario', name='codigo_usuario'),
    url(r'agregar$', 'agregar', name='agregar'),
    url(r'borrar/(?P<id>\d+)$', 'borrar', name='borrar'),
    url(r'editar/(?P<id>\d+)$', 'editar', name='editar'),
    url(r'estadisticas/$', 'estadisticas', name='estadisticas'),
)

