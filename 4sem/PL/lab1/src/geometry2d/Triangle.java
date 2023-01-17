package src.geometry2d;

import src.Exceptions.IllegalArgument;

public class Triangle implements Figure{
        protected double base, height;
        protected String name = "Triangle";
        public Triangle(double sa, double sh) throws IllegalArgument{
            if(sa<=0 || sh<=0) throw new IllegalArgument("Invalid data in triangle constructor");
                this.base = sa;
                this.height = sh;
            }
    
        @Override
        public double Area(){
                return base*height/2;
            }
        
        @Override
        public String show() {
            return name;
        }
}
