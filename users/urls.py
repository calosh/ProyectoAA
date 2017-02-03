from django.conf.urls import patterns, url

from .views import LoginView, RegisterView

urlpatterns = patterns('',
    url(r'^login$', LoginView.as_view(), name='login'),
    url(r'^salir$', 'users.views.salir', name='salir'),
    url(r'^register$', RegisterView.as_view(), name='register'),
)