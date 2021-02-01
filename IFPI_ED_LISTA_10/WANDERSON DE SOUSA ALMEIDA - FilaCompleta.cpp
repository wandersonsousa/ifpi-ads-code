#include <stdio.h>
#include <iostream>
#include <stdlib.h>
#include <string.h>

using namespace std;

class No{
	public:
		char nome;
		No *prox;
		No(char n){
			this->nome = n;
			this->prox = NULL;
		}
};

class Fila{
	public:
		No *inicio;
		No *fim;
		
		Fila(){
			this->inicio = NULL;
			this->fim = NULL;
		}
		
		void inserir(char n){
			No *novo = new No(n);
			if(this->inicio == NULL){
				this->inicio = novo;
				this->fim = novo;
			}else{
				this->fim->prox = novo;
				this->fim = novo;
			}
		}
		
		char apagar(){
			No *temp;
			char nome;
			if(this->inicio != NULL){
				temp = this->inicio;
				nome = this->inicio->nome;
				this->inicio = this->inicio->prox;
				free(temp);
			}
			return nome;
		}
		
		bool isEmpty(){
			return (inicio == NULL);
		}
	
	    public:
			void apagaTodos(){
	    		while (!isEmpty())
	    	    	apagar();
	    	
			}
};

int main(){
    Fila *f1=new Fila();

    f1->inserir('A');
	f1->inserir('B');
	f1->inserir('C');
    
	

	
}
