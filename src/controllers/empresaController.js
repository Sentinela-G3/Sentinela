var empresaModel = require("../models/empresaModel");

function cadastrar(req, res) {
  var nome = req.body.nomeFantasiaServer;
  var cnpj = req.body.cnpjServer;
  var categoria = req.body.categoriaServer;

  empresaModel.cadastrar(nome, cnpj, categoria)
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

function cadastrarEndereco(req, res){
    var logradouro = req.body.logradouroServer;
    var cep = req.body.cepServer;
    var estado = req.body.estadoServer;
    var complemento = req.body.complementoServer;
    var fkEmpresa = req.body.fkEmpresaServer;

    empresaModel.cadastrarEndereco(logradouro, cep, estado, complemento, fkEmpresa)
    .then(
        function (resultado) {
            res.json(resultado);
        }
    ).catch(
        function (erro) {
            console.log(erro);
            console.log(
                "\nHouve um erro ao realizar o cadastro do endereço! Erro: ",
                erro.sqlMessage
            );
            res.status(500).json(erro.sqlMessage);
        }
    );    
}

function excluirEndereco(req, res){
    var idEndereco = req.body.enderecoServer;

    empresaModel.excluirEndereco(idEndereco)
    .then(
        function (resultado) {
            res.json(resultado);
        }
    ).catch(
        function (erro) {
            console.log(erro);
            console.log(
                "\nHouve um erro ao excluir o endereço! Erro: ",
                erro.sqlMessage
            );
            res.status(500).json(erro.sqlMessage);
        }
    ); 
}

module.exports = {
  cadastrar,
  cadastrarEndereco,
  excluirEndereco
};
