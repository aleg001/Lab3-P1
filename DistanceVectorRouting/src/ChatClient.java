import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.Socket;

public class ChatClient {
    private static final String SERVER_IP = "127.0.0.1"; // Cambia a la dirección IP del servidor si es necesario
    private static final int SERVER_PORT = 12345;

    public static void main(String[] args) {
        try {
            System.out.println("Ingresa tu nombre o identificador:");
            BufferedReader userInput = new BufferedReader(new InputStreamReader(System.in));
            String clientName = userInput.readLine();

            Socket socket = new Socket(SERVER_IP, SERVER_PORT);
            BufferedReader reader = new BufferedReader(new InputStreamReader(socket.getInputStream()));
            PrintWriter writer = new PrintWriter(socket.getOutputStream(), true);

            // Envía el nombre o identificador al servidor
            writer.println(clientName);

            // Lee mensajes del servidor
            Thread readerThread = new Thread(() -> {
                try {
                    String message;
                    while ((message = reader.readLine()) != null) {
                        System.out.println(message);
                    }
                } catch (IOException e) {
                    e.printStackTrace();
                }
            });
            readerThread.start();

            // Envía mensajes al servidor
            String userInputMessage;
            while ((userInputMessage = userInput.readLine()) != null) {
                writer.println(userInputMessage);
            }

        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
