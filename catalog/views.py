# -*- coding: utf-8 -*-
from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import Http404, HttpResponse
from django.db.models import Q

from catalog.models import Drug
from catalog.form import SearchFormAdvanced


def index(request):
    """
        Заглушка для главной страницы.
        Выводит переменную для title.
    """
    return render(request, 'base.html', {'page_name': 'Main page'})


def catalog(request):
    """
    Эта функция извлекает из БД все объекты, и передает их в шаблон ввиде словаря.
    """
    obj_drugs = Drug.objects.all()[:10]

    if not obj_drugs:
        raise Http404

    return render(request, 'catalog.html', {'obj_drugs': obj_drugs})


def drug_detail(request, uid):
    """
    Функция извлекает один объект по uid полученного из URL.
    """
    obj_drug = get_object_or_404(Drug, id__exact=int(uid))

    return render(request, 'drug_detail.html', {'obj_drug': obj_drug})


def search(request):
    """
    Функция поиска.
    """
    form = SearchFormAdvanced()
    if request.method == 'GET':
        form = SearchFormAdvanced(request.GET or None)
        if form.is_valid():
            # Непосредвенно здесь выполняется поиск
            qs = form.cleaned_data['search_query']
            q_opt = form.cleaned_data['q_opt']

            if q_opt == 'q_sympt':
                search_results = Drug.objects.filter(Q(title__iexact=qs) | Q(symptoms__icontains=qs))
            elif q_opt == 'q_contrind':
                search_results = Drug.objects.filter(Q(title__iexact=qs) | Q(contraindications__icontains=qs))
            elif q_opt == 'q_descr':
                search_results = Drug.objects.filter(Q(title__iexact=qs) | Q(description__icontains=qs))
            elif q_opt == 'q_all':
                search_results = Drug.objects.filter(Q(title__iexact=qs) \
                                                     | Q(symptoms__icontains=qs) \
                                                     | Q(contraindications__icontains=qs) \
                                                     | Q(description__icontains=qs))

            if not search_results:
                msg = 'По вашему запросу ничего не найдено.'
                return render_to_response('search.html', {'msg': msg})

            return render_to_response('search.html', {'search_results': search_results, 'qs': qs})

    return render(request, 'search.html', {'form': form})
