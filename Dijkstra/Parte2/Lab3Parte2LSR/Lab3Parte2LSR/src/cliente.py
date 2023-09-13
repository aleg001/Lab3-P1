import slixmpp
import json
from slixmpp.exceptions import IqError, IqTimeout
from slixmpp.xmlstream import ElementBase, ET, register_stanza_plugin
import slixmpp
import prettytable
import threading
import asyncio
import aioconsole
import base64
from tabulate import tabulate
import time
# Define la clase de tu cliente XMPP
class cliente(slixmpp.ClientXMPP):
    def __init__(self, jid, password, noddi):

        self.matriz = None
        self.usuario = jid
        self.recibidos = []
        self.old = True
        self.auto_nodo = noddi
        self.topologia = r'C:\Users\charl\Desktop\Lab3Parte2LSR\src\Data\topologia.json'
        self.nomenclatura = r'C:\Users\charl\Desktop\Lab3Parte2LSR\src\Data\nomenclatura.json'

        super().__init__(jid, password)

        # * Plugins para conexiones y manipulaciones
        self.register_plugin("xep_0199")
        self.register_plugin("xep_0030")
        self.register_plugin("xep_0004")
        self.register_plugin("xep_0060")
        self.register_plugin("xep_0085")
        self.register_plugin("xep_0066")
        self.register_plugin('xep_0045')
        self.register_plugin('xep_0085')
        self.register_plugin('xep_0353')

        self.add_event_handler("session_start", self.start)
        self.add_event_handler("message", self.listener)
        # self.add_event_handler("menu", self.menu_principal)

    def banner(self, header, row_jumps = True):
        value   = 60
        banner = "{:─^60}".format(header)

        print(f'{"─"*value}')

        if row_jumps:
            print(f'\n{banner}\n')
        else:
            print(f'{banner}')
        print(f'{"─"*value}\n')

    async def start(self, event):
        self.send_presence()
        self.get_roster()

        self.old = False
        with open(self.nomenclatura, 'r') as archivo:
            nomenclatura = json.load(archivo)

        tipo_n = nomenclatura["type"]
        nomen = nomenclatura["config"]
        orden = list(nomen.keys())

        self.matriz = [[9999] * len(nomen) for _ in range(len(nomen))]

        with open(self.topologia, 'r') as archivo:
            topologia = json.load(archivo)

        tipo_T = topologia["type"]
        topo_T = topologia["config"]

        print(self.auto_nodo)

        for vecino in topo_T[self.auto_nodo]:
            self.matriz[orden.index(self.auto_nodo)][orden.index(vecino)] = 1

        self.matriz[orden.index(self.auto_nodo)][orden.index(self.auto_nodo)] = 0

        print(tabulate(self.matriz, tablefmt="fancy_grid"))

        """ Enviando informacion a vecinos """

        for vecino in topo_T[self.auto_nodo]:
            mensaje = {"type":"echo","headers": {"from": f"{self.auto_nodo}", "to": f"{vecino}", "hop_count": 1},"payload": "ping"}

            concatenacion = json.dumps(mensaje)

            from_ = self.usuario
            to_ = nomen[vecino]
            # email_destino = "nuevor@alumchat.xyz"

            self.banner(f" Mensaje inicial a vecino {vecino} ", False)
            self.send_message(mto=to_, mbody=concatenacion, mtype='chat')

        """ Menu principal """
        # asyncio.create_task(self.menu_principal())


    async def menu_principal(self):
        await asyncio.sleep(10)
        while True:
            print("Menú:")
            print("1. Matriz")
            print("2. Enviar mensaje")
            print("3. Salir")

            opcion = input("Selecciona una opción (1/2/3): ")

            if opcion == "1":
                print("Has seleccionado la Opción 1.")
                print(tabulate(self.matriz, tablefmt="fancy_grid"))

            elif opcion == "2":
                print("Has seleccionado la Opción 2.")
                # Aquí puedes colocar el código que corresponde a la Opción 2.
            elif opcion == "3":
                print("Saliendo del programa.")
                self.disconnect()
                break
            else:
                print("Opción no válida. Por favor, selecciona una opción válida (1/2/3).")

    async def listener(self, msg):

        if self.old:
            return
        raw_data = msg['body']
        # print(raw_data)

        if "echo" in raw_data:
            with open(self.nomenclatura, 'r') as archivo:
                nomenclatura = json.load(archivo)

            tipo_n = nomenclatura["type"]
            nomen = nomenclatura["config"]

            data = json.loads(raw_data.replace("'", '"'))
            # print(data["type"])

            emisor = nomen[data['headers']['from']]
            saltos = data['headers']['hop_count']


            if saltos == 1:
                # print("in")
                self.recibidos.append(emisor)

                emisor_nodo = None

                for llave, valor in nomen.items():
                    if valor == emisor:
                        emisor_nodo = llave

                # print(f' Regresando informacion a {emisor} ')

                print("enviando mensaje 2 saltos")

                mensaje = {"type":"echo","headers": {"from": f"{self.auto_nodo}", "to": f"{emisor_nodo}", "hop_count": 2},"payload": "ping"}
                concatenacion = json.dumps(mensaje)
                print(concatenacion)
                self.send_message(mto=emisor, mbody=concatenacion, mtype='chat')


                print("buenas")
                self.recibidos.append(emisor)
                self.recibidos = list(set(self.recibidos))


                print("enviando mensaje 1 saltos")
                x_nodo = None
                for llave, valor in nomen.items():
                    if valor == emisor:
                        x_nodo = llave

                mensaje = {"type":"info", "headers": {"from": f"{self.auto_nodo}", "to": f"{x_nodo}", "hop_count": 1}, "payload": str(self.matriz)}
                concatenacion = json.dumps(mensaje)

                print(concatenacion)

                self.send_message(mto=emisor, mbody=concatenacion, mtype='chat')


            elif saltos == 2:
                print("imn")
                self.recibidos.append(emisor)
                self.recibidos = list(set(self.recibidos))

                self.banner(f' Enviando tabla a  {emisor} ', False)

                x_nodo = None
                for llave, valor in nomen.items():
                    if valor == emisor:
                        x_nodo = llave

                mensaje = {"type":"info", "headers": {"from": f"{self.auto_nodo}", "to": f"{x_nodo}", "hop_count": 1}, "payload": str(self.matriz)}
                concatenacion = json.dumps(mensaje)

                self.send_message(mto=emisor, mbody=concatenacion, mtype='chat')

        elif "info" in raw_data:
            data = json.loads(raw_data.replace("'", '"'))

            with open(self.nomenclatura, 'r') as archivo:
                nomenclatura = json.load(archivo)

            tipo_n = nomenclatura["type"]
            nomen = nomenclatura["config"]

            emisor = nomen[data['headers']['from']]
            matriz_de_emisor = json.loads(data['payload'].replace("'", '"'))

            # print(matriz_de_emisor)

            son_iguales = True
            for i in range(len(self.matriz)):
                for j in range(len(self.matriz[i])):
                    if self.matriz[i][j] != matriz_de_emisor[i][j]:
                        son_iguales = False
                        break

            if son_iguales == False:
                print("ACtualizando")
                for i in range(len(matriz_de_emisor)):
                    for j in range(len(matriz_de_emisor[i])):
                        if self.matriz[i][j] == 9999:
                            self.matriz[i][j] = matriz_de_emisor[i][j]

                for visitas in self.recibidos:
                    emisor_nodo = None
                    for llave, valor in nomen.items():
                        if valor == visitas:
                            emisor_nodo = llave

                    mensaje = {"type":"info", "headers": {"from": f"{self.auto_nodo}", "to": f"{visitas}", "hop_count": 1}, "payload": str(self.matriz)}
                    concatenacion = json.dumps(mensaje)

                    self.send_message(mto=emisor, mbody=concatenacion, mtype='chat')
                    await asyncio.sleep(1)
        # print(msg["body"])
        # print(tabulate(self.matriz, tablefmt="fancy_grid"))
