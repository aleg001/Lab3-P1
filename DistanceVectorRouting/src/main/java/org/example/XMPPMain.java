package org.example;

import org.jivesoftware.smack.packet.Presence;
import org.jxmpp.stringprep.XmppStringprepException;

import java.util.*;

public class XMPPMain {

    public static void main(String[] args) throws XmppStringprepException {
        Scanner scanner = new Scanner(System.in);
        int choice;

        XMPPClient xmppClient = new XMPPClient();

        String selectedNode = xmppClient.selectNode(false);
        if (selectedNode != null) {
            String userNode = selectedNode.replace("@alumchat.xyz", "");
            xmppClient.login(userNode, "123");
            int[] distanceVector = xmppClient.tablaEnrutamiento(selectedNode);
            System.out.println("\nVECTOR DE DISTANCIA INICIAL:\n " + Arrays.toString(distanceVector));
            xmppClient.broadcastMessage();
        }
        do {
            System.out.println("\nMENU");
            System.out.println("1. Vector distancia");
            System.out.println("2. Enviar mensaje");
            System.out.println("3. Salir");
            System.out.print("Select an option: ");
            choice = scanner.nextInt();
            switch (choice) {
                case 1:
                    System.out.println("\nVECTOR DE DISTANCIA:\n " + Arrays.toString(xmppClient.getTablaEnrutamiento()) + "\n ENLACES \n " + Arrays.toString(xmppClient.getEnlaces()));
                    break;
                case 2:
                    String messageNode = xmppClient.selectNode(true);
                    System.out.print("Ingrese el mensaje a enviar: ");
                    scanner.nextLine();
                    String cm = scanner.nextLine();
                    xmppClient.chatMessage(messageNode, cm);
                    break;
                case 3:
                    xmppClient.disconnect();
                    System.out.println("Gracias por usar el programa");
                    break;
                default:
                    System.out.println("Invalid option.");
            }
        }while (choice != 3);




    }

}
