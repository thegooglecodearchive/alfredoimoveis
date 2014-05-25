# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Endereco.rua_comercial'
        db.add_column(u'enderecos_endereco', 'rua_comercial',
                      self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Endereco.numero_comercial'
        db.add_column(u'enderecos_endereco', 'numero_comercial',
                      self.gf('django.db.models.fields.IntegerField')(default=0, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Endereco.bairro_comercial'
        db.add_column(u'enderecos_endereco', 'bairro_comercial',
                      self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='bairro_comercial', null=True, to=orm['enderecos.Bairro']),
                      keep_default=False)

        # Adding field 'Endereco.cep_comercial'
        db.add_column(u'enderecos_endereco', 'cep_comercial',
                      self.gf('django.db.models.fields.CharField')(max_length=9, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Endereco.complemento_comercial'
        db.add_column(u'enderecos_endereco', 'complemento_comercial',
                      self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Endereco.rua_comercial'
        db.delete_column(u'enderecos_endereco', 'rua_comercial')

        # Deleting field 'Endereco.numero_comercial'
        db.delete_column(u'enderecos_endereco', 'numero_comercial')

        # Deleting field 'Endereco.bairro_comercial'
        db.delete_column(u'enderecos_endereco', 'bairro_comercial_id')

        # Deleting field 'Endereco.cep_comercial'
        db.delete_column(u'enderecos_endereco', 'cep_comercial')

        # Deleting field 'Endereco.complemento_comercial'
        db.delete_column(u'enderecos_endereco', 'complemento_comercial')


    models = {
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
        }
    }

    complete_apps = ['enderecos']