# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Cliente'
        db.create_table(u'clientes_cliente', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('cnpj_cpf', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('rg', self.gf('django.db.models.fields.CharField')(max_length=11, null=True, blank=True)),
            ('endereco', self.gf('django.db.models.fields.related.ForeignKey')(related_name='endereco_cli', to=orm['enderecos.Endereco'])),
            ('endereco_cobranca', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='endereco_obra', null=True, to=orm['enderecos.Endereco'])),
            ('empresa', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['empresas.Empresa'])),
            ('ativo', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('data_cadastro', self.gf('django.db.models.fields.DateField')(auto_now_add=True, null=True, blank=True)),
            ('telefone', self.gf('django.db.models.fields.CharField')(default='0', max_length=11)),
            ('telefone2', self.gf('django.db.models.fields.CharField')(default='0', max_length=11)),
            ('telefone3', self.gf('django.db.models.fields.CharField')(default='0', max_length=11)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, null=True)),
            ('tipo_cliente', self.gf('django.db.models.fields.CharField')(default='C', max_length=1)),
        ))
        db.send_create_signal(u'clientes', ['Cliente'])


    def backwards(self, orm):
        # Deleting model 'Cliente'
        db.delete_table(u'clientes_cliente')


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
        }
    }

    complete_apps = ['clientes']