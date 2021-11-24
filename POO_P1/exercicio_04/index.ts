/* 1. Crie um array de números em typescript e escreva um código que exibe a soma
dos elementos.*/
const nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
let soma = 0;
for (let i = 0; i < nums.length; i++) {
    soma += nums[i];
}
console.log(soma);



/*2. Considere o trecho de código abaixo e descreva o que acontece com a execução
do código abaixo:
let a : number[] = [1,2,3,4,5];
for (let i : number = 0; i <= a.length; i++) {
console.log(a[i]);
}*/
console.log('Vai printar todos os números dentro do array')

/*
3. Declare um array com 10 números e exiba-os em ordem crescente e em ordem
decrescente.*/
const nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
console.log(nums2.sort());
console.log(nums2.reverse());

/*4. Declare uma string com o texto “Instituto Federal do Piauí” e use métodos específicos
para:*/
const texto = 'Instituto Federal do Piauí';
//a. Exibir a string toda em maiúsculo;
console.log(texto.toUpperCase());
//b. Retornar o caractere da posição 10;
console.log(texto.charAt(10));
//c. Retornar a última posição da vogal “o”;
console.log(texto.lastIndexOf('o'));
//d. Dividir a frase em um array de strings tendo como delimitador os caracteres de espaço. 
console.log(texto.split(' '));