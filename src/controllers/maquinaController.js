var maquinaModel = require("../models/usuarioModel");


function cadastrar(req, res) {
    

        maquinaModel.cadastrar(nome, email, cpf, contato, senha)
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
                        "\nHouve um erro ao realizar o cadastro! Erro: ",
                        erro.sqlMessage
                    );
                    res.status(500).json(erro.sqlMessage);
                }
            );
}

module.exports = {
    cadastrar,
    obterFkModelo
}