package src.Exceptions;

public class IllegalArgument extends Exception {
        protected String error;
        public IllegalArgument(String message){
                this.error = message;
            }
        public void show(){
            System.out.println("Error: " + error);
        }
}
