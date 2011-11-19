# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Pixel.x'
        db.add_column('pixel_pixel', 'x', self.gf('django.db.models.fields.PositiveIntegerField')(default=0), keep_default=False)

        # Adding field 'Pixel.y'
        db.add_column('pixel_pixel', 'y', self.gf('django.db.models.fields.PositiveIntegerField')(default=0), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Pixel.x'
        db.delete_column('pixel_pixel', 'x')

        # Deleting field 'Pixel.y'
        db.delete_column('pixel_pixel', 'y')


    models = {
        'pixel.pixel': {
            'Meta': {'object_name': 'Pixel'},
            'b': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'g': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image1': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'pos': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'r': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'x': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'y': ('django.db.models.fields.PositiveIntegerField', [], {})
        },
        'pixel.userimage': {
            'Meta': {'object_name': 'UserImage'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pixels': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['pixel.Pixel']", 'symmetrical': 'False'})
        }
    }

    complete_apps = ['pixel']
