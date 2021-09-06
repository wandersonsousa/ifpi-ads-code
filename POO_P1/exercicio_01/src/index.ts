/* Verifique nas alternativas abaixo quais compilam ou não. Explique o motivo:*/

// a) let a = 10;
// a = "2";
console.log('RESPOSTA: Não compila, typescript tem inferência de tipo, a variável é tipada automaticamente para number')

// b) let b: any = 10;
//b = 2;
console.log('RESPOSTA: Compila, ambos são tipo number, e o tipo any entrega flexibilidade maior ao tratar tipos diferentes')

//c) let c: number = 10;
//c = 2;
console.log('RESPOSTA: Compila, ambos são do tipo number')

/* 2) Dada a função soma abaixo, tente executar os scripts das alternativas e exiba os
eventuais resultados:*/

function soma(x: number, y?: any): number {
    return x + y
}
// a) console.log(soma(1, 2));
console.log('RESPOSTA: 3')
// b) console.log(soma(1, "2"));
console.log('RESPOSTA: 12')
// c) console.log(soma(1));
console.log('RESPOSTA: NaN')




/* 3) Crie uma enum com as siglas dos estados “PI”, “CE”, “MA” e implemente as duas
 alternativas abaixo:*/

enum ESTADOS {
    PI = 'Piauí',
    CE = 'Ceará',
    MA = 'Maranhão'
}

// a) Crie um laço usando for para imprimir esses valores;
for (const key in ESTADOS) {
    console.log(ESTADOS[key])
}

// b) Crie um laço que imprima os índices dessa enum e diga o que aconteceu.
Object.keys(ESTADOS).forEach(key => console.log(key))
console.log('RESPOSTA: printou as keys')


/*4) Sobre enums, implemente o seguinte:*/
// a) Crie uma enum chamada DiasSemana com os valores representando os dias
// da semana segunda a domingo;
enum DiasSemana {
    Segunda = 1,
    Terca,
    Quarta,
    Quinta,
    Sexta,
    Sabado,
    Domingo
}
// b) Crie um namespace com mesmo nome e dentro dele crie uma função chamada
// isDiaUtil recebe um parâmetro do tipo DiasSema e retorna false se for um
// sábado ou domingo e retorna true caso contrário;
namespace DiasUtil {
    export function isDiaUtil(dia: DiasSemana): boolean {
        return dia !== DiasSemana.Sabado && dia !== DiasSemana.Domingo
    }
}
// c) Escreva também um script que declara uma variável do tipo da enum e que
// testa a função DiasSemana.isDiaUtil().
let dia: DiasSemana = DiasSemana.Sabado
console.log(DiasUtil.isDiaUtil(dia))
// 5) Crie uma função chamada exibir receba como parâmetro um “rest parameter”
// representando strings. A função deve exibir no log cada um dos elementos do “rest
// parameter”. Chame a função usando diferentes quantidade de parâmetros
// conforme abaixo:
// exibir(“a”, “b”);
// exibir(“a”, “b”, “c”);
// exibir(“a”, “b”, “c”, “d”);
function exibir(...args: string[]) {
    args.forEach(arg => console.log(arg))
}
exibir('a', 'b')
exibir('a', 'b', 'c')
exibir('a', 'b', 'c', 'd')
