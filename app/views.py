from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.db.models import Sum, Min

# Create your views here.
def hello(request, nome, idade):
    return HttpResponse('<h1>Hello {} de {} anos</h1>'.format(nome,idade))

def soma(request, numero1, numero2):
    somar = numero1 + numero2
    return HttpResponse('A soma de {} e {} é: {} '.format(numero1, numero2,somar))

def subtracao(request, numero1, numero2):
    sub = numero1 - numero2
    return HttpResponse('A subtração de {} e {} é: {}'.format(numero1,numero2,sub))
def multiplicacao(request, numero1, numero2):
    mult = numero1 * numero2
    return HttpResponse('A multiplicação de {} e {} é: {}'.format(numero1,numero2,mult))

def divisao(request, numero1, numero2):
    div = numero1 / numero2
    return HttpResponse('A divisão de {} e {} é: {}'.format(numero1,numero2,div))