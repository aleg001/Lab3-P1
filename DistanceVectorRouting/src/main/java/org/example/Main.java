package org.example;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Network network = new Network(10);

        System.out.println(network.getNodes());

        int updates = 1;
        while (updates!=0) {
            updates = network.distanceVectorRouting(1, false);
            System.out.println("Actualizaciones: "+updates);
        }
        network.printTopology();

        NetworkDiagram.display(network);

        // Solicitar la entrada del usuario para el nodo de origen y destino
        Scanner scanner = new Scanner(System.in);
        System.out.print("Ingrese el nodo de origen: ");
        Integer origen = scanner.nextInt();
        System.out.print("Ingrese el nodo de destino: ");
        Integer destino = scanner.nextInt();

        Node sourceNode = network.getNodes().get(origen);
        Node destinationNode = network.getNodes().get(destino);

        if (sourceNode == null || destinationNode == null) {
            System.out.println("Nodo de origen o destino no encontrado en la topología.");
            return;
        }

        // Enviar un mensaje desde el nodo de origen al nodo de destino
        network.sendMessage(sourceNode, destinationNode, "Hola, soy " + origen + " e intento llegar a " + destino);

    }
}