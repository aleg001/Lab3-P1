import java.io.IOException;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.Map;
import java.util.UUID;
import java.util.concurrent.ConcurrentHashMap;
import com.google.gson.JsonObject;
import com.google.gson.JsonParser;
public class ChatServer {
    private static final int PORT = 12345;
    private static Map<String, ChatClientHandler> clients = new ConcurrentHashMap<>();

    public static void main(String[] args) {
        try (ServerSocket serverSocket = new ServerSocket(PORT)) {
            System.out.println("ChatServer is running on port " + PORT);

            while (true) {
                Socket clientSocket = serverSocket.accept();
                String clientId = UUID.randomUUID().toString();
                ChatClientHandler clientHandler = new ChatClientHandler(clientSocket, clientId);
                clients.put(clientId, clientHandler);
                Thread thread = new Thread(clientHandler);
                thread.start();
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public static void broadcastMessage(String jsonMessage, String senderId) {
        ChatClientHandler sender = clients.get(senderId);

        try {
            // Parsea el mensaje JSON
            JsonParser jsonParser = new JsonParser();
            JsonObject jsonObject = jsonParser.parse(jsonMessage).getAsJsonObject();

            // Extrae el destinatario del mensaje desde el campo "to"
            String recipient = jsonObject.getAsJsonObject("headers").get("to").getAsString();

            // Envía el mensaje completo solo al destinatario
            for (Map.Entry<String, ChatClientHandler> entry : clients.entrySet()) {
                String clientId = entry.getKey();
                ChatClientHandler client = entry.getValue();
                if (client.getClientName().equals(recipient)) {
                    client.sendMessage(jsonMessage);
                }
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }


}
