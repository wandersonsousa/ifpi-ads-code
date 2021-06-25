#include "graph.c"

int main(int argc, char const *argv[])
{
    p_grafo meuGrafo = criar_grafo(4);
    imprimi_arestas(le_grafo());
    return 0;
}