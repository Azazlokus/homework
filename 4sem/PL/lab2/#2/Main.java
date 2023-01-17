import javafx.application.Application;
import javafx.stage.Stage;
import javafx.scene.Scene;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
 
public class Main extends Application{
    public static void main(String[] args) {		
        Application.launch(args);	
    }
     
    @Override
    public void start(Stage stage) throws Exception {
         
        Parent root = FXMLLoader.load(getClass().getResource(".\\view.fxml")); 
        Scene scene = new Scene(root);
         
        stage.setScene(scene);
         
        stage.setTitle("#2");
        stage.setWidth(350);
        stage.setHeight(250);
        stage.show();
    }
}