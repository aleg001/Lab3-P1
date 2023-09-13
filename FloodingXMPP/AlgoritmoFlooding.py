import json
from slixmpp.exceptions import IqError, IqTimeout
from slixmpp.xmlstream import ElementBase, ET, register_stanza_plugin
import slixmpp
import asyncio
import aioconsole
from Constants import XEP_0030, XEP_0045, XEP_0085, XEP_0199, XEP_0353


class Flooding(slixmpp.ClientXMPP):
    def __init__(self, jid, password):
        super().__init__(jid, password)
        self.email = jid
        self.old = True
        self.register_plugins()
        self.add_event_handler("session_start", self.start)
        self.add_event_handler("message", self.message)
        self.Online = False
        self.topology = None
        self.message_trace = []

    def register_plugins(self):
        plugins = [XEP_0030, XEP_0045, XEP_0085, XEP_0199, XEP_0353]
        for plugin in plugins:
            self.register_plugin(plugin)

    def load_data_from_file(self, filename):
        fileExt = filename + ".txt"
        try:
            with open(fileExt, "r") as file:
                data = json.load(file)

            data = data["config"]
            return data

        except FileNotFoundError:
            print(f"File '{fileExt}' not found. Please make sure the file exists.")
            return None

    def create_message_table(self, o, d, n, m):
        return {
            "type": "message",
            "headers": {
                "from": o,
                "to": d,
                "visited": n,
            },
            "payload": m,
        }

    async def ToDict(self, package):
        try:
            Pack = package.replace("'", '"')
            return json.loads(Pack)
        except json.JSONDecodeError as err:
            print(err)
            return None

    async def start(self, event):
        try:
            print("🚀 Initializing XMPP client...")
            self.send_presence()
            print("📡 Sending presence...")
            self.get_roster()
            print("📋 Getting roster...")
            await asyncio.sleep(2)
            self.old = False
            print("📋 Creating XMPP menu task...")
            create_xmpp_menu_task = asyncio.create_task(self.create_xmpp_menu())
            await create_xmpp_menu_task
            print("✅ XMPP menu task completed.")

        except Exception as e:
            print(f"❌ Error: {e}")

    async def create_xmpp_menu(self):
        self.Online = True
        self.keys = self.NodeSelection()
        self.graph = next((k for k, v in self.keys.items() if v == self.email), None)

        print("\n📬 Welcome to your Messages and Notifications 📬")
        await asyncio.sleep(5)

        opComm = 0
        while opComm != 4:
            opComm = await self.MenuComms()
            if opComm == 1:
                await self.send_user_message()
                await asyncio.sleep(1)

            elif opComm == 2:
                print("\nGoodbye! 👋 Session closed.")
                self.disconnect()
                exit()

    async def MenuComms(self):
        print("\n1) ✉️ Send a Message")
        print("2) 🚪 Exit")

        while True:
            try:
                op = int(
                    await aioconsole.ainput("Enter the number of your desired option: ")
                )
                if op in range(1, 10):
                    return op
                else:
                    print(
                        "\n❌ Invalid option. Please choose a number between 1 and 9.\n"
                    )
            except ValueError:
                print("\n❌ Invalid input. Please enter a number.\n")

    async def send_user_message(self):
        print("\n📬 Sending a Message to a User 📬")
        recipient_node = None
        while True:
            print("Select a node from the list: ")
            nodes = self.keys
            node_keys = list(key for key, value in nodes.items())
            node_values = list(value for key, value in nodes.items())
            for i, z in enumerate(node_keys):
                print(f"{i + 1}. {z}")

            try:
                selNode = await aioconsole.ainput("Enter the node number: ")
                selNode = int(selNode)
                if 1 <= selNode <= len(nodes):
                    if self.graph == node_keys[selNode - 1]:
                        print("🚫 You can't send a message to yourself.\n")
                        continue
                    else:
                        recipient_node = node_keys[selNode - 1]
                        break
                else:
                    print("Please enter a valid number.")

            except ValueError:
                print("Please enter a valid number.")

        user_input = await aioconsole.ainput("Enter your message: ")

        vNode = [self.graph]
        Data = self.create_message_table(self.graph, recipient_node, vNode, user_input)
        message_json = json.dumps(Data)

        print("\n🚀 Sending Message 🚀")

        neighbors = self.NeighborSelection(self.graph)

        for i in neighbors:
            if i == self.email:
                continue
            if i not in vNode:
                recipient_jid = i
                self.send_message(mto=recipient_jid, mbody=message_json, mtype="chat")
                print(f"✉️ Message sent to {i}.")
                await asyncio.sleep(1)

    def NodeSelection(self):
        print("\n📋 Getting nodes from file...")
        file_name = input("Enter the file name (without extension): ")
        return self.load_data_from_file(file_name)

    def NeighborSelection(self, node):
        print("\n📋 Getting neighbors from file...")
        with open("Topologia.txt", "r") as file:
            data = json.load(file)

        data = data["config"]
        neighbors = list(data[node])

        list_neighbors = []
        for n in neighbors:
            list_neighbors.append(self.keys[n])

        return list_neighbors

    async def message(self, msg):
        if self.old:
            return

        if msg["type"] == "chat" and "message" in msg["body"]:
            sender = msg["from"].bare
            mInfo = await self.ToDict(msg["body"].replace("'", '"'))
            mCont = mInfo["payload"]
            ori = mInfo["headers"]["from"]
            dest = mInfo["headers"]["to"]
            curMess = str(ori + "," + dest + "," + mCont)

            if curMess in self.message_trace:
                self.message_trace.append(curMess)
                return
            else:
                self.message_trace.append(curMess)

            vNode = mInfo["headers"]["visited"]
            if self.graph in vNode:
                return

            if dest == self.graph:
                print(f"\n💌 Message 💌\n👤 {ori} sent a message: {mCont}")
                return

            else:
                vNode.append(self.graph)
                message_table = self.create_message_table(ori, dest, vNode, mCont)
                table = json.dumps(message_table)
                relay = True
                neighbors = self.NeighborSelection(self.graph)
                for i in neighbors:
                    neighbor_name = ""
                    reverse_keys = {v: k for k, v in self.keys.items()}
                    neighbor_name = reverse_keys.get(i, "")

                    if (
                        i == self.email
                        or neighbor_name == ori
                        or neighbor_name in vNode
                    ):
                        continue

                    else:
                        recipient_jid = i
                        self.send_message(mto=recipient_jid, mbody=table, mtype="chat")
                        print(f"Relaying message to {i}.")
                        relay = False
                        await asyncio.sleep(1)

                if relay:
                    print(
                        "📢 Oops! It seems there are no nodes available to relay the message. 😕"
                    )
