# -*- encoding: utf-8 -*-
from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=128, default=u'Inscrição AndroidConf 2011')
    slug = models.SlugField(max_length=128,  default=u'androidconf-2011')
    price = models.PositiveIntegerField(default=100)

    def __unicode__(self):
        return self.title

    class Admin:
        list_display   = ('title', 'slug', 'price')
        list_filter    = ('title',)
        ordering       = ('-price',)
        search_fields  = ('title',)

