from django.db import models
from django.db.models import Model
from django.db.models import CharField, BooleanField, NullBooleanField, FileField, IntegerField, EmailField, TextField, ImageField
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator
from django.conf import settings
from django.contrib.auth.hashers import make_password


# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)



class Client(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE, null=True)
    cnpj = CharField(max_length=255, verbose_name=u'CNPJ')
    name = CharField(max_length=200, verbose_name=u'Apelido da Instituição')
    code = CharField(max_length=200, verbose_name=u'Código')
    year = IntegerField()
    active = NullBooleanField(verbose_name=u'Ativo')

    def __str__(self):
        return self.name + ' - ' + self.cnpj


class Product(models.Model):
    PARTICIPATION_CHOICES = [('Abertura de Segmento', 'Abertura de Segmento'),
                             ('Página Exclusiva', 'Página Exclusiva'),
                             ('Contra Capa', 'Contra Capa'),
                             ('Ipanema', 'Ipanema')]

    SEGMENT_CHOICES = [('Administradores', 'Administradores'),
                       ('Advogados', 'Advogados'),
                       ('Agentes Fiduciários', 'Agentes Fiduciários'),
                       ('Auditores', 'Auditores'),
                       ('Avaliadores e Classificadoras',
                        'Avaliadores e Classificadoras'),
                       ('Consultores', 'Consultores'),
                       ('Custodiantes', 'Custodiantes'),
                       ('Distribuidores', 'Distribuidores'),
                       ('Estruturadores', 'Estruturadores'),
                       ('Fintechs', 'Fintechs'),
                       ('Gestores', 'Gestores'),
                       ('Informação e Análise', 'Informação e Análise'),
                       ('Investidores Institucionais',
                        'Investidores Institucionais'),
                       ('Securitizadoras', 'Securitizadoras'),
                       ('Servicers e Agentes de Cobrança',
                        'Servicers e Agentes de Cobrança'),
                       ('Tecnologia da Informação', 'Tecnologia da Informação'),
                       ('Lawtechs', 'Lawtechs'),
                       ('Seguradoras', 'Seguradoras'),
                       ('Infraestrutura de Mercado', 'Infraestrutura de Mercado'),
                       ('', '')]

    CONDITION_CHOICES = [('Pagante', 'Pagante'), ('Cortesia', 'Cortesia')]

    STATUS_CHOICES = [('Não Iniciado', 'Não Iniciado'), ('Incompleto',
                                                         'Incompleto'), ('Concluído', 'Concluído'), ('Aprovado', 'Aprovado')]

    client = models.ForeignKey(
        Client, verbose_name=u'Cliente', on_delete=models.CASCADE)
    participation = CharField(
        max_length=100, verbose_name=u'Participação', choices=PARTICIPATION_CHOICES)
    segment = CharField(max_length=100, verbose_name=u'Segmento',
                        choices=SEGMENT_CHOICES, blank=True)
    condition = CharField(
        max_length=50, verbose_name=u'Condição', choices=CONDITION_CHOICES)
    layout = NullBooleanField(verbose_name=u'Layout')
    layoutuqbar = NullBooleanField(verbose_name=u'Layout UQBAR')
    status = CharField(max_length=50, verbose_name=u'Status',
                       choices=STATUS_CHOICES, default='Não Iniciado')

    def __str__(self):
        if self.segment == '':
            return 'Produto ' + str(self.id)
        else:
            return 'Produto ' + str(self.id)