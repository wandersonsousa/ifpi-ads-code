package exercicios;

public class TestSaudacao {
	public static void main(String[] args) {
		Saudacao saudacao = new Saudacao();
		saudacao.texto = "Boa noite";
		saudacao.destinatario = "Someone";
		System.out.println(saudacao.obterSaudacao());
	}
}
