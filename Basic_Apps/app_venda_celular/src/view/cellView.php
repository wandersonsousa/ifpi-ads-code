<?php

class CellView
{
    public function listarCelulares($celulares)
    {
        $celularesTotal = count($celulares);
        print("Listando $celularesTotal celulares \n");
        foreach ($celulares as $celular) {
            print("Nome: {$celular['nome']} \n");
            print("Marca: {$celular['marca']} \n");
            print("Valor: {$celular['valor']} \n");
            print("------------------------------------ \n");
        }
    }

    public function listarCelular( $celular ){
        print("Nome: {$celular['nome']} \n");
        print("Marca: {$celular['marca']} \n");
        print("Valor: {$celular['valor']} \n");
        print("------------------------------------ \n");
    }

    public function listarBuscaResultado($celulares)
    {
        $celularesTotal = count($celulares);
        print("Listando $celularesTotal celulares \n");
        foreach ($celulares as $key => $celular) {
            print("Nome: {$celular['nome']} \n");
            print("Marca: {$celular['marca']} \n");
            print("Valor: {$celular['valor']} \n");
            print("ID: {$key} \n");
            print("------------------------------------ \n");
        }
    }

    public function entradaCelularSelecionado( $celularSelecionado ){
        echo "Celular Selecionado: {$celularSelecionado['nome']} \n";
        echo "Opções: \n";
        echo "1) Para Detalhes \n";
        echo "2) Para Remover \n";
        echo "3) Para Editar \n";
        echo "4) Para Duplicar \n";
    }

    public function entradaAtualizarCelular(){
        echo "Deixe o campo vazio e pressione <enter> para pular \n";

        $nome = strval(readline("nome: "));
        $marca = strval(readline("marca: "));
        $tela = strval(readline("tela: "));
        $valor = strval(readline("valor: "));
        $cam_frontal = strval(readline("Camera frontal(sim/nao): "));

        $celular = [];
        $celular['nome'] = $nome;
        $celular['marca'] = $marca;
        $celular['tela'] = $tela;
        $celular['valor'] = $valor;
        $celular['cam_frontal'] = $cam_frontal;

        return $celular;
        //return array_filter($celular, "strlen");
    }   

    public function entradaNovoCelular()
    {
        echo "Novo celular \n";

        $nome = strval(readline("nome: "));
        $marca = strval(readline("marca: "));
        $tela = strval(readline("tela: "));
        $valor = strval(readline("valor: "));
        $cam_frontal = strval(readline("Camera frontal(sim/nao): "));

        $celular = [];
        $celular['nome'] = $nome;
        $celular['marca'] = $marca;
        $celular['tela'] = $tela;
        $celular['valor'] = $valor;
        $celular['cam_frontal'] = $cam_frontal;

        return $celular;
    }

    public function geraMenu()
    {
        $menu = "***** App Jobs Cell *****\n";
        $menu .= "1 - Novo celular\n";
        $menu .= "2 - Listar celulares\n";
        $menu .= "3 - Buscar celular\n";
        $menu .= "4 - Salvar estado no banco\n";
        $menu .= "0 - sair\n";
        $menu .= "\nopcao >>> ";

        echo $menu;
    }
}
