from django.db import models
from django.core import validators


class Parzelle(models.Model):
    code = models.CharField(u'Code', max_length=100, validators=[validators.validate_slug], unique=True)
    name = models.CharField(u'Name', max_length=100, unique=True)
    
    class Meta:
        verbose_name = u'Parzelle'
        verbose_name_plural = u'Parzellen'
        
class Duengungsstufe(models.Model):
    name = models.CharField(u'Name', max_length=100, unique=True)
    
    class Meta:
        verbose_name = u'Duengungsstufe'
        verbose_name_plural = u'Duengungsstufe'
        
class Duenger(models.Model):
    name = models.CharField(u'Name', max_length=100, unique=True)
    
    class Meta:
        verbose_name = u'Duenger'
        verbose_name_plural = u'Duenger'
        
class Familie(models.Model):
    name = models.CharField(u'Name', max_length=100, unique=True)
    
    class Meta:
        verbose_name = u'Familie'
        verbose_name_plural = u'Familien'
        
class Kultur(models.Model):
    name = models.CharField(u'Name', max_length=100, unique=True)
    familie = models.ForeignKey(Familie, related_name='kulturen', null=False, blank=False,
                                 on_delete=models.PROTECT)
    
    class Meta:
        verbose_name = u'Kultur'
        verbose_name_plural = u'Kulturen'

class Satz(models.Model):
    nummer = models.IntegerField(u'Nummer')
    kultur = models.ForeignKey(Kultur, related_name='saetze', null=False, blank=False,
                                 on_delete=models.PROTECT)
    sorte = models.CharField(u'Sorte', max_length=200)
    duengungsstufe = models.ForeignKey(Duengungsstufe, related_name='saetze', null=False, blank=False,
                                 on_delete=models.PROTECT)
    duenger = models.ForeignKey(Duenger, related_name='saetze', null=False, blank=False,
                                 on_delete=models.PROTECT)
    parzelle = models.ForeignKey(Parzelle, related_name='saetze', null=False, blank=False,
                                 on_delete=models.PROTECT)
    anzucht = models.IntegerField(u'Anzucht',null=True,blank=True)
    g_pro_tausend = models.FloatField(u'g/1000 Pflanzen',null=True,blank=True)
    anzahl_anzucht = models.IntegerField(u'Anz. Anzucht',null=True,blank=True)
    setzen = models.IntegerField(u'Setzen',null=True,blank=True)
    g_pro_aare = models.IntegerField(u'g/Are',null=True,blank=True)
    saat = models.IntegerField(u'Saat',null=True,blank=True)
    erste_ernte = models.IntegerField(u'1. Ernte',null=True,blank=True)
    ernteschluss = models.IntegerField(u'Ernteschluss',null=True,blank=True)
    duenger_kg = models.CharField(u'Duenger kg 10N', max_length=100,null=True,blank=True)
    beet_breite = models.FloatField(u'g/1000 Pflanzen',null=True,blank=True)
    reihen_abstand = models.IntegerField(u'Reihenabstand',null=True,blank=True)
    pflanz_abstand = models.IntegerField(u'Pflanzabstand',null=True,blank=True)
    ertrag_erwartung = models.CharField(u'Ertrag kg/m2', max_length=100,null=True,blank=True)
    bemerkung = models.TextField(u'Allg. Bemerkungen', max_length=1000, null=True,blank=True)
    bem_anzucht = models.TextField(u'Bem.  Anzucht', max_length=1000, null=True,blank=True)
    bem_setzen = models.TextField(u'Bem. Setzen', max_length=1000, null=True,blank=True)
    bem_saat = models.TextField(u'Bem. Direktsaat', max_length=1000, null=True,blank=True)
    
    class Meta:
        verbose_name = u'Satz'
        verbose_name_plural = u'Saetze'
    
    
    
    
    