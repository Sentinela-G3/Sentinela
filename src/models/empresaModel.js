var database = require("../database/config");

function cadastrar(nome, cnpj, categoria) {
  var instrucaoSql = `INSERT INTO empresa (nomeFantasia, cnpj, categoria, dataInicio) VALUES ('${nome}', '${cnpj}', ${categoria}, now());`;

  return database.executar(instrucaoSql);
}

function cadastrarEndereco(logradouro, cep, estado, complemento){
  var instrucaoSql = `INSERT INTO endereco (logradouro, cep, estado, complemento) VALUES ('${logradouro}', '${cep}', '${estado}', '${complemento}');`;

  return database.executar(instrucaoSql);
}

module.exports = { cadastrar, cadastrarEndereco };
