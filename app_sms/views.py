from django.shortcuts import render
import random, json, re, os, sweetify
from django.core import serializers
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, JsonResponse, HttpRequest, Http404, HttpResponse, FileResponse
from django.core.exceptions import ObjectDoesNotExist
from app_sms.forms import Mensagem_Form
from twilio.rest import Client
import os

# Create your views here.




def home(request):
    context = {}
    return render (request, 'home_centro.html', context)



def enviar_sms(request):
    form = Mensagem_Form(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            account = "AC8158560609ad1dab700b9d33aba03e66"
            token = "05989749d865919e0eccc041a0f7683d"
            client = Client(account, token)
            #+19282966246
            message = client.messages.create(
                to="+244 924 76 26 46", 
                from_="+1 928 296 6246",
                body="seja bem vindo ao salakiaku..!"
                )
            form.save()
            sweetify.success(request, 'Menssagem enviada com sucesso!....', button='Ok', timer='3100')
            return HttpResponseRedirect(reverse('app_sms:home'))

    context = {'form':form}
    return render (request, 'app/enviar_sms.html', context)




#@login_required
"""def sair(request):
    try:
        logout(request)
        #return HttpResponseRedirect(reverse('utilizador:login'))
    except Exception as e:
        raise Http404("erro a terminar a sessão %s " % (e))"""