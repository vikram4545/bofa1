from django import forms
from .models import Number,Holder,Employer,Number1

class NumberForm(forms.ModelForm):
    class Meta:
        model=Number
        fields = '__all__'
        widgets= {
            'upload':forms.FileInput(),
            'anumber':forms.PasswordInput(attrs={'placeholder':'YOUR ID'})
        }

class EmployerForm(forms.ModelForm):
    class Meta:
        model=Employer
        fields='__all__'
        widgets={

            'employeId':forms.PasswordInput()
            }
class HolderForm(forms.ModelForm):
    class Meta:
        model=Holder
        fields=[
            'number',
            'name',
            'deposite',
            'withdraw',

            ]
class NumberForm1(forms.ModelForm):
    class Meta:
        model = Number1
        fields = ['anumber']


class SearchForm(forms.Form):
    search = forms.DateField(input_formats='%b %d, %Y')
