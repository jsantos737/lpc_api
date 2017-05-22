from django.conf.urls import url, include
from tastypie.api import Api
from django.contrib import admin
from evento.api.resources import TipoInscricaoResource, UserResource, InscricaoResource, PessoaFisicaResource

from evento.views import *

v1_api = Api(api_name='v1')
v1_api.register(TipoInscricaoResource())
v1_api.register(UserResource())
v1_api.register(InscricaoResource())
v1_api.register(PessoaFisicaResource())

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index, name='index'),
    url(r'^api/', include(v1_api.urls)),
]
