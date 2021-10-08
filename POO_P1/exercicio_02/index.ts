/* 1. Qual a diferença entre objetos e classes? Exemplifique. */
console.log('Classes são como a interface de objetos, elas que irão definir quais os comportamentos e estados que um objeto terá, pode se dizer que funciona como uma fábrica de estrutura de dados, a partir dela definimos novas estruturas de dados que serão representadas de forma concreta com objetos.')

/* 2. De forma breve, conceitue atributos e métodos. Pesquise e exemplifique um
exemplo de objeto que possua atributos e métodos (notação livre). */
console.log('Atributos são como variáveis escopadas dentro de uma classe, métodos são funções com escopo dentro da classe. Um objeto cachorro pode ter os atributos idade e nome, e os métodos comer e latir.')

/* 3. A abstração visa focar no que é importante para um sistema. Você concorda que
um atributo de uma pessoa pode ser importante ou não dependendo do contexto
do sistema. Enumere na tabela abaixo contextos/sistemas distintos em que os
atributos abaixo seriam ou não relevantes:

Atributo Sistema em que é
importante
- Sistema de clínica médica
- Sistema de coleta de dados de pessoas para o diagnóstico de doenças
Sistema em que
não é importante
- Sistema de gestão de estoque
- Sistema de gestão de pessoas
- Sistema de Apostas de futebol

Peso
Tipo de CNH
Tipo Sanguíneo
Habilidade destra
Percentual de gordura
Saldo em conta
Etinia */



/* 4. Considerando os objetos Pessoa e Conta:*/

/* a. Seria interessante em um sistema bancário um objeto "conta" possuir uma
"pessoa" como um atributo interno representando o titular da conta? */
console.log('Não, pois isso resultaria num grande acoplamento e dependência entre os objetos, uma solução mais viável seria representar uma determinada conta por ID e salvar este setar este ID em cada objeto pessoa.')

/* b. Olhando no sentido inverso, seria interessante uma pessoa possuir mais de
uma conta como atributo? Que elemento da programação estruturada melhor
representaria o conjunto de contas de uma pessoa? */
console.log('Um set funcionaria bem, já que não podem haver contas repetidas.')

/* 5. Identifique pelo menos 5 objetos de um sistema de controle acadêmico. Ex: aluno.*/
console.log('Aluno', 'Turma', 'Disciplina', 'Professor', 'Boletim')

/* 6. Imagine um jogo qualquer. Identifique o máximo de objetos possíveis e eventuais
características (atributos) e comportamentos (métodos) que os mesmos poderiam
ter. */
console.log('Em um RPG, existiria a classe jogador que conteria os atributos vida, arma, dano, defesa e métodos atacar, defender. Uma classe de monstro pode ser adicionada, com atributos parecidos mas teria limitações como exemplo, o uso de armas seria proibido, só podendo usar o ataque base.')

/* 7. Considerando o exemplo da classe Retangulo dos slides, implemente um método
adicional chamado que calcule o perímetro do retângulo e altere a classe
TestaRetangulo para exibir o cálculo do perímetro. */

class Retangulo {
    constructor(private altura: number = 0, private largura: number = 0) {
    }

    calculaArea(): number {
        return this.altura * this.largura;
    }

    calculaPerimetro(): number {
        return (this.altura + this.largura) * 2;
    }
}


/* 8. Crie uma classe Circulo que possua um atributo raio. Crie dois métodos que
calculam a área e o perímetro. Instancie um objeto dessa classe, atribua um valor
ao raio e exiba a área e o perímetro chamando os dois métodos definidos. */

class Circulo {
    constructor(private raio: number = 0) {
    }
    calculaArea(): number {
        return Math.PI * Math.pow(this.raio, 2);
    }
    calculaPerimetro(): number {
        return 2 * Math.PI * this.raio;
    }
}
const circulo = new Circulo(5);
console.log(`Área do circúlo: ${circulo.calculaArea()}`)
console.log(`Perimétro do circulo: ${circulo.calculaPerimetro()}`)

/* 9. Crie uma classe chamada SituacaoFinanceira com os atributos valorCreditos e
valorDebitos. Crie um método chamado saldo() que retorna/calcula a diferença
entre crédito e débito. Instancie uma classe SituacaoFinanceira, inicialize os dois
atributos e exiba o resultado do método saldo(). */

class SituacaoFinanceira {
    constructor(private valorCreditos: number = 0, private valorDebitos: number = 0) {
    }

    saldo(): number {
        return this.valorCreditos - this.valorDebitos
    }
}

const minhaSituacaoFinanceira = new SituacaoFinanceira(100, 50)
console.log(`Situação financeira, saldo: ${minhaSituacaoFinanceira.saldo()}`)