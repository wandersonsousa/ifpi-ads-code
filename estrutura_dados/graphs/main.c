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
int tem_aresta(p_grafo g, int u, int v);
void imprimi_arestas(p_grafo g);
int grau(p_grafo g, int u);

p_grafo le_grafo();

int main(int argc, char const *argv[])
{
    p_grafo meuGrafo = criar_grafo(4);
    le_grafo();
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
            g->adjacencia[i][j] = 0;

    return g;
}

void destroi_grafo(p_grafo g)
{
    int i;
    for (i = 0; i < g->n; i++)
        free(g->adjacencia[i]);
    free(g->adjacencia);
    free(g);
}

void insere_aresta(p_grafo g, int u, int v)
{
    g->adjacencia[u][v] = 1;
    g->adjacencia[v][u] = 1;
}

void remove_aresta(p_grafo g, int u, int v)
{
    g->adjacencia[u][v] = 0;
    g->adjacencia[v][u] = 0;
}

int tem_aresta(p_grafo g, int u, int v)
{
    return g->adjacencia[u][v];
}

void imprimi_arestas(p_grafo g)
{
    int u, v;
    for (u = 0; u < g->n; u++)
        for (v = 0; v < g->n; v++)
            if (g->adjacencia[u][v])
                printf("{%d, %d}\n", u, v);
}

p_grafo le_grafo()
{
    int n, m, i, u, v;
    p_grafo g;
    printf("n m\n");
    scanf("%d %d", &n, &m);
    g = criar_grafo(n);
    printf("u v\n");
    for (i = 0; i < m; i++)
    {
        scanf("%d %d", &u, &v);
        insere_aresta(g, u, v);
    }
    return g;
}

int grau(p_grafo g, int u)
{
    int v, grau = 0;
    for (v = 0; v < g->n; v++)
        if (g->adjacencia[u][v])
            grau++;
    return grau;
}

int mais_popular(p_grafo g)
{
    int u, max, grau_max, grau_atual;
    max = 0;
    grau_max = grau(g, 0);
    for (u = 1; u < g->n; u++)
    {
        grau_atual = grau(g, u);
        if (grau_atual > grau_max)
        {
            grau_max = grau_atual;
            max = u;
        }
        return max;
    }
}