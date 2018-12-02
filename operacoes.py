from datetime import datetime

dataAtual = datetime.today()
dataEmTexto = dataAtual.strftime('%d/%m/%y')
horario = datetime.now()
h = horario.hour
m = horario.minute
s = horario.second
horariof = str(f'{h}:{m}:{s}')


def soma(a, b):
    resultado = a + b
    arqSoma = open('Relatorios/soma.txt', 'a')
    final = str(f'{dataEmTexto} , {horariof} , {a} + {b} = {resultado}''\n')
    arqSoma.write(final)


def subtrair(a, b):
    resultado = a - b
    arqSubtrair = open('Relatorios/subtracao.txt', 'a')
    final = str(f'{dataEmTexto} , {horariof} , {a} - {b} = {resultado}''\n')
    arqSubtrair.write(final)


def multiplicar(a, b):
    resultado = a * b
    arqMultiplicar = open('Relatorios/multiplicacao.txt', 'a')
    final = str(f'{dataEmTexto} , {horariof} , {a} * {b} = {resultado}''\n')
    arqMultiplicar.write(final)


def dividir(a, b):
    resultado = a / b
    arqDividir = open('Relatorios/divisao.txt', 'a')
    final = str(f'{dataEmTexto} , {horariof} , {a} / {b} = {resultado}''\n')
    arqDividir.write(final)


def relatorioSoma():
    arqsoma = open('Relatorios/soma.txt', 'r')
    print('Relatorios de soma''\n')
    print(arqsoma.read())


def relatorioSubtriar():
    arqSubtrair = open('Relatorios/subtracao.txt', 'r')
    print('Relatorios de subtracoes' '\n')
    print(arqSubtrair.read())


def relatorioMultiplicar():
    arqMultiplicar = open('Relatorios/multiplicacao.txt', 'r')
    print('Relatorios de Multiplicacoes' '\n')
    print(arqMultiplicar.read())


def relatorioDividir():
    arqDividir = open('Relatorios/divisao.txt', 'r')
    print('Relatorios de Divisoes' '\n')
    print(arqDividir.read())
