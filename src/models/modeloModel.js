var database = require("../database/config")

function cadastrar(modelo, idEmpresa){
     console.log("ACESSEI O USUARIO MODEL \n \n\t\t >> Se aqui der erro de 'Error: connect ECONNREFUSED',\n \t\t >> verifique suas credenciais de acesso ao banco\n \t\t >> e se o servidor de seu BD está rodando corretamente. \n\n function entrar(): ", modelo, idEmpresa)
        var instrucaoSql = `
           INSERT INTO modelo (nomeModelo, fkEmpresa, status) values ('${modelo}', ${idEmpresa}, 'ativo');
        `;
        console.log("Executando a instrução SQL: \n" + instrucaoSql);
        return database.executar(instrucaoSql);
}


module.exports = {
    cadastrar
};