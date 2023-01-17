import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.IOException;
import java.net.Socket;
import java.util.ArrayList;

public class ClientHandler implements Runnable{

    public static ArrayList<ClientHandler> clientHandlers = new ArrayList<>();
    private Socket socket;
    private DataInputStream in;
    private DataOutputStream out;
    private String clientUserName;

    public ClientHandler(Socket socket) {
        try{
            this.socket = socket;
            this.in = new DataInputStream(socket.getInputStream());
            this.out = new DataOutputStream(socket.getOutputStream());
            this.clientUserName = in.readUTF();
            clientHandlers.add(this);
            broadcastMessage("Server: " + clientUserName + "has entered the game");
        } catch (IOException e){
            closeEverything(socket, in, out);
        }
    }

    private void broadcastMessage(String string) {
        for (ClientHandler clientHandler : clientHandlers) {
            try{
                if (clientHandler.clientUserName.equals(clientUserName)){
                    clientHandler.out.writeUTF(string);
                    clientHandler.out.flush();
                }
            } catch (IOException e){
                closeEverything(socket, in, out);
            }
        }
    }

    public void removeClientHandler(){
        clientHandlers.remove(this);
        broadcastMessage("Server:" + clientUserName + "has left the game");
    }

    public void closeEverything(Socket socket, DataInputStream in, DataOutputStream out){
        removeClientHandler();
        try{
            socket.close();
            in.close();
            out.close();
        } catch (IOException e){
            e.printStackTrace();
        }
    }

    @Override
    public void run() {
        while (socket.isConnected()){

        }
    }
    
}