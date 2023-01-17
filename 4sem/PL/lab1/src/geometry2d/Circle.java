package src.geometry2d;

import src.Exceptions.IllegalArgument;

public class Circle extends Ellipse {
        public Circle(double r) throws IllegalArgument{
                super(r, r);
                if(r<0) throw new IllegalArgument("Invalid data in circle constructor");
                bigA = r;
                smA = r;
                name = "Circle";
            }
}
