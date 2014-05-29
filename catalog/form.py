# -*- coding: utf-8 -*-

from django import forms


class SearchFormAdvanced(forms.Form):
    """
    Создаем форму для расширенного поиска.
    """
    Q_SYMPTOMS = 'q_sympt'
    Q_CONTRIND = 'q_contrind'
    Q_DESCR = 'q_descr'
    Q_ALL = 'q_all'
    SEARCH_OPTIONS = (
        (Q_SYMPTOMS, 'Показания'),
        (Q_CONTRIND, 'Противопоказания'),
        (Q_DESCR, 'Описание'),
        (Q_ALL, 'Искать везде'),
    )

    search_query = forms.CharField(max_length=100, label='Запрос:')
    q_opt = forms.MultipleChoiceField(choices=SEARCH_OPTIONS, label='Где искать:',
                                      widget=forms.CheckboxSelectMultiple)
