package controller;

import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.scene.control.Button;
import javafx.scene.control.TextField;
import javafx.stage.Stage;
import database.city;

public class ControllerInsert{
    @FXML
    private TextField area;

    @FXML
    private TextField name;

    @FXML
    private Button ok_btn;

    @FXML
    void insertStage(ActionEvent event) {
        String nameString = name.getText();
        String areaString = area.getText();
        city.addCity(nameString, areaString);
        Stage stage = (Stage) ok_btn.getScene().getWindow();
        Controller.refresh();
        stage.close();
    }
}
