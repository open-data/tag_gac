from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from guide.views import getType, getCode, TradeForm
from guide.forms import MandatoryElementsEN, ExceptionsEN, LimitedTenderingEN, CftaExceptionsEN

named_forms = (
    ('0', MandatoryElementsEN),
    ('1', ExceptionsEN),
    ('2', LimitedTenderingEN),
    ('3', CftaExceptionsEN)
)
trade_wizard = TradeForm.as_view(named_forms, url_name='guide:form_step', done_step_name='guide:done_step')

urlpatterns = [
    url(r'^en/(?P<step>.+)/$', trade_wizard, name='form_step'),
    url('/en/done/', trade_wizard, name='done_step'),
    path("ajax/type/", getType, name = 'get_type'),
	path("ajax/code/", getCode, name = 'get_code')
]
