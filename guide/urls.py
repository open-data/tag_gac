from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls import url
from guide.views import FORMS, url_name, done_step_name, TradeForm, lt_condition, EntitiesAutocomplete, TypeAutocomplete, CodeAutocomplete, OpenPDF
from django.shortcuts import redirect
from django.views.generic.base import RedirectView

trade_wizard = TradeForm.as_view(
    FORMS, 
    condition_dict={"3": lt_condition}, 
    url_name=url_name, 
    done_step_name=done_step_name
)
app_name='guide'
urlpatterns = [
    path('entities_autocomplete/', EntitiesAutocomplete.as_view(), name='entities_autocomplete'),
    path('type_autocomplete/', TypeAutocomplete.as_view(), name='type_autocomplete'),
    path('code_autocomplete/', CodeAutocomplete.as_view(), name='code_autocomplete'),
    path('open_pdf/', OpenPDF.as_view(), name='open_pdf'),
    path('markdownx/', include('markdownx.urls')),
    path('form/<step>/', trade_wizard, name='form_step'),
    path('form/done/', trade_wizard, name='done_step'),
    re_path('form/', RedirectView.as_view(url='0/'), name='form_start'),
    re_path('', RedirectView.as_view(url='form/0/')),
    re_path(r'^.*$', RedirectView.as_view(url='form/0/')),
    re_path(r'^.*/$', RedirectView.as_view(url='form/0/'))
]