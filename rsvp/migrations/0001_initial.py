# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Guest'
        db.create_table('rsvp_guest', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('party_size', self.gf('django.db.models.fields.PositiveIntegerField')(default=1)),
            ('arrival_date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2012, 11, 3, 0, 0))),
            ('date_submitted', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('rsvp', ['Guest'])

    def backwards(self, orm):
        # Deleting model 'Guest'
        db.delete_table('rsvp_guest')

    models = {
        'rsvp.guest': {
            'Meta': {'object_name': 'Guest'},
            'arrival_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 11, 3, 0, 0)'}),
            'date_submitted': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'party_size': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1'})
        }
    }

    complete_apps = ['rsvp']
