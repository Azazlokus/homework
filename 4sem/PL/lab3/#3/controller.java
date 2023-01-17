import javafx.application.Platform;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.scene.control.Button;
import javafx.scene.control.ProgressBar;

public class controller{
    public static boolean isSuspend = false;
    public static boolean isStart = false;
    public static boolean isStop = false;
    @FXML
    Button start, pause, stop;
    @FXML
    ProgressBar progress;

    @FXML
    private void startProgress(ActionEvent event){
        if (!isSuspend){
            new NewThread("Parallel;", progress, start, stop);
        }
    }

    @FXML
    private void pauseProgress(ActionEvent event){
        if (!isSuspend){
            pause.setText("Continue");
        }
        else{
            pause.setText("Pause");
        }
        isSuspend = !isSuspend;
    }


}

class NewThread implements Runnable{
    ProgressBar progress;
    Button start, pause, stop;

    NewThread(String name, ProgressBar progress, Button start, Button stop){
        this.start = start;
        this.stop = stop;
        this.progress = progress;
        Thread t = new Thread(this, name);
        System.out.println("Thread start: " + t.getName());
        t.start();
    }

    public void run(){
        Thread t =  Thread.currentThread();
		System.out.println(t.getName() + ":run");

            for(int i = 1; i<=1000; i++){

                if (start.isPressed() || stop.isPressed()){
                    progress.setProgress(0);
                    t.interrupt();
                    break;
                }

                while(controller.isSuspend){
                    try {
                        wait(0);
                    } catch (Exception e) {}
                }

                final double j = i;    	   
                Platform.runLater(new Runnable() { 
                    @Override
                    public void run() {
                        progress.setProgress(j/1000);	      
                    }
                });
                try {t.sleep(20);} catch (Exception e) {}
            }
        
        t.interrupt();
    }
}

