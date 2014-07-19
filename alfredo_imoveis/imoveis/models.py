# encoding: utf8
from django.db import models
from enderecos.models import Endereco
from clientes.models import Cliente
from empresas.models import Empresa

TIPO_CONTRATO = (
    ('C', 'COMERCIAL'),
    ('R', 'RESIDENCIAL'),
)

class Imovel(models.Model):
    endereco = models.ForeignKey(Endereco, null = False, blank = False, verbose_name='Endereço')
    descricao = models.CharField(u'Descrição do imóvel', max_length=300)
    cod_ref_site = models.CharField(u'Código de referência no site', max_length=120, null=True, blank=True)
    valor_iptu = models.DecimalField('Valor do IPTU',max_digits=6, decimal_places=2)
    valor_aluguel = models.DecimalField('Valor do Aluguel',max_digits=6, decimal_places=2)
    ultima_vistoria = models.DateField(u'Data da última vistoria', null=True, blank=True)
    data_cadastro = models.DateField(auto_now_add=True)
    proprietario = models.ForeignKey(Cliente,verbose_name='Proprietário')
    empresa = models.ForeignKey(Empresa,verbose_name='Filial responsável')
    ativo = models.BooleanField(default=True, verbose_name='Imóvel ativo')
    tipo_imovel = models.CharField(max_length=1, choices=TIPO_CONTRATO, verbose_name='Tipo do imóvel', default='R')

    def __unicode__(self):
        return self.proprietario.nome + ' - '+ str(self.proprietario.id) + ' - '+ self.descricao[:50:] + '-' + self.endereco.rua

    @property
    def disponivel(self):
        pass

    def retorna_tipo_imovel(self):
        return 'Residencial' if self.tipo_imovel == 'R' else 'Comercial'

    class Meta:
        ordering = ['descricao']
       
class ContratoLocacao(models.Model):
    imovel = models.OneToOneField(Imovel)
    inicio_contrato = models.DateField(u'Data do início do contrato')
    termino_contrato = models.DateField(u'Data do término do contrato')
    data_emissao_contrato = models.DateField(auto_now_add=True)
    locatario = models.ForeignKey(Cliente, related_name='locatario_contrato')
    fiador1 = models.ForeignKey(Cliente, related_name='fiador1_contrato', verbose_name=u'Primeiro fiador')
    fiador2 = models.ForeignKey(Cliente, null=True, blank=True, related_name='fiador2_contrato', verbose_name=u'Segundo fiador')
    fiador3 = models.ForeignKey(Cliente, null=True, blank=True, related_name='fiador3_contrato', verbose_name=u'Terceiro fiador')
    empresa = models.ForeignKey(Empresa,verbose_name='Filial responsável')
    tipo_contrato = models.CharField(max_length=1, choices=TIPO_CONTRATO, verbose_name='Tipo do contrato')
    observacao = models.TextField(verbose_name='Observações do contrato', null=True, blank=True)
    gerou_receber = models.BooleanField(verbose_name='Já gerou contas a receber', default=False, editable=False)

    def __unicode__(self):
        return self.imovel.descricao[:15:]+ ' - ' +self.locatario.nome

class ContratoAdministrativo(models.Model):
    imovel = models.OneToOneField(Imovel)
    inicio_contrato = models.DateField(u'Data do início do contrato')
    termino_contrato = models.DateField(u'Data do término do contrato') 
    data_emissao_contrato = models.DateField(u'Data da emissão do contato', auto_now=True, auto_now_add=True) 
    empresa = models.ForeignKey(Empresa,verbose_name='Filial responsável')
    
    def __unicode__(self):
        return str(self.imovel.descricao) + u' - Início: '+  unicode(self.inicio_contrato) + u' - Término:' + unicode(self.termino_contrato)

    def get_absolute_url(self):
        return reverse('app_imoveis_contrato_administrativo_home', kwargs={'pk': self.pk})


class LaudoVistoria(models.Model):
    imovel = models.ForeignKey(Imovel)
    data_vistoria = models.DateField(u'Data da vistoria')
    pintura_interna = models.CharField(max_length=100, verbose_name=u'Pintura interna', null=True, blank=True)
    pintura_externa = models.CharField(max_length=100, verbose_name=u'Pintura externa',null=True, blank=True)
    muros = models.CharField(max_length=100, verbose_name=u'Muros',null=True, blank=True)
    ferragens = models.CharField(max_length=100, verbose_name=u'Ferragens',null=True, blank=True)
    cores = models.CharField(max_length=100, verbose_name=u'Cores',null=True, blank=True)
    tipo_tinta = models.CharField(max_length=100, verbose_name=u'Tipos de tintas',null=True, blank=True)
    lampadas_comuns = models.CharField(max_length=100, verbose_name=u'Lâmpadas comuns',null=True, blank=True)
    lustres = models.CharField(max_length=100, verbose_name=u'Lustres',null=True, blank=True)
    globos = models.CharField(max_length=100, verbose_name=u'Globos',null=True, blank=True)
    lampadas_fluorecentes = models.CharField(max_length=100, verbose_name=u'Lâmpadas fluorecentes',null=True, blank=True)
    lampiao = models.CharField(max_length=100, verbose_name=u'Lampião',null=True, blank=True)
    interruptores = models.CharField(max_length=100, verbose_name=u'Interruptores',null=True, blank=True)
    luminarias = models.CharField(max_length=100, verbose_name=u'Lumínárias',null=True, blank=True)
    espelho_banheiro = models.CharField(max_length=100, verbose_name=u'Espelhos dos banheiros',null=True, blank=True)
    campainha = models.CharField(max_length=100, verbose_name=u'Campainha',null=True, blank=True)
    ar_condicionado = models.CharField(max_length=100, verbose_name=u'Ar condicionado',null=True, blank=True)
    instalacao = models.CharField(max_length=100, verbose_name=u'Instalação',null=True, blank=True)
    portao_eletronico = models.CharField(max_length=100, verbose_name=u'Portão eletrônico',null=True, blank=True)
    torneiras = models.CharField(max_length=100, verbose_name=u'Torneiras',null=True, blank=True)
    chuveiro = models.CharField(max_length=100, verbose_name=u'Chuveiro',null=True, blank=True)
    vaso = models.CharField(max_length=100, verbose_name=u'Vaso',null=True, blank=True)
    lavatorio = models.CharField(max_length=100, verbose_name=u'Lavatório',null=True, blank=True)
    tanque = models.CharField(max_length=100, verbose_name=u'Tanque',null=True, blank=True)
    bide = models.CharField(max_length=100, verbose_name=u'Bidê',null=True, blank=True)
    descarga = models.CharField(max_length=100, verbose_name=u'Descarga',null=True, blank=True)
    box = models.CharField(max_length=100, verbose_name=u'Box',null=True, blank=True)
    rede_esgoto = models.CharField(max_length=100, verbose_name=u'Rede de esgoto',null=True, blank=True)
    tacos = models.CharField(max_length=100, verbose_name=u'Tacos',null=True, blank=True)
    pisos = models.CharField(max_length=100, verbose_name=u'Pisos',null=True, blank=True)
    ceramico = models.CharField(max_length=100, verbose_name=u'ceramico',null=True, blank=True)
    paredes = models.CharField(max_length=100, verbose_name=u'Paredes',null=True, blank=True)
    azulejos = models.CharField(max_length=100, verbose_name=u'Azuleijos',null=True, blank=True)
    vidros = models.CharField(max_length=100, verbose_name=u'Vidros',null=True, blank=True)
    portas = models.CharField(max_length=100, verbose_name=u'Portas',null=True, blank=True)
    fechaduras = models.CharField(max_length=100, verbose_name=u'Fechaduras',null=True, blank=True)
    trincos = models.CharField(max_length=100, verbose_name=u'Trincos',null=True, blank=True)
    janelas = models.CharField(max_length=100, verbose_name=u'Janelas',null=True, blank=True)
    muros = models.CharField(max_length=100, verbose_name=u'Muros',null=True, blank=True)
    grades = models.CharField(max_length=100, verbose_name=u'Grades',null=True, blank=True)
    telhado = models.CharField(max_length=100, verbose_name=u'Telhado',null=True, blank=True)
    forro = models.CharField(max_length=100, verbose_name=u'Forro',null=True, blank=True)
    laje = models.CharField(max_length=100, verbose_name=u'Laje',null=True, blank=True)
    portao = models.CharField(max_length=100, verbose_name=u'Portão',null=True, blank=True)
    armarios = models.CharField(max_length=100, verbose_name=u'Armários',null=True, blank=True)
    guarda_roupas = models.CharField(max_length=100, verbose_name=u'Guarda-roupas',null=True, blank=True)
    rede_protecao = models.CharField(max_length=100, verbose_name=u'Rede de protecao',null=True, blank=True)
    chaves = models.CharField(max_length=100, verbose_name=u'Chaves',null=True, blank=True)
    observacao = models.TextField(verbose_name='Observações sobre a vistoria', null=True, blank=True)


    def __unicode__(self):
        return str(self.imovel.descricao)  + ' Data vistoria: ' + unicode(self.data_vistoria.strftime('%d-%m-%Y'))

    def get_absolute_url(self):
        return reverse('app_imoveis_laudo_vistoria_home', kwargs={'pk': self.pk})