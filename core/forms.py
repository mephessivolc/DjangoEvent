from django import forms

from .models import Congress, TypeCongress

class CongressCreateUpdateForm(forms.ModelForm):

    class Meta:
        model = Congress
        fields = ['username', 'name', 'type_congress']

class TypeCongressCreateUpdateForm(forms.ModelForm):

    class Meta:
        model = TypeCongress
        fields = ['type_congress', ]