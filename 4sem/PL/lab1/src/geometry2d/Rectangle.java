package src.geometry2d;

import src.Exceptions.IllegalArgument;

public class Rectangle implements Figure {
    protected double sideA, sideB;
    protected String name = "Rectangle";
    public Rectangle(double sa, double sb) throws IllegalArgument{
        if(sa<0 || sb<0) throw new IllegalArgument("Invalid data in rectangle constructor");
        this.sideA = sa;
        this.sideB = sb;
    }
    
    @Override
    public double Area(){
        return sideA*sideB;
    } 

    @Override
    public String show() {
        return name;
    }
}
