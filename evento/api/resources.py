from tastypie.resources import ModelResource
from tastypie import fields
from evento.models import Evento, TipoInscricao, Inscricoes, PessoaFisica
from django.contrib.auth.models import User
from tastypie.authorization import Authorization
from tastypie.exceptions import Unauthorized


class TipoInscricaoResource(ModelResource):
    class Meta:
        queryset = TipoInscricao.objects.all()
        allowed_methods = ['get', 'post']
        always_return_data = True
        authorization = Authorization()
        filtering = {
            "descricao": ('exact', 'startswith',)
        }


    def obj_create(self, bundle, **kwargs):
        tipo = TipoInscricao()
        tipo.descricao = bundle.data['descricao'].upper()
        tipo.save()
        bundle.obj = tipo
        return bundle


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
        allowed_methods = ['get', 'post', 'delete']
        always_return_data = True
        authorization = Authorization()

    def obj_get_list(self, bundle, **kwargs):
        return self.get_object_list(bundle.request)

    def obj_delete_list(self, bundle, **kwargs):
        raise Unauthorized("Sorry, no deletes.")

