# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Imovel'
        db.create_table(u'imoveis_imovel', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('endereco', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['enderecos.Endereco'])),
            ('descricao', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('valor_iptu', self.gf('django.db.models.fields.DecimalField')(max_digits=6, decimal_places=2)),
            ('valor_aluguel', self.gf('django.db.models.fields.DecimalField')(max_digits=6, decimal_places=2)),
            ('ultima_vistoria', self.gf('django.db.models.fields.DateField')()),
            ('data_cadastro', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('proprietario', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['clientes.Cliente'])),
            ('empresa', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['empresas.Empresa'])),
            ('ativo', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'imoveis', ['Imovel'])

        # Adding model 'ContratoLocacao'
        db.create_table(u'imoveis_contratolocacao', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('imovel', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['imoveis.Imovel'], unique=True)),
            ('inicio_contrato', self.gf('django.db.models.fields.DateField')()),
            ('termino_contrato', self.gf('django.db.models.fields.DateField')()),
            ('data_emissao_contrato', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('locatario', self.gf('django.db.models.fields.related.ForeignKey')(related_name='locatario_contrato', to=orm['clientes.Cliente'])),
            ('fiador1', self.gf('django.db.models.fields.related.ForeignKey')(related_name='fiador1_contrato', to=orm['clientes.Cliente'])),
            ('fiador2', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='fiador2_contrato', null=True, to=orm['clientes.Cliente'])),
            ('fiador3', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='fiador3_contrato', null=True, to=orm['clientes.Cliente'])),
            ('empresa', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['empresas.Empresa'])),
            ('tipo_contrato', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('gerou_receber', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'imoveis', ['ContratoLocacao'])


    def backwards(self, orm):
        # Deleting model 'Imovel'
        db.delete_table(u'imoveis_imovel')

        # Deleting model 'ContratoLocacao'
        db.delete_table(u'imoveis_contratolocacao')


    models = {
        u'clientes.cliente': {
            'Meta': {'object_name': 'Cliente'},
            'ativo': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'cnpj_cpf': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'data_cadastro': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True'}),
            'empresa': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['empresas.Empresa']"}),
            'endereco': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'endereco_cli'", 'to': u"orm['enderecos.Endereco']"}),
            'endereco_cobranca': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'endereco_obra'", 'null': 'True', 'to': u"orm['enderecos.Endereco']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'rg': ('django.db.models.fields.CharField', [], {'max_length': '11', 'null': 'True', 'blank': 'True'}),
            'telefone': ('django.db.models.fields.CharField', [], {'default': "'0'", 'max_length': '11'}),
            'telefone2': ('django.db.models.fields.CharField', [], {'default': "'0'", 'max_length': '11'}),
            'telefone3': ('django.db.models.fields.CharField', [], {'default': "'0'", 'max_length': '11'}),
            'tipo_cliente': ('django.db.models.fields.CharField', [], {'default': "'C'", 'max_length': '1'})
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
            'bairro': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['enderecos.Bairro']"}),
            'cep': ('django.db.models.fields.CharField', [], {'max_length': '9', 'null': 'True', 'blank': 'True'}),
            'complemento': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'numero': ('django.db.models.fields.IntegerField', [], {}),
            'rua': ('django.db.models.fields.CharField', [], {'max_length': '150'})
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
            'termino_contrato': ('django.db.models.fields.DateField', [], {}),
            'tipo_contrato': ('django.db.models.fields.CharField', [], {'max_length': '1'})
        },
        u'imoveis.imovel': {
            'Meta': {'object_name': 'Imovel'},
            'ativo': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'data_cadastro': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'descricao': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'empresa': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['empresas.Empresa']"}),
            'endereco': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['enderecos.Endereco']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'proprietario': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['clientes.Cliente']"}),
            'ultima_vistoria': ('django.db.models.fields.DateField', [], {}),
            'valor_aluguel': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '2'}),
            'valor_iptu': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '2'})
        }
    }

    complete_apps = ['imoveis']