package saudacoes;
import saudacoes.Saudacao;

public class TestaSaudacao {
	public static void main(String[] args) {
		Saudacao saudacao = new Saudacao();
		saudacao.texto = "Boa noite";
		saudacao.destinatario = "Someone";
		System.out.println(saudacao.obterSaudacao());
	}
}
