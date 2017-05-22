from tastypie.resources import ModelResource
from tastypie import fields
from evento.models import Evento, TipoInscricao, Inscricoes, PessoaFisica
from django.contrib.auth.models import User
from tastypie.authorization import Authorization


class TipoInscricaoResource(ModelResource):
    class Meta:
        queryset = TipoInscricao.objects.all()
        allowed_methods = ['get', 'post']
        always_return_data = True
        authorization = Authorization()
        filtering = {
            "descricao": ('exact', 'startswith',)
        }


class EventoResource(ModelResource):
    class Meta:
        queryset = Evento.objects.all()
        allowed_methods = ['get', 'post']
        always_return_data = True


class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'user'
        excludes = ['password', 'is_active']


class PessoaFisicaResource(ModelResource):
    class Meta:
        queryset = PessoaFisica.objects.all()
        allowed_methods = ['get']


class InscricaoResource(ModelResource):
    pessoafisica = fields.ToOneField(PessoaFisicaResource, 'pessoa')
    evento = fields.ToOneField(EventoResource, 'evento')
    tipoInscricao = fields.ToOneField(TipoInscricaoResource, 'tipoInscricao')

    class Meta:
        queryset = Inscricoes.objects.all()
        allowed_methods = ['get', 'post']
        always_return_data = True
        authorization = Authorization()
