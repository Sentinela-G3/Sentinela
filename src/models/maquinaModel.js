var database = require("../database/config");

function cadastrar(serial, setor, fkEndereco, fkModelo) {
  var instrucaoSql = `INSERT INTO maquina (serial, setor, fkEndereco, fkModelo, status) VALUES ('${serial}', '${setor}', '${fkEndereco}', '${fkModelo}', 'ativo');`;
  console.log("Executando a instrução SQL: \n" + instrucaoSql);
  return database.executar(instrucaoSql);
}

function obterFkModelo(fkEmpresa){
  var instrucaoSql = `SELECT idModelo, nomeModelo from modelo where fkEmpresa = ${fkEmpresa} and status = 'ativo';`;
  console.log("Executando a instrução SQL: \n" + instrucaoSql);
  return database.executar(instrucaoSql);
}

function obterMaquinas(fkEmpresa){
  var instrucaoSql = `SELECT maquina.* from maquina join modelo on fkModelo = idModelo join empresa on fkEmpresa = idEmpresa where fkEmpresa = ${fkEmpresa} and maquina.status = 'ativo';`;
  console.log("Executando a instrução SQL: \n" + instrucaoSql);
  return database.executar(instrucaoSql);
}

function excluir(idMaquina){
  var instrucaoSql = `UPDATE maquina set status = 'desativo' where idMaquina = ${idMaquina}`;
  console.log("Executando a instrução SQL: \n" + instrucaoSql);
  return database.executar(instrucaoSql);
}

function editar(setor, fkEndereco, idMaquina){
  var instrucaoSql = `UPDATE maquina set setor = '${setor}', fkEndereco = ${fkEndereco} where idMaquina = ${idMaquina}`;
  console.log("Executando a instrução SQL: \n" + instrucaoSql);
  return database.executar(instrucaoSql);
}

module.exports = 
{ cadastrar,
  obterFkModelo,
  obterMaquinas,
  excluir,
  editar
}
