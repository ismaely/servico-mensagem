from django.db import models

# Create your models here.




class Pessoa(models.Model):
    nome = models.CharField(max_length=200)
    genero = models.CharField(max_length=12)
    data_nascimento = models.DateField()
    bi = models.CharField(max_length=20, unique=True)
    residencia = models.CharField(max_length=90, blank=True, null=True)
    telefone = models.CharField(max_length=30, blank=True, null=True, default="--")
    email = models.EmailField(max_length=60, blank=True, null=True, default="sms@gmail.com")
    #municipio = models.ForeignKey(Municipio, on_delete=models.CASCADE, parent_link=True)
    
    def __str__(self):
        return self.id



class Enviar_sms(models.Model):
    telefone = models.CharField(max_length=18, default=" ")
    #email = models.EmailField(max_length=60, blank=True, null=True, default="sms@gmail.com")
    sms = models.CharField(max_length=390, blank=True, null=True)
    
    def __str__(self):
        return self.id
