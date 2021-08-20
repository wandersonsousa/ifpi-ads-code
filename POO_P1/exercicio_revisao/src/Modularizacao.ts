/*11. Escreva uma função que dados 2 valores reais p e x calcule e retorne quanto vale p
por cento de x */

function percent(p: number, x: number) {
    return ((x * p) / 100);
}
console.log(percent(50, 100));



/* 12. Faça uma função que recebe por parâmetro uma medida de tempo expressa em
segundos e retorna, também por parâmetro, esse tempo em horas, minutos e
segundos no formato: “hh:mm:ss”. */

function formatarTempo(segundos: number) {
    const horas = Math.floor(segundos / 3600);
    const restoHoras = segundos % 3600;
    const minutos = Math.floor(restoHoras / 60);
    const restoMinutos = restoHoras % 60;
    const seg = restoMinutos;
    console.log(`${horas} horas ${minutos} minutos e ${seg} segundos`);
}
formatarTempo(3600);


/*13. Escreva uma função que dados um inteiro n e um inteiro d, onde 0 < d ≤ 9, devolve
quantas vezes o dígito d aparece no número n. Por exemplo: se n = 7677 e d = 7, a
função deve retornar 3. */

function contarRepeticao(n: number, d: number) {
    return n.toString().split('').map(n => parseInt(n)).filter(n => n === d).length;
}
console.log("O número se repete:", contarRepeticao(111, 1), "vezes");