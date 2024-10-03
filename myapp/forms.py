from django import forms

class EmployeeForm(forms.Form):

    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control mb-3'}))

    designation = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control mb-3'}))

    department = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control mb-3'}))

    salary = forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control mb-3'}))

    contact = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control mb-3'}))

    address = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control mb-3'}))

