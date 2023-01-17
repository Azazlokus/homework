import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.control.RadioButton;
import javafx.scene.control.ToggleGroup;

public class controller {

    @FXML
    Label colors;
    @FXML
    Button btnPaint;
    @FXML
    ToggleGroup colors1, colors2, colors3;

    
    @FXML
    public void paint(ActionEvent event){
        String[] selectedColors = getSelectedColors();
        colors.setText(selectedColors[0] + ", " + selectedColors[1] + ", " + selectedColors[2]);
    }

    public String[] getSelectedColors(){
        String[] selectedColors = new String[3];
        RadioButton selected1 = (RadioButton) colors1.getSelectedToggle();
        RadioButton selected2 = (RadioButton) colors2.getSelectedToggle();
        RadioButton selected3 = (RadioButton) colors3.getSelectedToggle();
        selectedColors[0] = selected1.getText();
        selectedColors[1] = selected2.getText();
        selectedColors[2] = selected3.getText();
        return selectedColors;
    }

}
