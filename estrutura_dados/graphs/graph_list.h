#ifndef GRAPH_LIST
#define GRAPH_LIST

typedef struct no No;
typedef struct grafo Grafo;

struct no
{
    int v;
    No *prox;
};
typedef No *p_no;

struct grafo
{
    int n;
    p_no *adjacencia;
};
typedef Grafo *p_grafo;

p_grafo criar_grafo(int n);

void destroi_grafo(p_grafo g);
void insere_aresta(p_grafo g, int u, int v);
p_no insere_na_lista(p_no lista, int v);
void remove_aresta(p_grafo g, int u, int v);
int tem_aresta(p_grafo g, int u, int v);
int grau(p_grafo g, int u);
void imprime_arestas(p_grafo g);

#endif
