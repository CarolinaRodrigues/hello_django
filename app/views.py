from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.db.models import Sum, Min

# Create your views here.
def hello(request, nome, idade):
    return HttpResponse('<h1>Hello {} de {} anos</h1>'.format(nome,idade))

#Exercício para práticar
#No mesmo projeto que criamos acrescentar uma rota que aceite na URL mais dois parâmetros do tipo inteiro e retorne a soma deste dois parâmetros.
#A URL deverá ficar da seguinte forma:/soma/10/20
#Com o exemplo acima, a aplicação devará retorna a soma de 10 e 20.
#Criar rotas também para multiplicação, divisão e subtração.
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