import javafx.application.Platform;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.scene.control.Button;

public class controller{
    @FXML
    Button btn;

    @FXML
    private void click(ActionEvent event){
        //new NewThread("Paralle;", btn); // Реализация потока через implements Runnable
        Thread t = new NewThread2("Paralle;", btn); // // Реализация потока через extends Thread
        t.start();
    }

    @FXML
    private void clickError(ActionEvent event){
        while(true){

        }
    }
}

class NewThread implements Runnable{
    Button btn;

    NewThread(String name, Button btn){
        this.btn = btn;
        Thread t = new Thread(this, name);
        System.out.println("Thread start: " + t.getName());
        t.start();
    }

    public void run(){
        Thread t =  Thread.currentThread();
		System.out.println(t.getName() + ":run");		        	   
		int i = 1;
		Platform.runLater(new Runnable() { 
            @Override
            public void run() {
                btn.setText("Infinity cycle is started");	      
            }
        });
        while(true){                       
            System.out.println(t.getName() + " Count: " + i);
            try {t.sleep(1000);} catch (Exception e) {}
            i++;    
        }	  
    }
}

class NewThread2 extends Thread{
    Button btn;

    NewThread2(String name, Button btn){
        super(name);
        this.btn = btn;
    }

    public void run(){
        Thread t =  Thread.currentThread();
		System.out.println(t.getName() + ":run");		        	   
		int i = 1;
		Platform.runLater(new Runnable() { 
            @Override
            public void run() {
                btn.setText("Infinity cycle is started");	      
            }
        });
        while(true){                       
            System.out.println(t.getName() + " Count: " + i);
            try {t.sleep(1000);} catch (Exception e) {}
            i++;    
        }	  
    }
}