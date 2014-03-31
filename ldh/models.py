from django.db import models
from django.utils.translation import ugettext_lazy as _

COLOR_CHOICES = (('default', _('Default')),
                 ('primary', _('Primary')),
                 ('success', _('Success')),
                 ('info', _('Info')),
                 ('warning', _('Warning')),
                 ('danger', _('Danger')))

class Title(models.Model):

    key = models.CharField(verbose_name=_(u'key'),
                           max_length=100,
                           db_index=True)
    text = models.CharField(verbose_name=_(u'Text'),
                            max_length=100)

    class Meta:
        verbose_name = _('Title')
        verbose_name_plural = _('Titles')

    def __str__(self):
        return self.text

    def __unicode__(self):
        return self.text



class Chunk(models.Model):

    key = models.CharField(verbose_name=_(u'key'),
                           max_length=100,
                           db_index=True)
    text = models.TextField(verbose_name=_(u'Text'))

    class Meta:
        verbose_name = _('Chunk')
        verbose_name_plural = _('Chunks')

    def __str__(self):
        return self.text

    def __unicode__(self):
        return self.text


class Alert(models.Model):

    alert_type = models.CharField(verbose_name=_(u'Alert type'),
                                  choices=COLOR_CHOICES,
                                  max_length=10)
    msg = models.TextField(verbose_name=_(u'Msg'))

    class Meta:
        verbose_name = _('Alert')
        verbose_name_plural = _('Alerts')

    def __str__(self):
        return self.msg

    def __unicode__(self):
        return self.msg


class Panel(models.Model):

    title = models.CharField(verbose_name=_(u'Title'),
                             max_length=100)
    panel_type = models.CharField(verbose_name=_(u'Color type'),
                                  choices=COLOR_CHOICES,
                                  max_length=10)
    creation_time = models.DateTimeField(verbose_name=_(u'Creation time'))
    content = models.TextField(verbose_name=_(u'Content'))

    class Meta:
        verbose_name = _('Panel')
        verbose_name_plural = _('Panels')

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title


class Thumbnail(models.Model):

    alt = models.CharField(verbose_name=_(u'Alt'),
                           max_length=200)
    img = models.ImageField(verbose_name=_(u'Image'), upload_to='thumbnails')

    class Meta:
        verbose_name = _('Thumbnail')
        verbose_name_plural = _('Thumbnails')
#
 #   def __str__(self):
  #      return self.text

   # def __unicode__(self):
        #return self.title