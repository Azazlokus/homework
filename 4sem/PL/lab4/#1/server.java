import java.io.InputStream;
import java.io.OutputStream;
import java.net.ServerSocket;
import java.net.Socket;
import model.Calculator;


class Server {
	byte[] expr = new byte[2000];
	byte[] op = new byte[100];
	String wordOp, wordExpr;
	double ans = 0, num1, num2;
	ServerSocket ss;
	Socket s;
    InputStream in;
    OutputStream out;
	Calculator calc;

	
	public void initialize() {
		try{
			ss = new ServerSocket(1111);           
			System.out.println("Waiting connection...");	
			s = ss.accept();
			System.out.println("Connection accepted");	
			in = s.getInputStream();
			out = s.getOutputStream();
			calc = new Calculator();
		} catch (Exception e) {
			e.printStackTrace();
		}
	}

	public void getData(){
		System.out.println("Getting data...");
		try{
			int countEx = in.read(expr);
			wordExpr = new String(expr,0, countEx);
			int countOp = in.read(op);
			wordOp = new String(op, 0, countOp);
			String[] res = wordExpr.split(wordOp);
			num1 = Double.valueOf(res[0]);
			num2 = Double.valueOf(res[1]);
			System.out.println("\tExpression: " + wordExpr);
		} catch (Exception e){
			try{
				s.close();
				ss.close();
				in.close();
				out.close();
				System.out.println("Socket closed");
				System.out.println("Connection closed");
				System.exit(0);
			} catch (Exception exp){
				exp.printStackTrace();
			}
		}
	}

	public void sendData(String res){
		System.out.println("Sending data...");
		try{
			out.write(res.getBytes());
			System.out.println("\tResult: " + res);
		} catch (Exception e){
			e.printStackTrace();
		}
	}

	public String solve(double num1, double num2){
		switch(wordOp) {
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
		return res;
	}

	public void start(){
		initialize();
		while (true){
			getData();
			String res = solve(num1, num2);
			sendData(res);
		}
	}

	public static void main(String[] args) {
        Server s = new Server();
		s.start();
	}

}