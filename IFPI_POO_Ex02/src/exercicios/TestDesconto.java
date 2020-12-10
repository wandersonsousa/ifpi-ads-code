package exercicios;
import exercicios.Desconto;

public class TestDesconto {
	public static void main(String[] args) {
		Desconto desconto = new Desconto();	
		
		desconto.valorOriginal = 1000;
		desconto.desconto = 25;
		
		System.out.println( desconto.calcula() );
	}
	
}
