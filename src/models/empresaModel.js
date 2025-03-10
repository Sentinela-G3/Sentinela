var database = require("../database/config");

function cadastrar(nome, cnpj, categoria) {
  var instrucaoSql = `INSERT INTO empresa (nomeFantasia, cnpj, categoria, dataInicio) VALUES ('${nome}', '${cnpj}', ${categoria}, now())`;

  return database.executar(instrucaoSql);
}

module.exports = { cadastrar };
