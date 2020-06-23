from django import forms
from django.forms.forms import ValidationError
from django.utils.translation import ugettext_lazy as _
from guide.models import Organization, Code, GeneralException, LimitedTenderingReason, CftaException, CommodityType
from django.db.models import Q
from dal import autocomplete

estimated_value_label = _('What is the total estimated value of the procurement? ')
entities_label = _('Who is the procuring entity?')
type_label = _('What is the procurement commodity type?')
code_label = _('What is the Goods and Services Identification Number commodity (GSIN) code most closely associated with the procurement?')
general_exceptions_label = _("Exceptions")
limited_tendering_label = _("Limited Tendering Reasons")
cfta_exceptions_label = _("CFTA Exceptions")

# class TForm(forms.ModelForm):
#     class Meta:
#         model = TModel
#         fields = ('name', 'test')
#         widgets = {
#             'test': autocomplete.ModelSelect2(url='select2_fk')
#         }

class RequiredFieldsForm(forms.Form):

    estimated_value = forms.IntegerField(
        label = estimated_value_label,
        required = False,
        min_value = 0
    )
    estimated_value.widget.attrs['class'] = 'form-control'

    entities = forms.ModelChoiceField(
        Organization.objects.all(),
        label = entities_label,
        required = False,
        widget=autocomplete.ModelSelect2(url='entities-autocomplete')
    )

    type = forms.ModelChoiceField(
        CommodityType.objects.all(),
        label = type_label,
        required = False,
        widget = autocomplete.ModelSelect2(url='type-autocomplete')
    )
    
    code = forms.ModelChoiceField(
        Code.objects.only('code'),
        label = code_label,
        required = False,
        widget = autocomplete.ModelSelect2(url = 'code-autocomplete', forward=['type'])
    )

    def clean_estimated_value(self):
        val = self.cleaned_data.get('estimated_value')
        if val is None:
            raise ValidationError('Please enter a valid number greater than zero.')

        if int(val) <= 0:
            raise ValidationError('Please enter a valid number greater than zero.')
        else:
            return int(val)

    def clean_entities(self):
        org = self.cleaned_data.get('entities')
        if Organization.objects.filter(name = org).exists():
            return org
        else:
            raise ValidationError('Select a valid choice. That choice is not one of the available choices.')

    def clean_type(self):
        type = self.cleaned_data.get('type')
        if Code.objects.filter(type = type).exists():
            return type
        else:
            raise ValidationError('Select a valid choice. That choice is not one of the available choices.')
        # type = self.cleaned_data.get('type')
        # try:
        #     if Code.objects.filter(type_en_ca = type).exists():
        #         return type
        #     else:
        #         raise ValidationError('Select a valid choice. That choice is not one of the available choices.')
        # except:
        #     if Code.objects.filter(type_fr_ca = type).exists():
        #         return type
        #     else:
        #         raise ValidationError('Select a valid choice. That choice is not one of the available choices.')

    def clean_code(self):
        code = self.cleaned_data.get('code')
        if Code.objects.filter(code = code).exists():
            return code
        else:
            raise ValidationError('Select a valid choice. That choice is not one of the available choices.')

class GeneralExceptionForm(forms.Form):

    exceptions = forms.ModelMultipleChoiceField(
        GeneralException.objects.only('name'),
        widget = forms.CheckboxSelectMultiple,
        label = general_exceptions_label,
        required = False
    )
    exceptions.widget.attrs['class'] = 'form-control'


class LimitedTenderingForm(forms.Form):

    limited_tendering = forms.ModelMultipleChoiceField(
        LimitedTenderingReason.objects.only('name'),
        widget = forms.CheckboxSelectMultiple,
        label = limited_tendering_label,
        required = False
    )
    limited_tendering.widget.attrs['class'] = 'form-control'


class CftaExceptionForm(forms.Form):

    cfta_exceptions = forms.ModelMultipleChoiceField(
        CftaException.objects.only('name'),
        to_field_name = 'id',
        widget = forms.CheckboxSelectMultiple,
        label = cfta_exceptions_label,
        required = False
    )
    cfta_exceptions.widget.attrs['class'] = 'form-control'


