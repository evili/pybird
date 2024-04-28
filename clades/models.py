# -*- coding: utf-8 -*-
"""Clades groups and classifies living beings into several
   hierarchical categories:
     kingdom, phylum, class, order, family, genus, and species.
"""
from pybird.models import BaseObject, BaseNamed
from django.db import models
from django.utils.translation import get_language
from pycountry import languages
from django.conf import settings

LANG_CHOICES = []

for ln in languages:
    lng = dict(ln)
    if 'alpha_2' in lng:
        LANG_CHOICES += (lng['alpha_2'], lng['name'].split(';')[0]),


class Kingdom(BaseNamed):
    """Kingdom is a taxonomic rank, which is either the highest rank or in
    the more recent three-domain system, the rank below domain. Kingdoms
    are divided into smaller groups called phyla (in zoology) or divisions
    in botany."""
    pass


class Phylum(BaseNamed):
    """Phylum is a taxonomic rank below kingdom and above class. Traditionally,
    in botany the term division is used instead of phylum"""
    kingdom = models.ForeignKey(Kingdom, on_delete=models.PROTECT)

    class Meta:
        verbose_name_plural = 'phyla'


class Classe(BaseNamed):
    """Classis is a taxonomic rank fitting between phylum and order."""
    phylum = models.ForeignKey(Phylum, on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'classi'
        verbose_name_plural = 'classi'


class Order(BaseNamed):
    """Order is a taxonomic rank  fitting between classis and family."""
    classe = models.ForeignKey(Classe, on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'ordo'
        verbose_name_plural = 'ordines'


class Family(BaseNamed):
    """Family is a taxonomic rank fitting between order and genus."""
    order = models.ForeignKey(Order, on_delete=models.PROTECT)

    class Meta:
        verbose_name_plural = 'families'


class Genus(BaseNamed):
    """Genus is a taxonomic rank fitting between family and scpecies.The
    scientific name of a genus may be called the generic name or generic
    epithet: it is always capitalized. It plays a pivotal role in binomial
    nomenclature, the system of biological nomenclature."""
    family = models.ForeignKey(Family, on_delete=models.PROTECT)

    class Meta:
        verbose_name_plural = 'genera'


class Species(BaseNamed):
    """Species s one of the basic units of biological classification and a
    taxonomic rank. A species is often defined as a group of organisms capable
    of interbreeding and producing fertile offspring."""
    genus = models.ForeignKey(Genus, on_delete=models.PROTECT)

    def sci_name(self):
        return self.genus.name.capitalize() + u' ' + self.name.lower()

    def __unicode__(self):
        cn = self.sci_name()
        try:
            loc = get_language()
        except ValueError:
            loc = settings.LANGUAGE_CODE
        loc = loc.replace('-', '_')
        lang = loc.split('_')[0]
        try:
            cn = self.commonname_set.get(locale=lang).cname
        except ValueError:
            pass

        return cn

    class Meta:
        verbose_name_plural = 'species'


class CommonName(BaseObject):
    cname = models.CharField(max_length=127)
    species = models.ForeignKey(Species, on_delete=models.PROTECT)
    locale = models.CharField(max_length=15, choices=LANG_CHOICES)

    def __unicode__(self):
        return u'{0} ({1})'.format(self.cname, self.species.sci_name())

    class Meta:
        ordering = ['locale', 'species', 'cname']
