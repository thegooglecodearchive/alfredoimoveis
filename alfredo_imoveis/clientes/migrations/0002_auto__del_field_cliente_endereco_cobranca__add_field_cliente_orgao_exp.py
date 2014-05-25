# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Cliente.endereco_cobranca'
        db.delete_column(u'clientes_cliente', 'endereco_cobranca_id')

        # Adding field 'Cliente.orgao_expeditor'
        db.add_column(u'clientes_cliente', 'orgao_expeditor',
                      self.gf('django.db.models.fields.CharField')(max_length=5, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Cliente.filiacao'
        db.add_column(u'clientes_cliente', 'filiacao',
                      self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Cliente.nacionalidade'
        db.add_column(u'clientes_cliente', 'nacionalidade',
                      self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Cliente.naturalidade'
        db.add_column(u'clientes_cliente', 'naturalidade',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['enderecos.Cidade']),
                      keep_default=False)

        # Adding field 'Cliente.endereco_comercial'
        db.add_column(u'clientes_cliente', 'endereco_comercial',
                      self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='endereco_obra', null=True, to=orm['enderecos.Endereco']),
                      keep_default=False)

        # Adding field 'Cliente.data_nascimento'
        db.add_column(u'clientes_cliente', 'data_nascimento',
                      self.gf('django.db.models.fields.DateField')(auto_now_add=True, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Cliente.estado_civil'
        db.add_column(u'clientes_cliente', 'estado_civil',
                      self.gf('django.db.models.fields.CharField')(default='S', max_length=1),
                      keep_default=False)

        # Adding field 'Cliente.profissao'
        db.add_column(u'clientes_cliente', 'profissao',
                      self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Cliente.empresa_trabalha'
        db.add_column(u'clientes_cliente', 'empresa_trabalha',
                      self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Cliente.renda'
        db.add_column(u'clientes_cliente', 'renda',
                      self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=5, decimal_places=2),
                      keep_default=False)

        # Adding field 'Cliente.socio_empresa'
        db.add_column(u'clientes_cliente', 'socio_empresa',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Cliente.empresa_socio'
        db.add_column(u'clientes_cliente', 'empresa_socio',
                      self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Cliente.end_empresa_socio'
        db.add_column(u'clientes_cliente', 'end_empresa_socio',
                      self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Cliente.endereco_cobranca'
        db.add_column(u'clientes_cliente', 'endereco_cobranca',
                      self.gf('django.db.models.fields.related.ForeignKey')(related_name='endereco_obra', null=True, to=orm['enderecos.Endereco'], blank=True),
                      keep_default=False)

        # Deleting field 'Cliente.orgao_expeditor'
        db.delete_column(u'clientes_cliente', 'orgao_expeditor')

        # Deleting field 'Cliente.filiacao'
        db.delete_column(u'clientes_cliente', 'filiacao')

        # Deleting field 'Cliente.nacionalidade'
        db.delete_column(u'clientes_cliente', 'nacionalidade')

        # Deleting field 'Cliente.naturalidade'
        db.delete_column(u'clientes_cliente', 'naturalidade_id')

        # Deleting field 'Cliente.endereco_comercial'
        db.delete_column(u'clientes_cliente', 'endereco_comercial_id')

        # Deleting field 'Cliente.data_nascimento'
        db.delete_column(u'clientes_cliente', 'data_nascimento')

        # Deleting field 'Cliente.estado_civil'
        db.delete_column(u'clientes_cliente', 'estado_civil')

        # Deleting field 'Cliente.profissao'
        db.delete_column(u'clientes_cliente', 'profissao')

        # Deleting field 'Cliente.empresa_trabalha'
        db.delete_column(u'clientes_cliente', 'empresa_trabalha')

        # Deleting field 'Cliente.renda'
        db.delete_column(u'clientes_cliente', 'renda')

        # Deleting field 'Cliente.socio_empresa'
        db.delete_column(u'clientes_cliente', 'socio_empresa')

        # Deleting field 'Cliente.empresa_socio'
        db.delete_column(u'clientes_cliente', 'empresa_socio')

        # Deleting field 'Cliente.end_empresa_socio'
        db.delete_column(u'clientes_cliente', 'end_empresa_socio')


    models = {
        u'clientes.cliente': {
            'Meta': {'object_name': 'Cliente'},
            'ativo': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'cnpj_cpf': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'data_cadastro': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'data_nascimento': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True'}),
            'empresa': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['empresas.Empresa']"}),
            'empresa_socio': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'empresa_trabalha': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'end_empresa_socio': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'endereco': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'endereco_cli'", 'to': u"orm['enderecos.Endereco']"}),
            'endereco_comercial': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'endereco_obra'", 'null': 'True', 'to': u"orm['enderecos.Endereco']"}),
            'estado_civil': ('django.db.models.fields.CharField', [], {'default': "'S'", 'max_length': '1'}),
            'filiacao': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nacionalidade': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'naturalidade': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['enderecos.Cidade']"}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'orgao_expeditor': ('django.db.models.fields.CharField', [], {'max_length': '5', 'null': 'True', 'blank': 'True'}),
            'profissao': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'renda': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '5', 'decimal_places': '2'}),
            'rg': ('django.db.models.fields.CharField', [], {'max_length': '11', 'null': 'True', 'blank': 'True'}),
            'socio_empresa': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
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
        }
    }

    complete_apps = ['clientes']