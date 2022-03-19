from django import forms

from calc.models import teacher


class studentform(forms.ModelForm):
    class Meta:
        model = teacher
        fields = '__all__'