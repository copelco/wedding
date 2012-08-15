# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Guest.comments'
        db.add_column('rsvp_guest', 'comments',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)

    def backwards(self, orm):
        # Deleting field 'Guest.comments'
        db.delete_column('rsvp_guest', 'comments')

    models = {
        'rsvp.guest': {
            'Meta': {'object_name': 'Guest'},
            'arrival_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2012, 11, 3, 0, 0)'}),
            'comments': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'date_submitted': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'party_size': ('django.db.models.fields.PositiveIntegerField', [], {'default': '2'})
        }
    }

    complete_apps = ['rsvp']