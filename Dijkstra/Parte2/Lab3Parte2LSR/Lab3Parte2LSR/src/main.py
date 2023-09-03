import json
from slixmpp.exceptions import IqError, IqTimeout
from slixmpp.xmlstream import ElementBase, ET, register_stanza_plugin
import slixmpp
import prettytable
import threading
import asyncio
import aioconsole
import base64
import time
from cliente import *

class Main:
    def __init__(self):
        self.topologia = r'C:\Users\charl\Desktop\Lab3Parte2LSR\src\Data\topologia.json'
        self.nomenclatura = r'C:\Users\charl\Desktop\Lab3Parte2LSR\src\Data\nomenclatura.json'
        self.cuenta = None
        self.nodo = None
        pass

    def banner(self, header, row_jumps = True):
        value   = 60
        banner = "{:─^60}".format(header)

        print(f'{"─"*value}')

        if row_jumps:
            print(f'\n{banner}\n')
        else:
            print(f'{banner}')
        print(f'{"─"*value}\n')

    def run(self):

        with open(self.topologia, 'r') as archivo:
            topologia = json.load(archivo)

        tipo = topologia["type"]
        config = topologia["config"]

        llaves = list(config.keys())

        print()
        while True:
            self.banner("Selecciona el nodo a representar en la topología", False)
            for posicion, nodo in enumerate(config):
                print(f"{posicion}.) {nodo}")
            print()

            try:
                nodo_elegido = int(input(" --> "))
                if 0 <= nodo_elegido < len(config):
                    break  # Salir del bucle si el valor es válido
                else:
                    print("Por favor, elige un número válido.")
            except ValueError:
                print("Por favor, ingresa un número válido.")

        with open(self.nomenclatura, 'r') as archivo:
            nomenclatura = json.load(archivo)

        tipo_n = nomenclatura["type"]
        nomen = nomenclatura["config"]

        self.banner(f" Utilizas la cuenta --> {nomen[llaves[nodo_elegido]]} ", False)

        self.cuenta = nomen[llaves[nodo_elegido]]
        self.nodo = llaves[nodo_elegido]



        # El código principal de tu programa irá aquí.
        # print("¡Hola, mundo!")

if __name__ == "__main__":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    programa = Main()
    programa.run()
    cliente = cliente(programa.cuenta,"1234", programa.nodo)
    cliente.connect(disable_starttls=True, use_ssl=False)
    cliente.process(forever=False)

