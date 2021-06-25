#include "graph.h"
#include <stdlib.h>
#include <stdio.h>

p_grafo criar_digrafo(int n)
{
    int i, j;
    p_grafo g = malloc(sizeof(Grafo));
    g->n = n;
    g->adjacencia = malloc(n * sizeof(int *));
    for (i = 0; i < n; i++)
        g->adjacencia[i] = malloc(n * sizeof(int *));

    for (i = 0; i < n; i++)
        for (j = 0; j < n; j++)
            g->adjacencia[i][j] = 0;

    return g;
}

p_grafo le_grafo()
{
    int n, m, i, u, v;
    p_grafo g;
    printf("n m\n");
    scanf("%d %d", &n, &m);
    g = criar_digrafo(n);
    printf("u v\n");
    for (i = 0; i < m; i++)
    {
        scanf("%d %d", &u, &v);
        insere_aresta(g, u, v);
    }
    return g;
}


void insere_aresta(p_grafo g, int u, int v)
{
    g->adjacencia[u][v] = 1;
}
void remove_aresta(p_grafo g, int u, int v)
{
    g->adjacencia[u][v] = 0;
}
void destroi_grafo(p_grafo g)
{
    int i;
    for (i = 0; i < g->n; i++)
        free(g->adjacencia[i]);
    free(g->adjacencia);
    free(g);
}

int tem_aresta(p_grafo g, int u, int v)
{
    return g->adjacencia[u][v];
}

int mais_popular(p_grafo g)
{
    int greater = 0, current_grau = grau(g, greater), max = current_grau;
    for (int u = 1; u < g->n; u++)
    {
        current_grau = grau(g, u);
        if (current_grau > max)
        {
            greater = u;
            max = current_grau;
        }
    }
    return greater;
}
int grau(p_grafo g, int u)
{
    int grau = 0;
    for (int v = 0; v < g->n; v++)
        if (g->adjacencia[u][v])
            grau++;
    return grau;
}

void imprime_arestas(p_grafo g)
{
    int u, v;
    for (u = 0; u < g->n; u++)
        for (v = 0; v < g->n; v++)
            if (g->adjacencia[u][v])
                printf("{%d, %d}\n", u, v);
}
void imprime_recomendacoes(p_grafo g, int u)
{
    for (int v = 0; v < g->n; v++)
    {
        if (tem_aresta(g, u, v)) // if is Ana friend
        {
            for (int vF = 0; vF < g->n; vF++)
            {
                if (tem_aresta(g, v, vF) && !tem_aresta(g, u, vF) && vF != u) // if is friend of Ana friend and Ana dont know him
                {
                    printf("Possível amigo de %d: %d\n", u, vF);
                }
            }
        }
    }
}