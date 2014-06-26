# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Endereco.bairro'
        db.alter_column(u'enderecos_endereco', 'bairro_id', self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['enderecos.Bairro']))

        # Changing field 'Endereco.rua'
        db.alter_column(u'enderecos_endereco', 'rua', self.gf('django.db.models.fields.CharField')(default='', max_length=150))

        # Changing field 'Endereco.cep'
        db.alter_column(u'enderecos_endereco', 'cep', self.gf('django.db.models.fields.CharField')(default='', max_length=9))

    def backwards(self, orm):

        # Changing field 'Endereco.bairro'
        db.alter_column(u'enderecos_endereco', 'bairro_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['enderecos.Bairro']))

        # Changing field 'Endereco.rua'
        db.alter_column(u'enderecos_endereco', 'rua', self.gf('django.db.models.fields.CharField')(max_length=150, null=True))

        # Changing field 'Endereco.cep'
        db.alter_column(u'enderecos_endereco', 'cep', self.gf('django.db.models.fields.CharField')(max_length=9, null=True))

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
            'bairro': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'bairro'", 'to': u"orm['enderecos.Bairro']"}),
            'bairro_comercial': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'bairro_comercial'", 'null': 'True', 'to': u"orm['enderecos.Bairro']"}),
            'cep': ('django.db.models.fields.CharField', [], {'max_length': '9'}),
            'cep_comercial': ('django.db.models.fields.CharField', [], {'max_length': '9', 'null': 'True', 'blank': 'True'}),
            'complemento': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'complemento_comercial': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'numero': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'numero_comercial': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'rua': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'rua_comercial': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['enderecos']