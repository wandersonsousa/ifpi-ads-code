<?php

class CellModel
{
    private $celulares;
    private $databasePath;

    function __construct(string $databasePath)
    {
        $this->databasePath = $databasePath;
        $this->atualizarStatusNoBD();
    }

    public function atualizarStatusNoBD(){
        $this->celulares = json_decode( file_get_contents($this->databasePath), true );
    }
    public function salvarEstadoNoBD(){
        file_put_contents( $this->databasePath, json_encode( $this->celulares ));
    }

    public function pegarCelulares()
    {
        return $this->celulares;
    }

    public function adicionar( $celularNovo )
    {
        array_push( $this->celulares, $celularNovo);
    }
    public function remover( $id ){
        unset( $this->celulares[$id] );
    }
    public function atualizar( $id, $celularAtualizado ){
        $this->celulares[$id] = $celularAtualizado;
    }
   
}
