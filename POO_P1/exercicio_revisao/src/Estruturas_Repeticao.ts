//5 Escreva um programa que imprima os números inteiros de 1 a 100.
for (let index = 1; index <= 100; index++) {
    console.log(index);
}


/*6 Escreva um programa que leia uma sequência de números inteiros terminada por –1 e
imprima na tela a soma e a média aritmética destes números. Obs: o valor –1 é
somente um terminador e não deve ser considerado nos cálculos. */
let numeros = [7, 7, 7];
console.log("Soma: ", numeros.reduce((acumullator, current) => {
    return acumullator + current;
}));

console.log("Média", numeros.reduce((acumullator, current, index) => {
    acumullator += current;
    if (index === numeros.length - 1) return acumullator / numeros.length
    return acumullator;
}));