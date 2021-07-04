#include "graph_list.h"
#include <stdlib.h>
#include <stdio.h>

p_grafo criar_grafo(int n)
{
    p_grafo g = malloc(sizeof(p_grafo));
    g->n = n;
    g->adjacencia = malloc(g->n * sizeof(p_no));

    for (int i = 0; i < g->n; i++)
    {
        g->adjacencia[i] = malloc(sizeof(p_no));
        g->adjacencia[i]->v = i;
        g->adjacencia[i]->prox = NULL;
    }
    return g;
}

p_no insere_na_lista(p_no lista, int v)
{
    p_no novo = malloc(sizeof(No));
    novo->v = v;
    novo->prox = lista;
    return novo;
}

void insere_aresta(p_grafo g, int u, int v)
{
    g->adjacencia[u] = insere_na_lista(g->adjacencia[u], v);
    g->adjacencia[v] = insere_na_lista(g->adjacencia[v], u);
}

void libera_lista(p_no lista)
{
    if (lista != NULL)
    {
        libera_lista(lista->prox);
        free(lista);
    }
}

p_no remove_da_lista(p_no lista, int v)
{
    p_no proximo;
    if (lista == NULL)
        return NULL;
    else if (lista->v == v)
    {
        proximo = lista->prox;
        free(lista);
        return proximo;
    }
    else
    {
        lista->prox = remove_da_lista(lista->prox,
                                      v);
        return lista;
    }
}

void remove_aresta(p_grafo g, int u, int v)
{
    g->adjacencia[u] = remove_da_lista(g->adjacencia[u],
                                       v);
    g->adjacencia[v] = remove_da_lista(g->adjacencia[v],
                                       u);
}

void destroi_grafo(p_grafo g)
{
    int i;
    for (i = 0; i < g->n; i++)
        libera_lista(g->adjacencia[i]);
    free(g->adjacencia);
    free(g);
}

int tem_aresta(p_grafo g, int u, int v)
{
    p_no t;
    for (t = g->adjacencia[u]; t != NULL; t = t->prox)
        if (t->v == v)
            return 1;
    return 0;
}

void imprime_arestas(p_grafo g)
{
    for (int i = 0; i < g->n; i++)
    {
        printf("Vertice: %d\n", g->adjacencia[i]->v);
        libera_lista(g->adjacencia[i]);
    }
}