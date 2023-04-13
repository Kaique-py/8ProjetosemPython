"""Simulador de dado - Programa que gera um valor aleatório de 1 a 6"""
import random
import time
import PySimpleGUI

class SimuladorDeDado:
    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 6
        self.mensagem = 'Quer jogar o dado? [s/n]'
        #layout da tela
        layout = [
            [sg.Text("Jogar o dado?")],
            [sg.Buttom('SIM'), sg.Buttom("NÃO")]
        ]
        #criar janela
        janela = sg.Window("Roll the Dice!", Layout=layout)
        #ler valores da tela
        self.eventos, self.valores = janela.Read()
        #realizar algo com esses valores
    
    def Iniciar(self):
        resposta = input(self.mensagem)
        try:
            if resposta == 'S' or resposta == 's':
                self.GerarValorDoDado()
            elif resposta == 'N' or resposta == 'n':
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