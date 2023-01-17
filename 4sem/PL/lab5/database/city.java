package database;

import java.sql.ResultSet;
import java.sql.SQLException;
import javafx.beans.property.SimpleIntegerProperty;
import javafx.beans.property.SimpleStringProperty;
import javafx.collections.FXCollections;
import javafx.collections.ObservableList;

public class city {
    public SimpleIntegerProperty id;
    public SimpleStringProperty name;
    public SimpleIntegerProperty area;

    public city(int id, String name, int area){
        this.id = new SimpleIntegerProperty(id);
        this.name = new SimpleStringProperty(name);
        this.area = new SimpleIntegerProperty(area);
    }

    public int getId(){
        return this.id.get();
    }

    public String getName(){
        return this.name.get();
    }

    public int getArea(){
        return this.area.get();
    }

    public void setId(int id){
        this.id.set(id);
    }

    public void setName(String name){
        this.name.set(name);
    }

    public void setArea(int area){
        this.area.set(area);
    }

    public static ObservableList<city> getAllCities() throws SQLException{
        ObservableList<city> cities = FXCollections.observableArrayList();
        ResultSet rs;
        String query = "select * from city";
        rs = DB.exeQuery(query);
        while(rs.next()){
            city city = new city(rs.getInt("id"), rs.getString("name"), rs.getInt("area"));
            cities.add(city);
        }
        return cities;
    }

    public static ObservableList<city> getFilteredCities(String queryFilter) throws SQLException{
        ObservableList<city> cities = FXCollections.observableArrayList();
        ResultSet rs;
        String query = "select * from city where " + queryFilter + ";";
        rs = DB.exeQuery(query);
        while(rs.next()){
            city city = new city(rs.getInt("id"), rs.getString("name"), rs.getInt("area"));
            cities.add(city);
        }
        return cities;
    } 

    public static void addCity(String name, String area){
        String query = "insert into city(name, area)\nvalues (\'" + name + "\', " + area + ");";
        DB.exeUpdate(query);
    }

    public static void updateCity(String id, String name, String area){
        String query = "update city\nset name=\'" + name + "\', area=" + area + " \nwhere id=" + id + ";";
        DB.exeUpdate(query);
    }

    public static void deleteCity(String id){
        String query = "delete from city\nwhere id=" + id + ";";
        DB.exeUpdate(query);
    }
}
