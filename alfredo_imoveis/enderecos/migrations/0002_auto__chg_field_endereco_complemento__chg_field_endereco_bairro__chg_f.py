# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Endereco.complemento'
        db.alter_column(u'enderecos_endereco', 'complemento', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

        # Changing field 'Endereco.bairro'
        db.alter_column(u'enderecos_endereco', 'bairro_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['enderecos.Bairro'], null=True))

        # Changing field 'Endereco.rua'
        db.alter_column(u'enderecos_endereco', 'rua', self.gf('django.db.models.fields.CharField')(max_length=150, null=True))

        # Changing field 'Endereco.numero'
        db.alter_column(u'enderecos_endereco', 'numero', self.gf('django.db.models.fields.IntegerField')(null=True))

    def backwards(self, orm):

        # Changing field 'Endereco.complemento'
        db.alter_column(u'enderecos_endereco', 'complemento', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'Endereco.bairro'
        db.alter_column(u'enderecos_endereco', 'bairro_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['enderecos.Bairro']))

        # User chose to not deal with backwards NULL issues for 'Endereco.rua'
        raise RuntimeError("Cannot reverse this migration. 'Endereco.rua' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'Endereco.rua'
        db.alter_column(u'enderecos_endereco', 'rua', self.gf('django.db.models.fields.CharField')(max_length=150))

        # User chose to not deal with backwards NULL issues for 'Endereco.numero'
        raise RuntimeError("Cannot reverse this migration. 'Endereco.numero' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'Endereco.numero'
        db.alter_column(u'enderecos_endereco', 'numero', self.gf('django.db.models.fields.IntegerField')())

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
            'bairro': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['enderecos.Bairro']", 'null': 'True', 'blank': 'True'}),
            'cep': ('django.db.models.fields.CharField', [], {'max_length': '9', 'null': 'True', 'blank': 'True'}),
            'complemento': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'numero': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'rua': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['enderecos']