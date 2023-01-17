package test;

import java.util.Scanner;

import src.Exceptions.IllegalArgument;
import src.geometry2d.Circle;
import src.geometry2d.Ellipse;
import src.geometry2d.Figure;
import src.geometry2d.Rectangle;
import src.geometry2d.Square;
import src.geometry2d.Triangle;
import src.geometry3d.Cylinder;

public class FigureApp {
    public Scanner sc = new Scanner(System.in);

    public Figure choice() throws IllegalArgument{
        double width, height;
        int key;
        System.out.println("1. Ellipse");
        System.out.println("2. Circle");
        System.out.println("3. Triangle");
        System.out.println("4. Rectangle");
        System.out.println("5. Square");
        System.out.println("0. Exit");
        System.out.print("Enter the number of figure(1-5): ");
        key = sc.nextInt();
        while(key<0 || key>5){
            System.out.println("Error input data");
            System.out.print("Key = ");
            key = sc.nextInt();
        }
        if (key == 0) System.exit(0);

        System.out.print("Enter the width and height of the figure: ");
        width = sc.nextInt();
        height = sc.nextInt();

        Figure r = new Square(1);
        try{
            if(key==1) r = new Ellipse(width, height);
            else if(key==2) r = new Circle(width);
            else if(key==3) r = new Triangle(width, height);
            else if(key==4) r = new Rectangle(width, height);
            else if(key==5) r = new Square(width);
        } catch(IllegalArgument IllegalArgument){
            IllegalArgument.show();
            System.exit(1);
        }
        return r;
    }

    public void show(Figure r){
        String name = r.show();
        System.out.println(name);
        System.console().readLine();
    }

    public void outArea(Figure r){
        System.out.println("Area: " + r.Area());
        System.console().readLine();
    }

    public void outVolume(Figure r){
        double h;
        System.out.print("Enter the height of the cylinder: ");
        h = sc.nextDouble();    
        Cylinder Cylinder = new Cylinder(r, h);
        System.out.println("Volume = " + Cylinder.Volume());
        System.console().readLine();
    }

    public void Menu(Figure r) throws IllegalArgument{
        int key;
        do{
            System.out.println("------------");
            System.out.println("1. Show name of figure");
            System.out.println("2. Area of figure");
            System.out.println("3. Volume of cylinder");
            System.out.println("4. Choice figure");
            System.out.println("0. Exit");
            System.out.println("------------");
            System.out.print("Enter: ");
            key = sc.nextInt();
    
            switch(key){
                case 1:  show(r); break;
                case 2:  outArea(r); break;
                case 3:  outVolume(r); break;
                case 4:  r = choice(); break;
                case 0:  break;
                default:   
                          System.out.println("Error data, try again..."); 
                          System.console().readLine();
            }
        }while(key > 0);
        sc.close();
    }

    public void start() throws IllegalArgument{
        Figure r = choice();
        Menu(r);
    }
}
