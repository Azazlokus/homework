package src.geometry2d;

import src.Exceptions.IllegalArgument;

public class Square extends Rectangle {
    public Square(double sa) throws IllegalArgument{
        super(sa, sa);
        if(sa<0) throw new IllegalArgument("Invalid data in square constructor");
        this.sideA = sa;
        this.sideB = sa;
        this.name = "Square";
    } 
}
