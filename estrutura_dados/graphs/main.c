#include "digraph.c"

int main(int argc, char const *argv[])
{
    p_grafo meuGrafo = criar_digrafo(4);
    insere_aresta(meuGrafo, 2, 2);
    insere_aresta(meuGrafo, 0, 1);
    insere_aresta(meuGrafo, 0, 2);
    insere_aresta(meuGrafo, 1, 0);
    insere_aresta(meuGrafo, 1, 2);
    insere_aresta(meuGrafo, 2, 0);
    insere_aresta(meuGrafo, 2, 1);
    insere_aresta(meuGrafo, 3, 1);

    //printf("Grau do Node A: %d\n", grau(meuGrafo, 0));
    //printf("Quem é o bichão ? - é o %d\n", mais_popular(meuGrafo));

    //imprime_recomendacoes(meuGrafo, 3);
    imprime_arestas(meuGrafo);
    return 0;
}