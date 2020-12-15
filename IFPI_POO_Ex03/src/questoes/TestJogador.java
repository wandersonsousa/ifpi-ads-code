package questoes;
import questoes.*;

public class TestJogador {

	public static void main(String[] args) {
		Jogador j1 = new Jogador(100, 1, 400);
		Jogador j2 = new Jogador(200, 2, 800);
		
		j1.atacar(j2);
		j2.atacar(j1);
		
		System.out.println("pontos Jogador 1: " + j1.pontosAtuais);
		System.out.println("pontos Jogador 2: " + j2.pontosAtuais);
	}

}
