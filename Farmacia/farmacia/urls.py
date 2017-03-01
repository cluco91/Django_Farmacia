from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('apps.medicamentos.urls', namespace="medicamentos_app")),
    url(r'^ventas/', include('apps.ventas.urls', namespace="ventas_app")),
    url(r'^', include('apps.users.urls',  namespace='users_app')),
    url(r'^', include('apps.clientes.urls',  namespace='clientes_app')),
    url(r'^', include('apps.distribuidor.urls',  namespace='distribuidores_app')),
    url(r'^', include('apps.compras.urls',  namespace='compras_app')),
    url(r'^', include('apps.laboratorio.urls',  namespace='laboratorios_app')),
    url(r'^todolist/', include('apps.inline.urls',  namespace='todolist')),
    url(r'^', include('apps.factura.urls',  namespace='factura_app')),
)

if settings.DEBUG:
    urlpatterns += patterns("",
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT,}
        ),
    )