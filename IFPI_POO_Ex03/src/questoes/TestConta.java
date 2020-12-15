package questoes;

public class TestConta {
    public static void main(String[] args) {
        Conta c1 = new Conta("1", 100);
        Conta c2 = new Conta("2", 100);
        c1 = c2;
        c1.sacar(10);
        c1.transferir(c2, 50);

        System.out.println( c1.consultarSaldo() );
        System.out.println( c2.consultarSaldo() );

    }
}
