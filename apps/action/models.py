#coding: utf-8

from django.db import models
from django.utils.translation import ugettext_lazy as _


class Action(models.Model):
    title = models.CharField(_(u'Acao'), max_length=200)
    description = models.TextField(_(u'Descrição'))
    date = models.DateField(_(u'Data'))
    due_to = models.DateField(_(u'Data Final'), blank=True, null=True)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = u'Ação'
        verbose_name_plural = u'Ações'


class Venue(models.Model):
    action = models.ForeignKey(Action, related_name='venues')
    address = models.CharField(
        _(u'Logradouro'), max_length=300, blank=True, null=True)
    number = models.IntegerField(blank=True, null=True)
    district = models.CharField(
        _(u'Bairro'), max_length=200)
    city = models.CharField(
        _(u'Cidade'), max_length=200)
    state = models.CharField(
        _(u'Estado'), max_length=200)
    latitude = models.CharField(
        _(u'latitude'), max_length=20, blank=True, null=True)
    longitude = models.CharField(
        _(u'longitude'), max_length=20, blank=True, null=True)

    #TODO: function to get latitude and longitude.
    def __unicode__(self):

        return '{0}: {1} - {2}'.format(
            self.action,
            self.address,
            self.number or 's/n')
