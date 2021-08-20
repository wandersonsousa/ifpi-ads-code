/* 7. Escreva um programa que leia um vetor de 5 posições e apresente-o na tela.*/
const vetorLido = [1, 23, 7, 45, 5];
vetorLido.forEach(e => console.log(e));

/*8. Escreva um programa que leia e mostre um vetor de 20 elementos inteiros. A seguir,
conte quantos valores pares existem
no vetor. */
const vetorVinte = [1, 23, 54, 5, 6, 7, 7, 8, 9, 2, 3, 5, 2, 2, 3, 4, 5, 6, 7, 2, 12];
console.log("Existem ", vetorVinte.filter(el => el % 2 == 0).length, "valores pares no array");

/* 9. Construir um programa que leia uma string s, e dois caracteres a e b. Em seguida, o
programa deve substituir todas as ocorrências do caractere a na string s pelo caractere
b. */
const s = "ww";
const a = 'w';
const b = 'a';
console.log(s.replaceAll(a, b));


/*10 Escreva um programa que leia um texto pelo teclado e remova todas as suas vogais.
Exiba a string resultante. */
let texto = "Wanderson";
const vogais = ['a', 'e', 'i', 'o', 'u'];
vogais.forEach(vogal => {
    texto = texto.replaceAll(vogal, "1");
});
console.log(texto);