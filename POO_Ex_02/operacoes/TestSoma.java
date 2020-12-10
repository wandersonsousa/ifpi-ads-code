package operacoes;
import operacoes.Soma;

public class TestSoma {
	
	
	public static void main(String[] args) {
		Soma soma = new Soma();
		soma.n1 = 2;
		soma.n2 = 10;
		
		System.out.println( soma.calculaSoma() );
	}
	
}
