package exercicios;
import exercicios.Equipamento;

public class TestaEquipamentos {
	public static void main(String[] args) {
		Equipamento equipamento = new Equipamento();
		Equipamento outroEquipamento = new Equipamento();
		
		equipamento.nome = "Lava Louças";
		outroEquipamento.nome = "Boneca XLR de 9 modos";
		
		equipamento.liga();
		outroEquipamento.desliga();
		
		equipamento.inverte();
		outroEquipamento.inverte();
		
		TestaEquipamentos.printarEstado(equipamento);
		TestaEquipamentos.printarEstado(outroEquipamento);
	}
	
	private static void printarEstado( Equipamento eq ) {
		if(eq.estaLigado()) {
			System.out.println("O equipamento " + eq.nome + " está ligado");
		}else {
			System.out.println("O equipamento " + eq.nome + " está desligado");
		}
	}
}
