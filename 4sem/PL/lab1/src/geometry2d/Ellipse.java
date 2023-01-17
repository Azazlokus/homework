package src.geometry2d;

import src.Exceptions.IllegalArgument;

public class Ellipse implements Figure{
        protected String name = "Ellipse";
        protected double bigA, smA;
        public Ellipse(double ba, double sa) throws IllegalArgument{
            if(ba<0 || sa<0) throw new IllegalArgument("Invalid data in ellipse constructor");
            this.bigA = ba;
            this.smA = sa;
        }
        
        @Override
        public double Area(){
                return 3.14*bigA*smA;
            }

        @Override
        public String show() {
            return name;
        }
}
