"""Simulador de dado - Programa que gera um valor aleatório de 1 a 6"""
import random
import time
import PySimpleGUI as sg

class SimuladorDeDado:
    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 6
        self.mensagem = 'Quer jogar o dado? [s/n]'
        #layout da tela
        self.layout = [
            [sg.Text("Jogar o dado?")],
            [sg.Button('SIM'), sg.Button("NÃO")]
        ]
    
    def Iniciar(self):
        #criar janela
        janela = sg.Window("Roll the Dice!", self.layout, size=(400,400))
        #ler valores da tela
        self.eventos, self.valores = janela.Read()
        #realizar algo com esses valores
        try:
            if self.eventos == 'SIM':
                self.GerarValorDoDado()
            elif self.eventos == 'NÃO':
                print("Foi um prazer ter você por aqui. Até a próxima!")
            else:
                print("Entrada inválida. Favor responder com S ou N.")
        except:
            print("Ocorreu algum erro ao receber sua resposta.")
    def GerarValorDoDado(self):
        print("Carregando valor.")
        time.sleep(1)
        print("Carregando valor..")
        time.sleep(1)
        print("Carregando valor...")
        time.sleep(1)
        print(random.randint(self.valor_minimo, self.valor_maximo))

#Depois de criar a classe, para rodar o programa, há que se instanciar essa classe e depois chamar algum método dela:
simulador = SimuladorDeDado()
simulador.Iniciar()