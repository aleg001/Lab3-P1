package com.example;

import java.util.Arrays;

public class Dijkstra {
    
    public final int V;

    public Dijkstra(int V) {
        this.V = V;
    }
    
    public static final int INF = Integer.MAX_VALUE;

    public void dijkstra(int[][] graph, int source) {
        boolean[] visited = new boolean[V];
        int[] distance = new int[V];

        Arrays.fill(distance, INF);
        distance[source] = 0;

        for (int count = 0; count < V - 1; count++) {
            int minDistance = findMinDistance(distance, visited);

            visited[minDistance] = true;

            for (int v = 0; v < V; v++) {
                if (!visited[v] && graph[minDistance][v] != 0 &&
                    distance[minDistance] != INF &&
                    distance[minDistance] + graph[minDistance][v] < distance[v]) {
                    distance[v] = distance[minDistance] + graph[minDistance][v];
                }
            }
        }

        printSolution(distance);
    }

    public int findMinDistance(int[] distance, boolean[] visited) {
        int minDistance = INF;
        int minIndex = -1;

        for (int v = 0; v < V; v++) {
            if (!visited[v] && distance[v] <= minDistance) {
                minDistance = distance[v];
                minIndex = v;
            }
        }

        return minIndex;
    }

    public void printSolution(int[] distance) {
        System.out.println("Distancias mínimas desde el nodo de origen:");

        for (int i = 0; i < V; i++) {
            System.out.println("Nodo " + (i+1) + ": " + distance[i]);
        }
    }

}
