from django import forms

from journal import models


class DateInputWidget(forms.DateTimeInput):
    input_type = 'datetime-local'

    def __init__(self, attrs=None, format='%Y-%m-%dT%H:%M'):
        attrs = attrs if attrs else dict()
        if 'class' not in attrs:
            attrs['class'] = 'form-control'
        super().__init__(attrs, format)


class ToiletForm(forms.ModelForm):
    class Meta:
        model = models.ToiletRecord
        fields = ['category', 'dt']

        widgets = {
            'dt': DateInputWidget(),
            'category': forms.Select(attrs={'class': "form-select"})
        }


class FoodForm(forms.ModelForm):
    class Meta:
        model = models.FoodRecord
        fields = ['category', 'name', 'quantity', 'dt']

        widgets = {
            'dt': DateInputWidget(attrs={'class': "form-control"}),
            'category': forms.Select(attrs={'class': "form-select"}),
        }


class SleepForm(forms.ModelForm):
    class Meta:
        model = models.SleepRecord
        fields = ['duration', 'dt']

        widgets = {
            'dt': DateInputWidget(),
        }


class WalkForm(forms.ModelForm):
    class Meta:
        model = models.WalkRecord
        fields = ['duration', 'dt']

        widgets = {
            'dt': DateInputWidget(),
        }


class GymnasticsForm(forms.ModelForm):
    class Meta:
        model = models.GymnasticsRecord
        fields = ['duration', 'dt']

        widgets = {
            'dt': DateInputWidget(),
        }


class OtherEventForm(forms.ModelForm):
    class Meta:
        model = models.OtherEventRecord
        fields = ['name', 'description', 'dt']

        widgets = {
            'dt': DateInputWidget(),
        }
