from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'restaurante.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'recetario.views.inicio', name='inicio'),
    url(r'^usuarios/$', 'recetario.views.usuarios', name='usuarios'),
    url(r'^sobre/$', 'recetario.views.sobre', name='sobre'),
    url(r'^receta/(?P<id_receta>\d+)$', 'recetario.views.detalle_receta', name='detalle_receta'),
    url(r'^recetas/$', 'recetario.views.lista_recetas', name='lista_recetas'),
    url(r'^receta/nueva/$', 'recetario.views.nueva_receta', name='nueva_receta'),
    url(r'^comenta/$', 'recetario.views.nuevo_comentario', name='nuevo_comentario'),
    url(r'^usuario/nuevo/$', 'recetario.views.nuevo_usuario', name='nuevo_usuario'),
    url(r'^ingresar/$', 'recetario.views.ingresar', name='ingresar'),
    url(r'^privado/$', 'recetario.views.privado', name='privado'),
    url(r'^cerrar/$', 'recetario.views.cerrar', name='cerrar'),
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
