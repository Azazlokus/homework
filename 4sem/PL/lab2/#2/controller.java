import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.scene.control.Button;
import javafx.scene.control.CheckBox;
import javafx.scene.control.RadioButton;
import javafx.scene.control.TextField;


public class controller {
      
    @FXML
    private Button btn;
    @FXML
    private RadioButton rbtn;
    @FXML
    private TextField text;
    @FXML
    private CheckBox check_btn, check_rbtn, check_text;
		 
    @FXML
    private void hide(ActionEvent event) {
        if (check_btn.isSelected()){
           btn.setVisible(false);
        }
        else{
           btn.setVisible(true);
        }
        
        if (check_rbtn.isSelected()){
            rbtn.setVisible(false);
        }
        else{
            rbtn.setVisible(true);
        }

        if (check_text.isSelected()){
            text.setVisible(false);
        }
        else {
            text.setVisible(true);
        }
    }
}
