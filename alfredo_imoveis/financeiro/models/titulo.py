# encoding: utf-8
__author__ = 'gpzim98'

from django.db import models
from django.shortcuts import get_object_or_404
from parametros.models import ParametrosGerais
from empresas.models import Empresa
from financeiro.models.conta_caixa import ContaCaixa
from django.contrib.auth.admin import User
from clientes.models import Cliente
from imoveis.models import ContratoLocacao
from datetime import date
from funcoes import days_between, calcula_meses_atraso, today
from NumerosPorExtenso import extenso

TIPO_CONTA = (
    ('D', 'DESPESA'),
    ('R', 'RECEITA'),
)


class Titulo(models.Model):
    descricao = models.CharField(max_length=500, null=False, blank=False)
    conta_caixa = models.ForeignKey(ContaCaixa, null=True, blank=True)
    empresa = models.ForeignKey(Empresa)
    data_cadastro = models.DateTimeField(
        verbose_name='Data de cadastro', auto_now_add=True)
    vencimento = models.DateField(verbose_name='Data de vencimento')
    data_quitacao = models.DateField(
        verbose_name='Data de quitação do título', null=True, blank=True)
    tipo = models.CharField(
        choices=TIPO_CONTA, max_length=1, verbose_name='Tipo da movimentação',
        help_text='Informe o tipo da movimentação')
    usuario_cadastrou = models.ForeignKey(User)
    valor = models.DecimalField(
        max_digits=6, decimal_places=2, verbose_name='Valor do título')
    valor_copasa = models.DecimalField(
        max_digits=6, decimal_places=2, verbose_name='Valor da COPASA no mês',
        default=0, null=True, blank=True)
    valor_cemig = models.DecimalField(
        max_digits=6, decimal_places=2, verbose_name='Valor da CEMIG no mês',
        default=0, null=True, blank=True)
    valor_encargos = models.DecimalField(
        max_digits=6, decimal_places=2, verbose_name='Valores de encargos',
        default=0, null=True, blank=True)
    perc_juros = models.DecimalField(
        max_digits=4, decimal_places=2, default=0.0, null=True, blank=True)
    taxa_multa = models.DecimalField(
        max_digits=5, decimal_places=2, null=True, blank=True)
    valor_iptu_pago = models.DecimalField(
        max_digits=5, decimal_places=2, null=True, blank=True)
    pagamento_parcial = models.DecimalField(
        max_digits=6, decimal_places=2, verbose_name='Valor pago até o momento',
        null=True, blank=True, default=0)
    deletado = models.NullBooleanField(null=True, blank=True, default=False)
    cliente = models.ForeignKey(Cliente, null=True)
    contrato_locacao = models.ForeignKey(
        ContratoLocacao, null=True, blank=True)
    valor_condominio_pago = models.DecimalField(
        max_digits=5, decimal_places=2, null=True, blank=True)
    conta_parcelas = models.CharField(
        null=True, blank=True, max_length=7,
        verbose_name=u'Contagem das parcelas')
    observacoes = models.TextField(null=True, blank=True)
    descricao_encargos = models.TextField(
        null=True, blank=True, verbose_name=u'Descrição de encargos')

    @property
    def total(self):
        """Calcula o total do título considerando juros,
             multa, cemig, condomínio,
             IPTU e o pagamento pagamento parcial
        """

        if self.dias_atraso == 0:
            total = self.valor + self.valor_cemig + \
                self.valor_copasa + self.valor_encargos

            if self.contrato_locacao:
                total += self.contrato_locacao.imovel.valor_condominio

           #     if self.contrato_locacao.imovel.iptu_vencido:
           #        total += self.contrato_locacao.imovel.valor_iptu

            if self.liquidado:
                total += self.valor_iptu_pago
        else:
            total = self.valor + self.valor_cemig + \
                self.valor_copasa + self.valor_encargos + \
                self.juros + self.multa

            if self.contrato_locacao:
                total += self.contrato_locacao.imovel.valor_condominio

            #    if self.contrato_locacao.imovel.iptu_vencido:
             #       total += self.contrato_locacao.imovel.valor_iptu

            if self.liquidado:
                total += self.valor_iptu_pago

        return total

    @property
    def valor_restante(self):
        return self.total - self.pagamento_parcial

    @property
    def juros(self):
        parametros = ParametrosGerais.objects.all()[0]

        if self.liquidado:
            if self.dias_atraso > 0:
                qtd_mes_atraso = calcula_meses_atraso(
                    self.vencimento, self.data_quitacao)
                juros = (
                    self.valor * pow((1 +
                        (self.perc_juros / 100)), qtd_mes_atraso)) - self.valor
                return juros
            else:
                return 0
        else:
            if self.dias_atraso > 0:
                qtd_mes_atraso = calcula_meses_atraso(self.vencimento, today)
                juros = (
                    self.valor * pow((1 +
                        (parametros.taxa_juros / 100)), qtd_mes_atraso)) -\
                    self.valor
                return juros
            else:
                return 0

    @property
    def multa(self):
        parametros = ParametrosGerais.objects.all()[0]

        if self.liquidado:
            if self.dias_atraso > 0:
                multa = (self.taxa_multa * self.valor) / 100
                return multa
            else:
                return 0
        else:
            if self.dias_atraso > 0:
                multa = (parametros.multa * self.valor) / 100
                return multa
            else:
                return 0

    @property
    def dias_atraso(self):
        data_carencia = date(
            self.vencimento.year, self.vencimento.month,
            self.vencimento.day + 5)

        if self.liquidado:
            if data_carencia < self.data_quitacao:
                return days_between(self.vencimento, self.data_quitacao)
            elif data_carencia > self.data_quitacao:
                return 0
            else:
                return 0
        else:
            if data_carencia < today:
                return days_between(self.vencimento, today)
            elif data_carencia > today:
                return 0
            else:
                return 0

    @property
    def liquidado(self):
        return True if self.data_quitacao else False

    class Meta:
        app_label = 'financeiro'
        verbose_name = 'Título'
        verbose_name_plural = 'Títulos'
        ordering = ['descricao']

    def __unicode__(self):
        return self.descricao[:20:] + self.vencimento.strftime('%d/%m/%y')\
            + ' ' + \
            str(self.pagamento_parcial) + '/' + str(
                self.valor) + ' ' + self.tipo

    def abater_valor(self, valor, IPTU_quitado=False, condominio_quitado=False):
        parametros = ParametrosGerais.objects.all()[0]

        self.data_quitacao = today
        if condominio_quitado:
            self.valor_condominio_pago =\
                self.contrato_locacao.imovel.valor_condominio
        else:
            self.valor_condominio_pago = 0

        if IPTU_quitado:
            self.valor_iptu_pago = self.contrato_locacao.imovel.valor_iptu
            self.contrato_locacao.imovel.data_last_pag_iptu = today
            self.contrato_locacao.imovel.vencimento_iptu = date(
                today.year + 1, today.month, today.day)
            self.contrato_locacao.imovel.save()
        else:
            self.contrato_locacao.imovel.data_last_pag_iptu = None
            self.valor_iptu_pago = 0
            self.contrato_locacao.imovel.save()

        self.pagamento_parcial = valor
        self.perc_juros = parametros.taxa_juros
        self.taxa_multa = parametros.multa
        self.save()

    @property
    def periodo(self):
        return date(
            self.vencimento.year, self.vencimento.month,
            self.vencimento.day)

    @property
    def total_por_extenso(self):
        total = self.total if self.total > 0 else self.total * -1
        centavos = (total - int(total)) * 100

        if centavos > 0:
            centavos = extenso(centavos)
            frase = extenso(total) + ' reais e ' + centavos + ' centavos'
        else:
            frase = extenso(total)
        return frase.capitalize()

    @property
    def get_descricao_encargos(self):
        return u'Descrição dos encargos\n' + self.descricao_encargos


class Recibo(models.Model):
    titulo = models.ForeignKey(Titulo)
    data_cadastro = models.DateTimeField(auto_now=True, auto_now_add=True)
    usuario = models.ForeignKey(User)
    descricao = models.TextField()

    def __unicode__(self):
        return u'Título:' + self.titulo.descricao + u' Usuário que emitiu:' +\
            self.usuario.username + u' na data:' + self.data_cadastro.strftime(
                '%m/%d/%y %H:%M:%S')

    class Meta:
        app_label = 'financeiro'
        verbose_name = 'Recibo'
        verbose_name_plural = 'Recibos'
