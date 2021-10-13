/* 1. Suponha uma classe Hotel que sirva apenas para guardar a quantidade de
solicitações de reservas feitas conforme abaixo:*/

/*
 class Hotel {
    quantReservas: number;
    adicionarReserva(): void {
        quantReservas++;
    }
} 
*/

/* Podemos afirmar que haverá um problema de compilação, pois a variável inteira não
foi inicializada previamente? Justifique. */
console.log('Sim, quantReserva precisa ser iniciada como valor 0 no processo de instantiação da classe, ou no construtor, e para utilizar é necessário um this')

/* 2. Ainda sobre a classe do exemplo anterior, considere o método main abaixo:
let hotel : Hotel = new Hotel(2);
console.log(hotel.quantReservas);
Adicione o construtor que aceite um parâmetro inteiro e faça a inicialização do atributo
quantReservas. */

class Hotel {
    public quantReservas: number = 0;
    constructor(quantReservas: number) {
        this.quantReservas = quantReservas;
    }
    adicionarReserva(): void {
        this.quantReservas++;
    }
}

/* 3. Considere a classe Radio e as instruções fazem seu uso abaixo:*/

/* class Radio {
    volume: number;
    constructor(volume: number) {
        this.volume = volume;
    }
}
let r: Radio = new Radio();
r.volume = 10; */

/*Justifique o erro de compilação e proponha uma solução. */
console.log('A classe rádio requer um argumento volume no construtor, uma solução usar um default value para o paramêtro volume.')
/*
4. Considerando o uso da classe Conta apresentada em aula e seu uso abaixo:
let c1 : Conta = new Conta("1",100);
let c2 : Conta = new Conta("2",100);
c1 = c2;
c1.sacar(10);
c1.tranferir(c2,50);

console.log(c1.saldo);
console.log(c2.saldo); */

//a. Qual o resultado dos dois "prints"? Justifique sua resposta.
console.log('O resultado vai ser 90, após a instrução que iguala as duas contas, ambas as variáveis apontam para o mesmo objeto, portanto o método transferir que vai subtrair da conta de origem e adicionar da conta de destino estará tratando da mesma conta, anulando ambas as intruções.')
//b. O que acontece com o objeto para o qual a referência c1 aponta?
console.log('O garbage colector manda pro saco')
/* 5. Crie uma classe chamada Jogador e nela: */
//a. Crie 3 atributos inteiros representando força, nível e pontos atuais;
//b. Crie um construtor no qual os 3 parâmetros são passados e inicialize os respectivos atributos;
//c. Crie um método que calcule os pontos relativos a um ataque que são calculados pela multiplicação de força pelo nível;
// d. Crie um método chamado atacar em que é passado um outro jogador como parâmetro e é feita a subtração de pontos de tal jogador baseado na quantidade de pontos do jogador atual (“this”).
// e. Avalie em com testes dois jogadores instanciados e inicializados através do construtor. Utilize o método de ataque de cada jogador e ao final, verifique qual jogador tem mais pontos.

class Jogador {
    constructor(public forca: number = 0, public nivel: number = 0, public pontosAtuais: number = 0) { }

    calcularPontosDeAtaque() {
        return this.forca * this.nivel
    }

    atacar(jogadorAlvo: Jogador) {
        jogadorAlvo.pontosAtuais -= this.calcularPontosDeAtaque()
    }
}

const jogadorNumeroUm = new Jogador(10, 5, 20)
const jogadorAlvo = new Jogador(1, 1, 1)
jogadorNumeroUm.atacar(jogadorAlvo)
console.log(jogadorNumeroUm.pontosAtuais > jogadorAlvo.pontosAtuais ? 'Jogador número um tem mais pontos!' : 'Jogador alvo tem mais pontos!')


/* 6. Altere a classe conta dos slides conforme as instruções abaixo: */
//a. Altere o método sacar de forma que ele retorne verdadeiro ou falso. Caso o saque deixe saldo negativo, o mesmo não será realizado, retornando falso;
//b. Altere o método transferir() para que o mesmo use os métodos sacar() e depositar(). Visto pelo prisma da "proteção do saldo", chamar outros métodos em vez de acessar o saldo diretamente é mais seguro?
// c. Altere o método transferir() para que retorne também um valor lógico e que não seja feita a transferência caso o sacar() na conta origem não seja satisfeito;
// d. Verifique as diferentes operações implementadas.
class Conta {
    private numero: string = "0"
    constructor(public id: string, private saldo: number = 0) { }
    creditar(valor: number): boolean {
        if (this.saldo - valor < 0) return false
        this.saldo -= valor
        return true
    }

    depositar(valor: number) {
        this.saldo += valor;
    }
    transferir(destino: Conta, valor: number): boolean {
        if (!this.creditar(valor)) return false

        destino.depositar(valor)
        return true
    }
    mostrarSaldo() {
        return this.saldo
    }
}


/* 7. Crie uma classe chamada Produto e nela: */
// a. Crie os atributos codigo, descricao, valor e um construtor que os inicialize;
// b. Crie os métodos baixar(quantidade : number) e repor(quantidade : number) que reduzem e incrementam a quantidade disponível do produto;
// c. Crie um atributo quantidadeMinima e reescreva o método baixar para que não seja possível realizar a baixa caso a operação deixe a quantidade abaixo da quantidade mínima;
// d. Crie um método da classe Produto chamado reajusta(taxa : number) que reajusta em x% o valor do produto.
// e. Crie um método chamado toString() que retorna a representação textual do produto concatenando todos os atributos.
// f. Crie um método equals(Produto produto) que retorna true ou false se o produto passado como parâmetro possui o mesmo código;
// g. Verifique as diferentes operações implementadas com testes.
class Produto {
    constructor(public codigo: string = "", public descricao: string = "", public valor: number = 0, public quantidade: number = 0, public quantidadeMinima = 0) {

    }
    baixar(quantidade: number) {
        if (this.quantidade - this.quantidadeMinima) return null
        this.quantidade -= quantidade
    }
    repor(quantidade: number) {
        this.quantidade += quantidade
    }
    reajusta(taxa: number) {
        this.valor += (this.valor * taxa / 100)
    }
    toString() {
        return `Produto de código: ${this.codigo}\nDesc: ${this.descricao}\nValor: ${this.valor}\nQuantidade Disponível: ${this.quantidade}\nQuantidade Mínima: ${this.quantidadeMinima}`
    }
    equals(produto: Produto) {
        return this.codigo === produto.codigo
    }

}

const xbox = new Produto("xbox1234", "Melhor videogame da geração", 1500, 10, 5)
const playstation = new Produto("play41313", "Segundo melhor videogame", 2500, 50, 8)
console.log(xbox.equals(playstation))
console.log(xbox.toString())