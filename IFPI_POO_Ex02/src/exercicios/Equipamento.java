package exercicios;

public class Equipamento {
	public Boolean ligado = false;
	public String nome;
	
	public void liga() {
		if(!this.ligado) {
			this.ligado = true;
		}
	}
	public void desliga() {
		if(ligado) {
			this.ligado = false;
		}
	}
	public void inverte() {
		this.ligado = !this.ligado;
	}
	public Boolean estaLigado() {
		return this.ligado;
	}
	
}
