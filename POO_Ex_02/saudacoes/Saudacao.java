package saudacoes;
public class Saudacao {
	public String texto;
	public String destinatario;
	
	public String obterSaudacao() {
		return this.texto + ", " + this.destinatario;
	}
	
}
