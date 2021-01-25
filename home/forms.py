from django import forms

from data.models import machine, order


class machine_form(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(machine_form, self).__init__(*args, **kwargs)
        self.fields['name'].label = ''
        self.fields['desc'].label = ''
        self.fields['image'].label = ''
        self.fields['manu'].label = ''
        self.fields['modell'].label = ''
        self.fields['year'].label = ''


    class Meta:
        model = machine
        fields = ['name','desc','image','manu','modell','year']

class order_form(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(order_form, self).__init__(*args, **kwargs)
        self.fields['product'].label = ''

    class Meta:
        model = order
        fields = ['product']