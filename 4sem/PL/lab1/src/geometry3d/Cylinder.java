package src.geometry3d;

import src.Exceptions.IllegalResult;
import src.geometry2d.Figure;

public class Cylinder {
    protected Figure base;
    protected double height;
    public Cylinder(Figure f, double h){
        this.height = h;
        this.base = f;
    }

    public double Volume(){
        double result = 0;
        try{
            result = height*base.Area();
            if (result < 0) throw new IllegalResult();
        }
        catch(IllegalResult IllegalResult){
            IllegalResult.show(result);
            System.exit(1);
        }
        return result;
    }
}
