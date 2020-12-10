package exercicios;

public class NumberUtils {
	public int n;
	public Boolean isPair() {
		return this.n % 2 == 0;
	}
	public Boolean isOdd() {
		return !this.isPair();
	}
	public Boolean isPrime() {
		boolean isPrimo = true;
		for (int i = 2; i <= this.n; i++) {
			if ( ( (this.n % i) == 0) && (i != this.n) ) {
				isPrimo = false;
				break;
			}
		}
		if (isPrimo) {
			return true;
		}
		return false;

	}
	public void printCount() {
		for (int i = 0; i <= this.n; i++) {
			System.out.print( i + ", " );
		}
	}
	public void printReverseCount() {
		for (int i = this.n; i >= 0; i--) {
			System.out.print( i + ", " );
		}
	}
}
