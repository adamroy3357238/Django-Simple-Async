# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Group.final'
        db.add_column('async_group', 'final',
                      self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='ends', null=True, to=orm['async.Job']),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Group.final'
        db.delete_column('async_group', 'final_id')


    models = {
        'async.error': {
            'Meta': {'object_name': 'Error'},
            'exception': ('django.db.models.fields.TextField', [], {}),
            'executed': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'job': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'errors'", 'to': "orm['async.Job']"}),
            'traceback': ('django.db.models.fields.TextField', [], {})
        },
        'async.group': {
            'Meta': {'object_name': 'Group'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'final': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'ends'", 'null': 'True', 'to': "orm['async.Job']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'reference': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'async.job': {
            'Meta': {'object_name': 'Job'},
            'added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'args': ('django.db.models.fields.TextField', [], {}),
            'cancelled': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'executed': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'group': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'jobs'", 'null': 'True', 'to': "orm['async.Group']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'identity': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_index': 'True'}),
            'kwargs': ('django.db.models.fields.TextField', [], {}),
            'meta': ('django.db.models.fields.TextField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'priority': ('django.db.models.fields.IntegerField', [], {}),
            'result': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'scheduled': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'started': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['async']