package operacoes;
import operacoes.DecimalNumber;

public class TestDecimalNumber {
	public static void main(String[] args) {
		DecimalNumber d = new DecimalNumber();
		d.D = 100;
		
		System.out.println( d.returnInteger() );
		System.out.println( d.returnDecimal() );
	}
}
