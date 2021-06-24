#include <stdio.h>
#include <stdlib.h>

typedef struct
{
    int **adjacencia;
    int n;

} Grafo;

typedef Grafo *p_grafo;
p_grafo criar_grafo(int n);

void destroi_grafo(p_grafo g);
void insere_aresta(p_grafo g, int u, int v);
void remove_aresta(p_grafo g, int u, int v);
void tem_aresta(p_grafo g, int u, int v);
void imprimi_arestas(p_grafo g);

int main(int argc, char const *argv[])
{
    p_grafo meuGrafo = criar_grafo(4);
    return 0;
}

p_grafo criar_grafo(int n)
{
    int i, j;
    p_grafo g = malloc(sizeof(Grafo));
    g->n = n;
    g->adjacencia = malloc(n * sizeof(int *));
    for (i = 0; i < n; i++)
        g->adjacencia[i] = malloc(n * sizeof(int *));

    for (i = 0; i < n; i++)
        for (j = 0; j < n; j++)
            printf("i = %d j = %d\n", i, j);

    return g;
}