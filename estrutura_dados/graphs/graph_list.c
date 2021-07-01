#include "graph_list.h"
#include <stdlib.h>
#include <stdio.h>

p_grafo criar_grafo(int n)
{
    p_grafo g = malloc(sizeof(p_grafo));
    g->n = n;
    g->adjacencia = malloc(n * sizeof(p_no));

    for (int i = 0; i < n; i++)
    {
        g->adjacencia[i] = malloc(sizeof(p_no));
        g->adjacencia[i]->prox = NULL;
        g->adjacencia[i]->v = i;
    }
    return g;
}

p_no insere_na_lista(p_no lista, int v)
{
    if (lista->prox != NULL)
    {
        return insere_na_lista(lista->prox, v);
    }
    else
    {
        p_no no = malloc(sizeof(p_no));
        no->v = v;
        no->prox = NULL;
        lista->prox = no;
        return lista;
    }
}

void insere_aresta(p_grafo g, int u, int v)
{
    g->adjacencia[v] = insere_na_lista(g->adjacencia[v], u);
    g->adjacencia[u] = insere_na_lista(g->adjacencia[u], v);
}