var maquinaModel = require("../models/maquinaModel");


function cadastrar(req, res) {
    var serial = req.body.serialServer;
    var setor = req.body.setorServer;
    var fkEndereco = req.body.fkEnderecoServer;
    var fkModelo = req.body.fkModeloServer;

        maquinaModel.cadastrar(serial, setor, fkEndereco, fkModelo)
            .then(
                function (resultado) {
                    res.json(resultado);
                }
            ).catch(
                function (erro) {
                    console.log(erro);
                    console.log(
                        "\nHouve um erro ao realizar o cadastro! Erro: ",
                        erro.sqlMessage
                    );
                    res.status(500).json(erro.sqlMessage);
                }
            );
}

function obterFkModelo(req, res){
    var fkEmpresa = req.body.fkEmpresaServer;

    maquinaModel.obterFkModelo(fkEmpresa)
            .then(
                function (resultado) {
                    res.json(resultado);
                }
            ).catch(
                function (erro) {
                    console.log(erro);
                    console.log(
                        "\nHouve um erro ao obter os modelos! Erro: ",
                        erro.sqlMessage
                    );
                    res.status(500).json(erro.sqlMessage);
                }
            );
}

function obterMaquinas(req, res){
    var fkEmpresa = req.body.fkEmpresaServer;

    maquinaModel.obterMaquinas(fkEmpresa)
    .then(
        function (resultado) {
            res.json(resultado);
        }
    ).catch(
        function (erro) {
            console.log(erro);
            console.log(
                "\nHouve um erro ao obter as maquinas! Erro: ",
                erro.sqlMessage
            );
            res.status(500).json(erro.sqlMessage);
        }
    );
}

function editarEndereco(req, res){
    var idMaquina = req.body.fkMaquinaServer;
    var idEndereco = req.body.enderecoServer;

    maquinaModel.editarEndereco(idMaquina, idEndereco)
    .then(
        function (resultado) {
            res.json(resultado);
        }
    ).catch(
        function (erro) {
            console.log(erro);
            console.log(
                "\nHouve um erro ao excluir a maquina! Erro: ",
                erro.sqlMessage
            );
            res.status(500).json(erro.sqlMessage);
        }
    );
}

function excluir(req, res){
    var idMaquina = req.body.idMaquinaServer;

    maquinaModel.excluir(idMaquina)
    .then(
        function (resultado) {
            res.json(resultado);
        }
    ).catch(
        function (erro) {
            console.log(erro);
            console.log(
                "\nHouve um erro ao obter os modelo! Erro: ",
                erro.sqlMessage
            );
            res.status(500).json(erro.sqlMessage);
        }
    );
}

module.exports = {
    cadastrar,
    obterFkModelo,
    obterMaquinas,
    editarEndereco,
    excluir
}