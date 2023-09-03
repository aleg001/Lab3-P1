package com.example;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Scanner;

import org.json.simple.JSONObject;
import org.json.simple.parser.JSONParser;

public class App {
    public static void main(String[] args){
        
        
        Scanner scanner = new Scanner(System.in);
        

        
        // ? Variables locales
        
        String nodoAgregado;
        
        String archivoJSON = "C:\\Users\\charl\\Desktop\\S22023\\Redes\\Laboratorio 3\\Parte 1\\Lab3-P1\\src\\Dijkstra\\asignaciones.json";
        String nombreArchivo = "C:\\Users\\charl\\Desktop\\S22023\\Redes\\Laboratorio 3\\Parte 1\\Lab3-P1\\src\\Dijkstra\\matriz_adyacencia.txt";
        
        // * Agregar el nodo al diccionario de nodos existentes * //
        
        while(true){

            System.out.print("\n --> Ingrese el nombre del nodo: ");
            nodoAgregado = scanner.nextLine();

            try {
                JSONParser parser = new JSONParser();
                FileReader fileReader = new FileReader(archivoJSON);
                JSONObject jsonObject = (JSONObject) parser.parse(fileReader);
                fileReader.close();
                
                int cantidadClaves = jsonObject.size();
                

                if (!jsonObject.containsKey(nodoAgregado)) {

                    jsonObject.put(nodoAgregado, cantidadClaves);

                    FileWriter fileWriter = new FileWriter(archivoJSON);
                    fileWriter.write(jsonObject.toJSONString());
                    fileWriter.close();
                    
                    System.out.println(" \"" + nodoAgregado + "\" creado, indice = " + cantidadClaves + ".\n");
                    break;
                } else {
                    System.out.println("\"" + nodoAgregado + "\" ya existe. \n");
                }
            } catch (Exception e) {
                e.printStackTrace();
            }
        }
        

        // * Aumentar la matriz * //


        try {

            BufferedReader br = new BufferedReader(new FileReader(nombreArchivo));

            // Determinar las dimensiones de la matriz
            int numRows = 0;
            int numCols = 0;

            String line;
            while ((line = br.readLine()) != null) {
                String[] values = line.split(", ");
                numCols = Math.max(numCols, values.length);
                numRows++;
            }

            numRows += 1;
            numCols += 1;

            br.close();

            // Crear la matriz con las dimensiones determinadas
            int[][] graph = new int[numRows][numCols];
        
            br = new BufferedReader(new FileReader(nombreArchivo)); // Reiniciar el lector
        
            int row = 0;
            while ((line = br.readLine()) != null) {
                String[] values = line.split(", ");
                for (int col = 0; col < values.length; col++) {
                        graph[row][col] = Integer.parseInt(values[col]);
                    }
                    row++;
                }
            
            br.close();
            
            // Ultima fila y columna de 0's

            for (int i = 0; i < numRows; i++) {
                for (int j = 0; j < numCols; j++) {
                    if (i == numRows - 1 || j == numCols - 1) {
                        graph[i][j] = 0; // Establece la última columna y la última fila a 0
                    } else {
                        // Inicializa el resto de la matriz según tus necesidades
                        // Por ejemplo, puedes asignar valores aleatorios o valores específicos aquí
                        graph[i][j] = graph[i][j] /* Valor deseado */;
                    }
                }
            }

            // Impresion

            for (int i = 0; i < numRows; i++) {
                for (int j = 0; j < numCols; j++) {
                    System.out.print(graph[i][j] + " ");
                }
                System.out.println();
            }

            // Guardar nueva matriz
            // Abre el archivo para escritura

            BufferedWriter writer = new BufferedWriter(new FileWriter(nombreArchivo));

            // Recorre la matriz y escribe cada elemento en el archivo
            for (int i = 0; i < numRows; i++) {
                for (int j = 0; j < numCols; j++) {
                    writer.write(Integer.toString(graph[i][j]));
                    if (j < numCols - 1) {
                        writer.write(", ");
                    }
                }
                writer.newLine(); // Nueva línea para la siguiente fila
            }

            // Cierra el archivo
            writer.close();

            System.out.println("Matriz guardada actualizada");

        } catch (Exception e) {
            System.out.println(" ");
        }

        // * Implementacion leyendo matriz comunitaria * //
        // String fileName = "C:\\Users\\charl\\Desktop\\S22023\\Redes\\Laboratorio 3\\Parte 1\\Lab3-P1\\src\\Dijkstra\\matriz_adyacencia.txt";
        
        // try {
        //         BufferedReader br = new BufferedReader(new FileReader(fileName));
            
        //         // Determinar las dimensiones de la matriz
        //         int numRows = 0;
        //         int numCols = 0;
            
        //         String line;
        //     while ((line = br.readLine()) != null) {
        //         String[] values = line.split(", ");
        //         numCols = Math.max(numCols, values.length);
        //         numRows++;
        //     }
        
        //     br.close();
        
        //     // Crear la matriz con las dimensiones determinadas
        //     int[][] graph = new int[numRows][numCols];
        
        //     br = new BufferedReader(new FileReader(fileName)); // Reiniciar el lector
        
        //     int row = 0;
        //     while ((line = br.readLine()) != null) {
        //         String[] values = line.split(", ");
        //         for (int col = 0; col < values.length; col++) {
        //             graph[row][col] = Integer.parseInt(values[col]);
        //         }
        //         row++;
        //     }
    
        //     br.close();
        
        //     // Ahora tienes tu matriz 'graph' lista para usar
        //     // Puedes acceder a sus elementos como graph[fila][columna]
        
        //     // Ejemplo: Imprimir la matriz
        //     for (int i = 0; i < numRows; i++) {
        //         for (int j = 0; j < numCols; j++) {
        //             System.out.print(graph[i][j] + " ");
        //         }
        //         System.out.println();
        //     }
            
        //             // Calcular distancias minimas desde origen
        // Dijkstra dijkstra = new Dijkstra(6);
        // dijkstra.dijkstra(graph, 0);
        // } catch (IOException e) {
        //     e.printStackTrace();
        // }
        
        // * Implementacion simple * //

        // int[][] graph = {
        //     {0, 2, 0, 6, 0},
        //     {2, 0, 3, 8, 5},
        //     {0, 3, 0, 0, 7},
        //     {6, 8, 0, 0, 9},
        //     {0, 5, 7, 9, 0}
        // };
        // Dijkstra.dijkstra(graph, 0);


        // int source = 0; // Nodo de origen

        while (true) {
            System.out.print("\n -> Ingrese el nombre del vecino (o 'fin'): ");
            String nombreVecino = scanner.nextLine();

            if (nombreVecino.equals("fin")) {
                break;
            }

            try {
                JSONParser parser2 = new JSONParser();
                FileReader fileReader2 = new FileReader("C:\\Users\\charl\\Desktop\\S22023\\Redes\\Laboratorio 3\\Parte 1\\Lab3-P1\\src\\Dijkstra\\asignaciones.json");
                JSONObject jsonObject2 = (JSONObject) parser2.parse(fileReader2);
                fileReader2.close();

                if (jsonObject2.containsKey(nombreVecino)) {
                    System.out.print("Ingrese la distancia a " + nombreVecino + ": ");
                    int distancia = scanner.nextInt();
                    scanner.nextLine();
                }else{
                    System.out.print("Nodo aun no existe, abra otra terminal y creelo");
                }

            } catch (Exception e) {
                System.out.println("ERROR");
            }

        }

        scanner.close();
    }
}
