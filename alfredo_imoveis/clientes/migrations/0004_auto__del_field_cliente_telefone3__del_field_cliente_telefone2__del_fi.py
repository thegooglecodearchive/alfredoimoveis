# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Cliente.telefone3'
        db.delete_column(u'clientes_cliente', 'telefone3')

        # Deleting field 'Cliente.telefone2'
        db.delete_column(u'clientes_cliente', 'telefone2')

        # Deleting field 'Cliente.telefone'
        db.delete_column(u'clientes_cliente', 'telefone')

        # Adding field 'Cliente.telefone_fixo'
        db.add_column(u'clientes_cliente', 'telefone_fixo',
                      self.gf('django.db.models.fields.CharField')(max_length=11, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Cliente.telefone_comercial'
        db.add_column(u'clientes_cliente', 'telefone_comercial',
                      self.gf('django.db.models.fields.CharField')(max_length=11, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Cliente.celular'
        db.add_column(u'clientes_cliente', 'celular',
                      self.gf('django.db.models.fields.CharField')(max_length=11, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Cliente.celular_2'
        db.add_column(u'clientes_cliente', 'celular_2',
                      self.gf('django.db.models.fields.CharField')(max_length=11, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Cliente.telefone3'
        db.add_column(u'clientes_cliente', 'telefone3',
                      self.gf('django.db.models.fields.CharField')(default='0', max_length=11),
                      keep_default=False)

        # Adding field 'Cliente.telefone2'
        db.add_column(u'clientes_cliente', 'telefone2',
                      self.gf('django.db.models.fields.CharField')(default='0', max_length=11),
                      keep_default=False)

        # Adding field 'Cliente.telefone'
        db.add_column(u'clientes_cliente', 'telefone',
                      self.gf('django.db.models.fields.CharField')(default='0', max_length=11),
                      keep_default=False)

        # Deleting field 'Cliente.telefone_fixo'
        db.delete_column(u'clientes_cliente', 'telefone_fixo')

        # Deleting field 'Cliente.telefone_comercial'
        db.delete_column(u'clientes_cliente', 'telefone_comercial')

        # Deleting field 'Cliente.celular'
        db.delete_column(u'clientes_cliente', 'celular')

        # Deleting field 'Cliente.celular_2'
        db.delete_column(u'clientes_cliente', 'celular_2')


    models = {
        u'clientes.cliente': {
            'Meta': {'object_name': 'Cliente'},
            'ativo': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'celular': ('django.db.models.fields.CharField', [], {'max_length': '11', 'null': 'True', 'blank': 'True'}),
            'celular_2': ('django.db.models.fields.CharField', [], {'max_length': '11', 'null': 'True', 'blank': 'True'}),
            'cnpj_cpf': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'data_cadastro': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'data_nascimento': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True'}),
            'empresa': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['empresas.Empresa']"}),
            'empresa_socio': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'empresa_trabalha': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'end_empresa_socio': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'endereco': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'endereco_cli'", 'to': u"orm['enderecos.Endereco']"}),
            'endereco_comercial': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'endereco_comercial'", 'null': 'True', 'to': u"orm['enderecos.Endereco']"}),
            'estado_civil': ('django.db.models.fields.CharField', [], {'default': "'S'", 'max_length': '1'}),
            'filiacao': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nacionalidade': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'naturalidade': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['enderecos.Cidade']"}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'orgao_expeditor': ('django.db.models.fields.CharField', [], {'max_length': '5', 'null': 'True', 'blank': 'True'}),
            'profissao': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'renda': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '6', 'decimal_places': '2'}),
            'rg': ('django.db.models.fields.CharField', [], {'max_length': '11', 'null': 'True', 'blank': 'True'}),
            'socio_empresa': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'telefone_comercial': ('django.db.models.fields.CharField', [], {'max_length': '11', 'null': 'True', 'blank': 'True'}),
            'telefone_fixo': ('django.db.models.fields.CharField', [], {'max_length': '11', 'null': 'True', 'blank': 'True'}),
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
            'bairro': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['enderecos.Bairro']", 'null': 'True', 'blank': 'True'}),
            'cep': ('django.db.models.fields.CharField', [], {'max_length': '9', 'null': 'True', 'blank': 'True'}),
            'complemento': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'numero': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'rua': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['clientes']