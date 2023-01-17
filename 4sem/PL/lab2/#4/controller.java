import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.scene.control.Button;
import javafx.scene.control.TextField;
import model.Calculator;

public class controller{
    @FXML
    Button btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn0,
    btnDot, btnPlus, btnMinus, btnMult, btnDiv, btnEqual, btnClear;
    @FXML
    TextField expr;

    double num1, num2;
    String currentOp = "";

    @FXML
    public void solve(ActionEvent event){
        Calculator calc = new Calculator();
        String[] nums = getNums();
        if (nums != null){
            num1 = Double.valueOf(nums[0]);
            num2 = Double.valueOf(nums[1]);
            double ans = 0;
            switch(currentOp) {
                case "\\+":
                    ans = calc.sum(num1, num2);
                    break;
                case "-":
                    ans = calc.minus(num1, num2);
                    break;
                case "\\*":
                    ans = calc.mult(num1, num2);
                    break;
                case "/":
                    ans = calc.div(num1, num2);
                    break;
            }
            String res = Double.toString(ans);
            if (res == "Infinity"){
                expr.setText("Divited by zero");
            }
            else{
                expr.setText(res);
            }
        }
        currentOp = "";
    }

    @FXML
    public void clickNum(ActionEvent event){
        String btnText = ((Button) event.getSource()).getText();
        if (expr.getText().equals("/") || expr.getText().equals("+") || expr.getText().equals("*")){
            expr.setText(btnText);
        }
        else{
            expr.setText(expr.getText() + btnText);
        }
    }

    @FXML
    public void clickOp(ActionEvent event){
        String btnText = ((Button) event.getSource()).getText();
        if (btnText.equals("C")){
            expr.setText("");
        }
        else if (btnText.equals("+")){
            currentOp = "\\+";
            expr.setText(expr.getText() + btnText);
        }
        else if (btnText.equals("-")){
            currentOp = "-";
            expr.setText(expr.getText() + btnText);
        }
        else if (btnText.equals("*")){
            currentOp = "\\*";
            expr.setText(expr.getText() + btnText);
        }
        else if (btnText.equals("/")){
            currentOp = "/";
            expr.setText(expr.getText() + btnText);
        }
    }

    public String[] getNums(){
        String text = expr.getText();
        if (currentOp != "" & !text.equals("-") & !text.equals("/") & !text.equals("+") & !text.equals("*")){
            String[] res = text.split(currentOp);
            return res;
        }
        String[] res = null;
        return res;
    }
}
