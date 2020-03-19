from django import forms
import re

class InpurMyForm(forms.Form):
    name=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'type name'}))
    email=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'type email'}))
    phone=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'type phone number'}))

    def clean(self):
        cleaned_data=super(InpurMyForm,self).clean()

        name=cleaned_data.get('name')
        print(name,'----------------------')

        email=cleaned_data.get('email')
        print(email,'-------------------')

        phone=cleaned_data.get('phone')
        print(phone,type(phone),'-----------')

        if name is None or email is None or phone is None:
            raise forms.ValidationError('inter somtiong ----------------')

        if len(name)<=5:
            raise forms.ValidationError('inter name ----------------')
        if re.match('^[a-z]+[0-9]*@gmail.com$',email)== None:
            raise forms.ValidationError('inder valid email ---------')
        if re.match('^0{1}1{1}[3-9]{1}[0-9]{8}$',phone) == None:
            raise forms.ValidationError('inter valide phone number ------------------')