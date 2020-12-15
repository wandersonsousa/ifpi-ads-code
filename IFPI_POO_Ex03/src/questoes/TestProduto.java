package questoes;


		public class TestProduto {
		    public static void main(String[] args) {
		        Produto p1 = new Produto(333, "arroz", 30, 100);
		        p1.baixar(54); 
		        p1.repor(30); 
		        p1.reajusta(10);
		        
		        System.out.println(  p1.toString() );
		    }
		}

