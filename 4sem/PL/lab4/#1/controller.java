import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.net.Socket;
import java.net.URL;
import java.util.ResourceBundle;

import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.fxml.Initializable;
import javafx.scene.control.Button;
import javafx.scene.control.TextField;

public class controller implements Initializable{
    @FXML
    Button btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn0,
    btnDot, btnPlus, btnMinus, btnMult, btnDiv, btnEqual, btnClear;
    @FXML
    TextField expr;

    byte[] ans = new byte[2000];
    String currentOp = "", res;
    Socket s;
    InputStream in;
    OutputStream out;

    @Override
    public void initialize(URL arg0, ResourceBundle arg1) {
        try{
            s = new Socket("127.0.0.1", 1111);
            in = s.getInputStream();
            out = s.getOutputStream();
        } catch(IOException e){
            e.printStackTrace();
        }
    }

    public void sendData() throws IOException {
        out.write(expr.getText().getBytes());
        out.write(currentOp.getBytes());
    }

    public void getData() throws IOException{
        int countAns = in.read(ans);
        res = new String(ans, 0, countAns);
    }

    @FXML
    public void solve(ActionEvent event) throws IOException, InterruptedException{
        sendData();
        getData();
        if (res == "Infinity"){
            expr.setText("Divited by zero");
        }
        else{
            expr.setText(res);
        }
        currentOp = "";
    }

    @FXML
    public void clickNum(ActionEvent event){
        String btnText = ((Button) event.getSource()).getText();
        if (expr.getText().equals("/") || expr.getText().equals("+") || expr.getText().equals("*")){
            expr.setText(btnText);
        }
        else{
            expr.setText(expr.getText() + btnText);
        }
    }

    @FXML
    public void clickOp(ActionEvent event){
        String btnText = ((Button) event.getSource()).getText();
        if (btnText.equals("C")){
            expr.setText("");
        }
        else if (btnText.equals("+")){
            currentOp = "\\+";
            expr.setText(expr.getText() + btnText);
        }
        else if (btnText.equals("-")){
            currentOp = "-";
            expr.setText(expr.getText() + btnText);
        }
        else if (btnText.equals("*")){
            currentOp = "\\*";
            expr.setText(expr.getText() + btnText);
        }
        else if (btnText.equals("/")){
            currentOp = "/";
            expr.setText(expr.getText() + btnText);
        }
    }

    public String[] getNums(){
        String text = expr.getText();
        if (currentOp != "" & !text.equals("-") & !text.equals("/") & !text.equals("+") & !text.equals("*")){
            String[] res = text.split(currentOp);
            return res;
        }
        String[] res = null;
        return res;
    }

}
