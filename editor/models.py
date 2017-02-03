from django.db import models

# Create your models here.

from django.conf import settings
from django.template import defaultfilters


LENGUAJES = ( 
    ('java', 'Java'), 
    ('python', 'Python'), 
    ('c', 'C'),
    ('cpp', 'C++'),
) 

class Codigo(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    codigo = models.TextField()
    tipo = models.CharField(max_length=10, choices=LENGUAJES)
    #output = models.TextField()
    #run_success = models.IntegerField(default=0)
    #run_failed = models.IntegerField(default=0)
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL)
    publ_priv = models.BooleanField(default=False)
    slug = models.SlugField(max_length=100)

    '''
    def save(self, *args, **kwargs):
           if not self.id:
                self.slug = defaultfilters.slugify(self.nombre)
                super(Codigo, self).save(*args, **kwargs)
    '''
    
    def __unicode__(self):
        return self.nombre


