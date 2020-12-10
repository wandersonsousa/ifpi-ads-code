package exercicios;

public class Desconto {
	public double valorOriginal, desconto;
	public double calcula() {
		return this.valorOriginal * (1 - this.desconto / 100);
	}
}
