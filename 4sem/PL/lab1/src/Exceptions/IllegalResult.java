package src.Exceptions;

public class IllegalResult extends Exception {
        public IllegalResult(){}
        public void show(double result){
            System.out.println("Invalid result in function: " + result);
        }
}
