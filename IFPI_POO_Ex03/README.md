# Questão 01
- O interpretador java irá atribuir o valor 0 para a variável, então não haverá erros

# Questão 02
- Erro, pois a classe não tem construtor declarado

# Questão 03
- Saída será 0, pois o construtor da classe está referenciando a váriavel A de seu escopo, e não da classe

# Questao 04
- O metódo está fazendo alterações em variáveis apenas do seu próprio escopo 
```Java
void x(double valor) {
    this.valor = this.valor + valor;
}
```
# Questao 05
- Erro, pois a classe necessita que um argumento seja passado em sua inicialização, para o construtor
```Java
public class TestaRadio {
    public static void main(String[] args) {
        Radio r = new Radio(10);
    }
}
```

# Questao 06
- A) 90 e 90, ambas referenciam o mesmo endereço de memória. 
- B) É limpo da memória pelo garbage collection, pois C1 agora aponta para outro endereço.
```Java
public class TestaRadio {
    public static void main(String[] args) {
        Radio r = new Radio(5);
        r.volume = 10;
    }
}
```