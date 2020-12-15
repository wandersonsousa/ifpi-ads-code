package questoes;

public class Jogador {
	int forca, nivel, pontosAtuais;
	Jogador(int f, int n, int p){
		this.forca = f;
		this.nivel = n;
		this.pontosAtuais = p;
	}
	
	public int forcaDeAtaque() {
		return this.forca * this.nivel;
	}
	public void atacar( Jogador alvo ) {
		alvo.pontosAtuais -= this.forcaDeAtaque();
	}
}

