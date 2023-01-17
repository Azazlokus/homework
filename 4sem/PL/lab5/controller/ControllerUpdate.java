package controller;

import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.scene.control.Button;
import javafx.scene.control.TextField;
import javafx.stage.Stage;
import database.city;

public class ControllerUpdate {

    @FXML
    private TextField area;

    @FXML
    private TextField id;

    @FXML
    private TextField name;

    @FXML
    private Button ok_btn;

    @FXML
    void updateStage(ActionEvent event) {
        String idString = id.getText();
        String nameString = name.getText();
        String areaString = area.getText();
        city.updateCity(idString, nameString, areaString);
        Stage stage = (Stage) ok_btn.getScene().getWindow();
        Controller.refresh();
        stage.close();
    }

}