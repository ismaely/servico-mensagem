#
# forms.py
# @Author : Gunza Ismael (7ilipe@gmail.com)
# @Link   : 
# @Date   : 12/09/2019, 00:33:33
from django import forms
from django.forms import ModelForm
from app_sms.models import Enviar_sms, Pessoa



class Mensagem_Form(ModelForm):
    class Meta:
        model = Enviar_sms
        fields = ['telefone', 'sms']
        widgets = {
            'telefone': forms.TextInput(attrs={'class': 'form-control'}),
            #'email': forms.TextInput(attrs={'class': 'form-control'}),
            'sms': forms.Textarea(attrs={'type':'textarea', 'class': 'form-control'}),
        }
    #sms = forms.CharField(required=False, widget=forms.Select(choices = TIPO_DECLARACAO , attrs={'class': 'form-control'}))
    