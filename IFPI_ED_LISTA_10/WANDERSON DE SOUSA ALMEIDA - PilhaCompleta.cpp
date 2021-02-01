#include <stdio.h>
#include <iostream>
#include <stdlib.h>
#include <string.h>

using namespace std;

class No
{
public:
	char nome;
	int tipo;
	No *prox;
	No(char n)
	{
		nome = n;
		prox = NULL;
	}
};

class Pilha
{
public:
	No *topo;

	Pilha()
	{
		this->topo = NULL;
	}

	void push(char n, int t = 0)
	{
		No *novoNo = new (No)(n);
		novoNo->tipo = t;
		novoNo->prox = this->topo;
		this->topo = novoNo;
	}

	char pop()
	{
		char nodeName = this->topo->nome;
		No *prox = this->topo->prox;

		delete this->topo;

		this->topo = prox;
		return nodeName;
	}

	bool isEmpty()
	{
		return (this->topo == NULL);
	}
	void popAll()
	{
		while (!this->isEmpty())
		{
			this->pop();
		}
	}
};

void verificaPilhaEstoque(Pilha pilha)
{
	if (pilha.isEmpty())
	{
		cout << "A pilha está vazia" << endl;
	}
	else
	{
		cout << "A pilha não está vazia" << endl;
	}
}
void listaPilha(Pilha pilha)
{
	if (pilha.isEmpty())
	{
		cout << "\n Pilha Vazia !" << endl;
		return;
	}
	cout << "    Listagem da Pilha: " << endl;
	while (pilha.topo->prox != NULL)
	{
		cout << "Elemento: " << pilha.topo->nome << endl;
		pilha.topo = pilha.topo->prox;

		if (pilha.topo->prox == NULL)
		{
			cout << "Elemento: " << pilha.topo->nome << endl;
		}
	}
}

bool eh_del_abertura(char del)
{
	string delimitadores = "{(";
	for (size_t j = 0; j < delimitadores.size(); j++)
	{
		char delimitador = delimitadores[j];
		if (delimitador == del)
		{
			return true;
		}
	}
	return false;
}


bool algoritmo_de_casamento(string texto)
{
	//QUESTAO 09
	Pilha algoritmo_pilha = Pilha();

	for (size_t i = 0; i < texto.size(); i++)
	{
		string delimitadores = "{()}";
		char letra = texto[i];

		for (size_t j = 0; j < delimitadores.size(); j++)
		{
			char delimitador = delimitadores[j];

			if (letra == delimitador)
			{
				if (algoritmo_pilha.isEmpty())
				{
					if (eh_del_abertura(delimitador))
					{
						//is first element
						if (delimitador == '{')
						{
							algoritmo_pilha.push(delimitador, 0);
						}
						else
						{
							algoritmo_pilha.push(delimitador, 1);
						}
					}
					else
					{
						return false;
					}
				}
				else
				{
					if ( eh_del_abertura(delimitador) )
					{
						if (delimitador == '{')
						{
							algoritmo_pilha.push(delimitador, 0);
						}
						else
						{
							algoritmo_pilha.push(delimitador, 1);
						}
					}else {
						if( delimitador == '}' && algoritmo_pilha.topo->tipo == 0 ){
							algoritmo_pilha.pop();
						}else if( delimitador == ')' && algoritmo_pilha.topo->tipo == 1 ){
							algoritmo_pilha.pop();
						}else{
							return false;
						}
					}
				}
			}
		}
	}
	return true;
}

bool algoritmo_de_reverso( string texto ){
	//QUESTAO 10
	Pilha pilha_direita = Pilha();
	string parte_esquerda = texto.substr( 0, texto.find("C") );
	string parte_direita = texto.substr( texto.find("C") + 1 ); 

	if( !(parte_direita.size() == parte_esquerda.size()) ){
		return false;
	}
	
	for (size_t i = 0; i < parte_direita.size(); i++)
	{
		pilha_direita.push( (char)parte_direita[i] );
	}
	for (size_t i = 0; i < parte_esquerda.size(); i++)
	{
		cout << "Texto: " << parte_esquerda[i] << " Pilha: " << pilha_direita.topo->nome << endl;
		if( parte_esquerda[i] != pilha_direita.topo->nome ){
			return false;
		}
		pilha_direita.pop();
	}
	
	return true;
}



int main()
{
	// string nome = "{Wan(d())erso{(n){}{}}}";
	// bool result = algoritmo_de_casamento(nome);
	// if(result){
	// 	cout << "Passou no algoritmo" << endl;
	// }else{
	// 	cout << "Não passou no algoritmo" << endl;
	// }

	string texto = "ABABBACABBABA";
	bool result = algoritmo_de_reverso( texto );
	if(result){
		cout << "Passou no algoritmo" << endl;
	}else{
		cout << "Não passou no algoritmo" << endl;
	}
}
