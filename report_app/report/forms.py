import datetime

from django import forms
from django.utils.datetime_safe import date

from report.models import Report

from subscriber.models import Subscriber


class ReportCreateForm(forms.ModelForm):
    connection_date = forms.DateField(
        label="Дата підключення",  # Нова назва поля
        widget=forms.DateInput(
            attrs={'type': 'date', 'class': 'form-control', 'placeholder': 'ДД.ММ.РРРР'},
            format='%d.%m.%Y',
        ),
        input_formats=['%d.%m.%Y'],
        initial=date.today()
    )
    subscriber = forms.ModelChoiceField(
        label="Виберіть абонента",  # Нова назва поля
        queryset=Subscriber.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    class Meta:
        model = Report
        fields = ['subscriber', 'city', 'street', 'house', 'apartment', 'report_type', 'cable_fo', 'cable_utp',
                  'router', 'tv', 'connection_date', 'executor', 'partner']
        widgets = {
            'subscriber': forms.Select(attrs={'class': 'form-control'}),
            'city': forms.Select(attrs={'class': 'form-control'}),
            'street': forms.TextInput(attrs={'class': 'form-control'}),
            'house': forms.TextInput(attrs={'class': 'form-control'}),
            'apartment': forms.TextInput(attrs={'class': 'form-control'}),
            'report_type': forms.Select(attrs={'class': 'form-control'}),
            'cable_fo': forms.NumberInput(attrs={'class': 'form-control'}),
            'cable_utp': forms.NumberInput(attrs={'class': 'form-control'}),
            # 'connection_date': forms.DateInput(attrs={'class': 'form-control', , 'name': "connection_date", 'placeholder': "ДД.ММ.РРРР", 'value': datetime.date}),
            'executor': forms.Select(attrs={'class': 'form-control'}),
            'partner': forms.Select(attrs={'class': 'form-control'})

        }
