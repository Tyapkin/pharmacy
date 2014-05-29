# -*- coding: utf-8 -*-
from django.db import models


class Drug(models.Model):
    title = models.CharField('название препарата', max_length=64, unique=True)
    symptoms = models.TextField('показания')
    contraindications = models.TextField('противопоказания')
    description = models.TextField('описание препарата', blank=True)

    class Meta:
        # здесь находятся мета-данные модели
        verbose_name = 'drug'
        verbose_name_plural = 'drugs'
        ordering = ('title',) # сортировка по названию препарата

    def __str__(self):
        # возвращаем понятное для человека название в админке
        return '%s' % self.title

    def get_absolute_url(self):
        '''
        функция возвращает абсолютную ссылку для препарата
        '''
        from django.core.urlresolvers import reverse
        return reverse('catalog.views.drug_detail', args=[str(self.id)])
