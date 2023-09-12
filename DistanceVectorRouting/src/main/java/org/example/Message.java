package org.example;

public class Message {
    private Node source;
    private Node destination;
    private String content;

    public Message(Node source, Node destination, String content) {
        this.source = source;
        this.destination = destination;
        this.content = content;
    }

    public Node getSource() {
        return source;
    }

    public Node getDestination() {
        return destination;
    }

    public String getContent() {
        return content;
    }
}
