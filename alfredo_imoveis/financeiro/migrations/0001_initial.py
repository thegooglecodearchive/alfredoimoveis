# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ContaCaixa'
        db.create_table(u'financeiro_contacaixa', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('descricao', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('conta_caixa_superior', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['financeiro.ContaCaixa'], null=True, blank=True)),
            ('empresa', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['empresas.Empresa'])),
        ))
        db.send_create_signal('financeiro', ['ContaCaixa'])

        # Adding model 'Titulo'
        db.create_table(u'financeiro_titulo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('descricao', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('conta_caixa', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['financeiro.ContaCaixa'], null=True, blank=True)),
            ('empresa', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['empresas.Empresa'])),
            ('data_cadastro', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('vencimento', self.gf('django.db.models.fields.DateField')()),
            ('tipo', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('usuario_cadastrou', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('valor', self.gf('django.db.models.fields.DecimalField')(max_digits=6, decimal_places=2)),
            ('pagamento_parcial', self.gf('django.db.models.fields.DecimalField')(default=0, null=True, max_digits=6, decimal_places=2, blank=True)),
            ('deletado', self.gf('django.db.models.fields.NullBooleanField')(default=False, null=True, blank=True)),
            ('cliente', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['clientes.Cliente'], null=True)),
            ('contrato_locacao', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['imoveis.ContratoLocacao'], null=True)),
        ))
        db.send_create_signal('financeiro', ['Titulo'])


    def backwards(self, orm):
        # Deleting model 'ContaCaixa'
        db.delete_table(u'financeiro_contacaixa')

        # Deleting model 'Titulo'
        db.delete_table(u'financeiro_titulo')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
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
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
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
        'financeiro.contacaixa': {
            'Meta': {'object_name': 'ContaCaixa'},
            'conta_caixa_superior': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['financeiro.ContaCaixa']", 'null': 'True', 'blank': 'True'}),
            'descricao': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'empresa': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['empresas.Empresa']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'financeiro.titulo': {
            'Meta': {'object_name': 'Titulo'},
            'cliente': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['clientes.Cliente']", 'null': 'True'}),
            'conta_caixa': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['financeiro.ContaCaixa']", 'null': 'True', 'blank': 'True'}),
            'contrato_locacao': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['imoveis.ContratoLocacao']", 'null': 'True'}),
            'data_cadastro': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'deletado': ('django.db.models.fields.NullBooleanField', [], {'default': 'False', 'null': 'True', 'blank': 'True'}),
            'descricao': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'empresa': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['empresas.Empresa']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pagamento_parcial': ('django.db.models.fields.DecimalField', [], {'default': '0', 'null': 'True', 'max_digits': '6', 'decimal_places': '2', 'blank': 'True'}),
            'tipo': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'usuario_cadastrou': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'valor': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '2'}),
            'vencimento': ('django.db.models.fields.DateField', [], {})
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

    complete_apps = ['financeiro']