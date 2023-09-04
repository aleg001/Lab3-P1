import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.Socket;

public class ChatClientHandler implements Runnable {
    private Socket socket;
    private PrintWriter writer;
    private String clientId;
    private String clientName;

    public ChatClientHandler(Socket socket, String clientId) {
        this.socket = socket;
        this.clientId = clientId;
    }

    @Override
    public void run() {
        try {
            BufferedReader reader = new BufferedReader(new InputStreamReader(socket.getInputStream()));
            writer = new PrintWriter(socket.getOutputStream(), true);

            // Lee el nombre o identificador del cliente
            clientName = reader.readLine();

            String message;
            while ((message = reader.readLine()) != null) {
                System.out.println("Mensaje recibido de " + clientName + ": " + message);
                ChatServer.broadcastMessage(message, clientId);
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public String getClientId() {
        return clientId;
    }

    public String getClientName() {
        return clientName;
    }

    public void sendMessage(String message) {
        writer.println(message);
    }
}
