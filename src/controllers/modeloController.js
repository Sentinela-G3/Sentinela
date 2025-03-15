var modeloModel = require("../models/modeloModel");

function cadastrar(req ,res){
    var nomeModelo = req.body.modeloServer;
    var idEmpresa = req.body.idEmpresaServer;

    if (nomeModelo == undefined) {
        res.status(400).send("Seu nome do modelo está undefined!");
    } else if (nomeModelo == undefined) {
        res.status(400).send("Seu idEmpresa está undefined!");
    }

     modeloModel.cadastrar(nomeModelo, idEmpresa)
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
    cadastrar
}