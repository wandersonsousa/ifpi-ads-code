package questoes;

public class Produto {
    int codigo;
    String descricao;
    double valor;
    int quantidade;
    int quantidadeMinima = 10;

    Produto(int codigo, String descricao, double valor, int quantidade){
        this.codigo = codigo;
        this.descricao = descricao;
        this.valor = valor;
        this.quantidade = quantidade;
    }

    boolean baixar(int quantidade){
        if (this.quantidade - quantidade < quantidadeMinima) {
            return false;
        } else {
            this.quantidade -= quantidade;
            return true;
        }
    }

    void repor(int quantidade){
        this.quantidade += quantidade;
    }

    void reajusta(double taxa) {
        this.valor += ((this.valor / 100) * taxa);
    }

    public String toString(){
        return "Codigo: " + this.codigo + "\nDescricao: " + this.descricao + "\nValor: R$" + this.valor + "\nQuantidade: " + this.quantidade;
    }

}