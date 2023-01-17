import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.IOException;
import java.net.Socket;
import java.net.URL;
import java.util.ResourceBundle;
import java.util.Scanner;

import javafx.fxml.FXML;
import javafx.fxml.Initializable;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.control.TextField;

public class Client implements Initializable {
    private Socket socket;
    private DataInputStream in;
    private DataOutputStream out;
    private String userName;
    public int count_matches;
    boolean isMyStep = true;

    @FXML
    Label matchCount, turn;
    @FXML
    TextField inMatches;
    @FXML
    Button sender, ready;
    @Override
    public void initialize(URL arg0, ResourceBundle arg1) {
        Scanner scanner = new Scanner(System.in);
        String username = scanner.nextLine();
        try (Socket socket = new Socket("localhost", 1111)) {
            Client client = new Client(socket, userName);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public Client(Socket socket, String userName){
        try{
            this.socket = socket;
            this.in = new DataInputStream(socket.getInputStream());
            this.out = new DataOutputStream(socket.getOutputStream());
            this.userName = userName;
        } catch (IOException e){
            closeEverything(socket, in, out);
        }
    }

    public void sendMatches(){
        try{
            out.writeUTF(userName);
            out.flush();

            while(socket.isConnected()){

            }
        } catch (IOException e){
            closeEverything(socket, in, out);
        }
    }

    public void listenForData(){
        new Thread(new Runnable() {
            @Override
            public void run(){
                while(socket.isConnected()){

                }
            }
        }).start();
    }

    public void closeEverything(Socket socket, DataInputStream in, DataOutputStream out){
        try{
            socket.close();
            in.close();
            out.close();
        } catch (IOException e){
            e.printStackTrace();
        }
    }
    
}