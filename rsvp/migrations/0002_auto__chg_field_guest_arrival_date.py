# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Guest.arrival_date'
        db.alter_column('rsvp_guest', 'arrival_date', self.gf('django.db.models.fields.DateField')())
    def backwards(self, orm):

        # Changing field 'Guest.arrival_date'
        db.alter_column('rsvp_guest', 'arrival_date', self.gf('django.db.models.fields.DateTimeField')())
    models = {
        'rsvp.guest': {
            'Meta': {'object_name': 'Guest'},
            'arrival_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2012, 11, 3, 0, 0)'}),
            'date_submitted': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'party_size': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1'})
        }
    }

    complete_apps = ['rsvp']