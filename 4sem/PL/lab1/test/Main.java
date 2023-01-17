package test;
import src.Exceptions.IllegalArgument;
import src.Exceptions.IllegalResult;

public class Main{
    public static void main(String[] args) throws IllegalArgument, IllegalResult{
        FigureApp app = new FigureApp();
        app.start();
    }
}
