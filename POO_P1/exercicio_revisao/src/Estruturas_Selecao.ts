//3 Escrever um programa que leia três valores inteiros e apresente o menor dos valores lidos
const num1: number = 2;
const num2: number = 10;
const num3: number = 15;

if (num1 > num2 && num1 > num3) {
    console.log(num1 + ' é o maior número');
}
if (num2 > num1 && num2 > num3) {
    console.log(num2 + ' é o maior número');
}
if (num3 > num2 && num3 > num1) {
    console.log(num3 + ' é o maior número');
}

//4 Escreva um programa que apresente o mês por extenso, a partir de um número digitado pelo usuário (entre 1 e 12).
const meses = [
    {
        id: 1,
        nome: "Janeiro"
    },
    {
        id: 2,
        nome: "Fevereiro"
    },
    {
        id: 3,
        nome: "Março"
    },
    {
        id: 4,
        nome: "Abril"
    },
    {
        id: 5,
        nome: "Maio"
    },
    {
        id: 6,
        nome: "Junho"
    },
    {
        id: 7,
        nome: "Julho"
    },
    {
        id: 8,
        nome: "Agosto"
    },
    {
        id: 9,
        nome: "Setembro"
    },
    {
        id: 10,
        nome: "Outubro"
    },
    {
        id: 11,
        nome: "Novembro"
    },
    {
        id: 12,
        nome: "Dezembro"
    }
]

const mesEntrada: number = 12;
const [mes] = meses.filter(mes => mes.id === mesEntrada);
console.log(mes.nome);