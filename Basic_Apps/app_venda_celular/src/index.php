<?php

require_once __DIR__ . "/model/cellModel.php";
require_once __DIR__ . "/view/cellView.php";

function main()
{
    $cellModel = new CellModel($databasePath = "database/db.json");
    $cellView = new CellView();

    while( true ) {
        $cellView->geraMenu();
        $opcao = intval(readline());

        if( $opcao === 0 ){
            $cellModel->salvarEstadoNoBD();
            return false;
        }

        controladorOpcoes( $opcao, $cellModel, $cellView );     

        readline("<enter> to continue... \n");
    }
}


function controladorOpcoes( &$opcao, &$cellModel, &$cellView ){

    switch ($opcao) {   
        case 1:
            $novoCelular = $cellView->entradaNovoCelular();
            $cellModel->adicionar($novoCelular);
            print("Celular cadastrado com sucesso! \n");
            break;
        case 2:
            $cellView->listarCelulares($cellModel->pegarCelulares());
            break;
        case 3:
            $search = readline("Search: ");
            $result = buscarCelulares($cellModel, $cellView,$search);
            if( empty($result) ){
                break;
            }

            $selecao = intval(readline("Selecione o celular com ID ou digite -1 para voltar: "));

            if($selecao === -1){
                break;
            }

            $celularSelecionado = $result[$selecao];

            $cellView->entradaCelularSelecionado( $celularSelecionado );
            $entrada = intval(readline("opcao >>> "));
            if($entrada === 1){
                $cellView->listarCelular( $celularSelecionado );
            }elseif( $entrada === 2 ){
                $cellModel->remover( $celularSelecionado['key'] );
            }elseif( $entrada === 3 ){
                $celularAtualizado = $cellView->entradaAtualizarCelular();
                
                $celularSelecionadoID =  $celularSelecionado['key'];
                unset($celularSelecionado['key']);

                foreach ($celularAtualizado as $keyAtualizado => $cellAtualizadoField) {
                    foreach( $celularSelecionado as  $keySelecionado => $cellSelecionadoField ){
                        if( $keyAtualizado === $keySelecionado && !$cellAtualizadoField ){
                                $celularAtualizado[$keyAtualizado] = $cellSelecionadoField;
                        }
                    }
                }

                $cellModel->atualizar( $celularSelecionadoID, $celularAtualizado );
            }elseif( $entrada === 4 ){
                $cellModel->adicionar($celularSelecionado);
            }
            break;
        case 4:
            $cellModel->salvarEstadoNoBD();
            break;
        default:
            print("Opção inválida \n");
            break;
    }

    return true;
}


function buscarCelulares(&$cellModel, &$cellView, $search ){
    $result = [];
    $celulares = $cellModel->pegarCelulares();
    foreach($celulares as $key => $cell){
        if( 
        stripos( $cell['nome'], $search) !== false ||
        stripos( $cell['marca'], $search) !== false   ){
            $cell['key'] = $key;
            array_push($result, $cell);
        }
    }

    $cellView->listarBuscaResultado( $result );
    return $result;
}


main();