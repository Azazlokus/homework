import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.scene.control.Button;
import javafx.scene.control.TextField;
import javafx.scene.input.MouseEvent;


public class controller{
      
    @FXML
    private Button btn;
    @FXML
    private TextField text1;
    @FXML
    private TextField text2;
		 
    @FXML
    private void click(ActionEvent event) {
        if (text1.getText() != ""){
            text2.setText(text1.getText());
            text1.clear();
            btn.setText("<-");
        }
        else if (text2.getText() != ""){
            text1.setText(text2.getText());
            text2.clear();
            btn.setText("->");
        }
    }

    @FXML
    private void setArrow(MouseEvent event){
        if (text1.isFocused() & text1.getText() == "" & text2.getText() == ""){ 
            btn.setText("->");
        }
        else if (text2.isFocused() & text1.getText() == "" & text2.getText() == ""){ 
            btn.setText("<-");
        }
    }
}
