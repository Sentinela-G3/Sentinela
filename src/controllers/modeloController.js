var modeloModel = require("../models/modeloModel");

function cadastrar(req ,res){
    var nomeModelo = req.body.nomeServer;

    if (nomeModelo == undefined) {
        res.status(400).send("Seu nome do modelo está undefined!");
    }

     modeloModel.cadastrar(nomeModelo)
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