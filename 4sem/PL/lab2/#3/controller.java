import java.net.URL;
import java.util.HashMap;
import java.util.ResourceBundle;

import javax.print.DocFlavor.STRING;

import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.fxml.Initializable;
import javafx.scene.Node;
import javafx.scene.control.CheckBox;
import javafx.scene.control.ChoiceBox;
import javafx.scene.control.Label;

public class controller implements Initializable {
    ObservableList<String> firstCourse = FXCollections.observableArrayList("Borsch", "Cabbage soup", "Fish soup");
    ObservableList<String> secondCourse = FXCollections.observableArrayList("Omelet", "Pilaf", "Steak");
    ObservableList<String> desertCourse = FXCollections.observableArrayList("Chocolate cake", "Pancakes", "Berry pie");
    ObservableList<String> drinkCourse = FXCollections.observableArrayList("Water", "Juice", "Lemonade");
    ObservableList<String> countFood = FXCollections.observableArrayList("1", "2", "3", "4", "5");

    @FXML
    ChoiceBox<String> firstBox, secondBox, desertBox, drinkBox, count1, count2, count3, count4;
    @FXML
    Label total, totalCount1, totalCount2, totalCount3, totalCount4;
    HashMap<String, String> food = getFood();

    @Override
    public void initialize(URL arg0, ResourceBundle arg1) {
        firstBox.setItems(firstCourse);
        firstBox.setValue("Not selected");
        secondBox.setItems(secondCourse);
        secondBox.setValue("Not selected");
        desertBox.setItems(desertCourse);
        desertBox.setValue("Not selected");
        drinkBox.setItems(drinkCourse);
        drinkBox.setValue("Not selected");
        count1.setItems(countFood);
        count1.setValue("0");
        count2.setItems(countFood);
        count2.setValue("0");
        count3.setItems(countFood);
        count3.setValue("0");
        count4.setItems(countFood);
        count4.setValue("0");


        firstBox.setOnAction(this::updateTotalCount);
        secondBox.setOnAction(this::updateTotalCount);
        desertBox.setOnAction(this::updateTotalCount);
        drinkBox.setOnAction(this::updateTotalCount);
        count1.setOnAction(this:: updateTotalCount);
        count2.setOnAction(this::updateTotalCount);
        count3.setOnAction(this::updateTotalCount);
        count4.setOnAction(this::updateTotalCount);
    }

    @FXML
    public void updateTotalCount(ActionEvent event){
        String finalPriceItem, totalString;
        double price = 0, totalDouble = 0;

        if (food.containsKey(firstBox.getValue()) & count1.getValue().equals("0")){
            count1.setValue("1");
        }
        if (food.containsKey(secondBox.getValue()) & count2.getValue().equals("0")){
            count2.setValue("1");
        }
        if (food.containsKey(desertBox.getValue()) & count3.getValue().equals("0")){
            count3.setValue("1");
        }
        if (food.containsKey(drinkBox.getValue()) & count4.getValue().equals("0")){
            count4.setValue("1");
        }

        if (food.containsKey(firstBox.getValue())){
            price = Double.valueOf(food.get(firstBox.getValue())) * Integer.valueOf(count1.getValue());
            totalDouble += price;
            finalPriceItem = String.format("%.2f", price);
            totalCount1.setText(finalPriceItem);
        }
        if (food.containsKey(secondBox.getValue())){
            price = Double.valueOf(food.get(secondBox.getValue())) * Integer.valueOf(count2.getValue());
            totalDouble += price;
            finalPriceItem = String.format("%.2f", price);
            totalCount2.setText(finalPriceItem);
        }
        if (food.containsKey(desertBox.getValue())){
            price = Double.valueOf(food.get(desertBox.getValue())) * Integer.valueOf(count3.getValue());
            totalDouble += price;
            finalPriceItem = String.format("%.2f", price);
            totalCount3.setText(finalPriceItem);
        }
        if (food.containsKey(drinkBox.getValue())){
            price = Double.valueOf(food.get(drinkBox.getValue())) * Integer.valueOf(count4.getValue());
            totalDouble += price;
            finalPriceItem = String.format("%.2f", price);
            totalCount4.setText(finalPriceItem);
        }

        totalString = String.format("%.2f", totalDouble);
        total.setText(totalString);
    }


    public HashMap<String, String> getFood(){
        HashMap<String, String> food = new HashMap<>();
        food.put("Borsch", "12.7");
        food.put("Cabbage soup", "12.5");
        food.put("Fish soup", "9.8");
        food.put("Omelet", "5.3");
        food.put("Pilaf", "8.3");
        food.put("Steak", "16.0");
        food.put("Chocolate cake", "13.2");
        food.put("Pancakes", "11.8");
        food.put("Berry pie", "11.2");
        food.put("Water", "4.0");
        food.put("Juice", "6.3");
        food.put("Lemonade", "5.7");
        return food;
    }
}
