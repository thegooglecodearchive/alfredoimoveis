# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ContratoAdministrativo'
        db.create_table(u'imoveis_contratoadministrativo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('imovel', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['imoveis.Imovel'], unique=True)),
            ('inicio_contrato', self.gf('django.db.models.fields.DateField')()),
            ('termino_contrato', self.gf('django.db.models.fields.DateField')()),
            ('data_emissao_contrato', self.gf('django.db.models.fields.DateField')(auto_now=True, auto_now_add=True, blank=True)),
            ('empresa', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['empresas.Empresa'])),
        ))
        db.send_create_signal(u'imoveis', ['ContratoAdministrativo'])

        # Adding model 'LaudoVistoria'
        db.create_table(u'imoveis_laudovistoria', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('imovel', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['imoveis.Imovel'])),
            ('data_vistoria', self.gf('django.db.models.fields.DateField')()),
            ('pintura_interna', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('pintura_externa', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('ferragens', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('cores', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('tipo_tinta', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('lampadas_comuns', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('lustres', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('globos', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('lampadas_fluorecentes', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('lampiao', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('interruptores', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('luminarias', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('espelho_banheiro', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('campainha', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('ar_condicionado', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('instalacao', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('portao_eletronico', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('torneiras', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('chuveiro', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('vaso', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('lavatorio', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('tanque', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('bide', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('descarga', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('box', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('rede_esgoto', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('tacos', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('pisos', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('ceramico', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('paredes', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('azulejos', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('vidros', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('portas', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('fechaduras', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('trincos', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('janelas', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('muros', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('grades', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('telhado', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('forro', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('laje', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('portao', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('armarios', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('guarda_roupas', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('rede_protecao', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('chaves', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('observacao', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'imoveis', ['LaudoVistoria'])

        # Adding field 'Imovel.cod_ref_site'
        db.add_column(u'imoveis_imovel', 'cod_ref_site',
                      self.gf('django.db.models.fields.CharField')(max_length=120, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Imovel.tipo_imovel'
        db.add_column(u'imoveis_imovel', 'tipo_imovel',
                      self.gf('django.db.models.fields.CharField')(default='R', max_length=1),
                      keep_default=False)


        # Changing field 'Imovel.ultima_vistoria'
        db.alter_column(u'imoveis_imovel', 'ultima_vistoria', self.gf('django.db.models.fields.DateField')(null=True))
        # Adding field 'ContratoLocacao.observacao'
        db.add_column(u'imoveis_contratolocacao', 'observacao',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'ContratoAdministrativo'
        db.delete_table(u'imoveis_contratoadministrativo')

        # Deleting model 'LaudoVistoria'
        db.delete_table(u'imoveis_laudovistoria')

        # Deleting field 'Imovel.cod_ref_site'
        db.delete_column(u'imoveis_imovel', 'cod_ref_site')

        # Deleting field 'Imovel.tipo_imovel'
        db.delete_column(u'imoveis_imovel', 'tipo_imovel')


        # User chose to not deal with backwards NULL issues for 'Imovel.ultima_vistoria'
        raise RuntimeError("Cannot reverse this migration. 'Imovel.ultima_vistoria' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'Imovel.ultima_vistoria'
        db.alter_column(u'imoveis_imovel', 'ultima_vistoria', self.gf('django.db.models.fields.DateField')())
        # Deleting field 'ContratoLocacao.observacao'
        db.delete_column(u'imoveis_contratolocacao', 'observacao')


    models = {
        u'clientes.cliente': {
            'Meta': {'object_name': 'Cliente'},
            'ativo': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'celular': ('django.db.models.fields.CharField', [], {'max_length': '11', 'null': 'True', 'blank': 'True'}),
            'celular_2': ('django.db.models.fields.CharField', [], {'max_length': '11', 'null': 'True', 'blank': 'True'}),
            'cnpj_cpf': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'conjuge': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['clientes.Cliente']", 'null': 'True', 'blank': 'True'}),
            'data_cadastro': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'data_nascimento': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'empresa': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['empresas.Empresa']", 'null': 'True', 'blank': 'True'}),
            'empresa_socio': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'empresa_trabalha': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'end_empresa_socio': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'endereco': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'endereco_cli'", 'to': u"orm['enderecos.Endereco']"}),
            'estado_civil': ('django.db.models.fields.CharField', [], {'default': "'S'", 'max_length': '1'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nacionalidade': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'naturalidade': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['enderecos.Cidade']", 'null': 'True', 'blank': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'nome_mae': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'nome_pai': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'observacoes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'orgao_expeditor': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'profissao': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'referencias_bancarias': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'referencias_comerciais': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'renda': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '6', 'decimal_places': '2'}),
            'rg': ('django.db.models.fields.CharField', [], {'max_length': '11', 'null': 'True', 'blank': 'True'}),
            'socio_empresa': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'telefone_comercial': ('django.db.models.fields.CharField', [], {'max_length': '11', 'null': 'True', 'blank': 'True'}),
            'telefone_fixo': ('django.db.models.fields.CharField', [], {'max_length': '11', 'null': 'True', 'blank': 'True'}),
            'tipo_cliente': ('django.db.models.fields.CharField', [], {'default': "'C'", 'max_length': '1'}),
            'tipo_pessoa': ('django.db.models.fields.CharField', [], {'default': "'F'", 'max_length': '1'})
        },
        u'empresas.empresa': {
            'Meta': {'object_name': 'Empresa'},
            'ativo': ('django.db.models.fields.NullBooleanField', [], {'default': 'True', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        },
        u'enderecos.bairro': {
            'Meta': {'object_name': 'Bairro'},
            'cidade': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['enderecos.Cidade']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        },
        u'enderecos.cidade': {
            'Meta': {'object_name': 'Cidade'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'pais': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'uf': ('django.db.models.fields.CharField', [], {'max_length': '2'})
        },
        u'enderecos.endereco': {
            'Meta': {'object_name': 'Endereco'},
            'bairro': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'bairro'", 'null': 'True', 'to': u"orm['enderecos.Bairro']"}),
            'bairro_comercial': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'bairro_comercial'", 'null': 'True', 'to': u"orm['enderecos.Bairro']"}),
            'cep': ('django.db.models.fields.CharField', [], {'max_length': '9', 'null': 'True', 'blank': 'True'}),
            'cep_comercial': ('django.db.models.fields.CharField', [], {'max_length': '9', 'null': 'True', 'blank': 'True'}),
            'complemento': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'complemento_comercial': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'numero': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'numero_comercial': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'rua': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'rua_comercial': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'})
        },
        u'imoveis.contratoadministrativo': {
            'Meta': {'object_name': 'ContratoAdministrativo'},
            'data_emissao_contrato': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'empresa': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['empresas.Empresa']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imovel': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['imoveis.Imovel']", 'unique': 'True'}),
            'inicio_contrato': ('django.db.models.fields.DateField', [], {}),
            'termino_contrato': ('django.db.models.fields.DateField', [], {})
        },
        u'imoveis.contratolocacao': {
            'Meta': {'object_name': 'ContratoLocacao'},
            'data_emissao_contrato': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'empresa': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['empresas.Empresa']"}),
            'fiador1': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'fiador1_contrato'", 'to': u"orm['clientes.Cliente']"}),
            'fiador2': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'fiador2_contrato'", 'null': 'True', 'to': u"orm['clientes.Cliente']"}),
            'fiador3': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'fiador3_contrato'", 'null': 'True', 'to': u"orm['clientes.Cliente']"}),
            'gerou_receber': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imovel': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['imoveis.Imovel']", 'unique': 'True'}),
            'inicio_contrato': ('django.db.models.fields.DateField', [], {}),
            'locatario': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'locatario_contrato'", 'to': u"orm['clientes.Cliente']"}),
            'observacao': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'termino_contrato': ('django.db.models.fields.DateField', [], {}),
            'tipo_contrato': ('django.db.models.fields.CharField', [], {'max_length': '1'})
        },
        u'imoveis.imovel': {
            'Meta': {'object_name': 'Imovel'},
            'ativo': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'cod_ref_site': ('django.db.models.fields.CharField', [], {'max_length': '120', 'null': 'True', 'blank': 'True'}),
            'data_cadastro': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'descricao': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'empresa': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['empresas.Empresa']"}),
            'endereco': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['enderecos.Endereco']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'proprietario': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['clientes.Cliente']"}),
            'tipo_imovel': ('django.db.models.fields.CharField', [], {'default': "'R'", 'max_length': '1'}),
            'ultima_vistoria': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'valor_aluguel': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '2'}),
            'valor_iptu': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '2'})
        },
        u'imoveis.laudovistoria': {
            'Meta': {'object_name': 'LaudoVistoria'},
            'ar_condicionado': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'armarios': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'azulejos': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'bide': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'box': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'campainha': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'ceramico': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'chaves': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'chuveiro': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'cores': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'data_vistoria': ('django.db.models.fields.DateField', [], {}),
            'descarga': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'espelho_banheiro': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'fechaduras': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'ferragens': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'forro': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'globos': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'grades': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'guarda_roupas': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imovel': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['imoveis.Imovel']"}),
            'instalacao': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'interruptores': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'janelas': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'laje': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'lampadas_comuns': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'lampadas_fluorecentes': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'lampiao': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'lavatorio': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'luminarias': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'lustres': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'muros': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'observacao': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'paredes': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'pintura_externa': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'pintura_interna': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'pisos': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'portao': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'portao_eletronico': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'portas': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'rede_esgoto': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'rede_protecao': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'tacos': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'tanque': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'telhado': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'tipo_tinta': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'torneiras': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'trincos': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'vaso': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'vidros': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['imoveis']