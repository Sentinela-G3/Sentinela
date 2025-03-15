var database = require("../database/config")

function autenticar(email, senha) {
    console.log("ACESSEI O USUARIO MODEL \n \n\t\t >> Se aqui der erro de 'Error: connect ECONNREFUSED',\n \t\t >> verifique suas credenciais de acesso ao banco\n \t\t >> e se o servidor de seu BD está rodando corretamente. \n\n function autenticar(): ", email, senha)
    var instrucaoSql = `
        SELECT idUsuario, nome, email, fkCargo, idEmpresa, fkDono FROM usuario join usuarioEndereco on idUsuario = fkUsuario join endereco on idEndereco = fkEndereco join empresa on idEmpresa = fkEmpresa WHERE email = '${email}' AND senha = '${senha}' limit 1;
    `;
    console.log("Executando a instrução SQL: \n" + instrucaoSql);
    return database.executar(instrucaoSql);
}

function cadastrar(nome, email, cpf, contato, senha) {
    console.log("ACESSEI O USUARIO MODEL \n \n\t\t >> Se aqui der erro de 'Error: connect ECONNREFUSED',\n \t\t >> verifique suas credenciais de acesso ao banco\n \t\t >> e se o servidor de seu BD está rodando corretamente. \n\n function cadastrar():", nome, email, cpf, contato, senha);
    var instrucaoSql = `
        INSERT INTO usuario (nome, email, cpf, contato, senha, fkCargo) VALUES ('${nome}', '${email}', '${cpf}', '${contato}', '${senha}', 1);
    `;
    console.log("Executando a instrução SQL: \n" + instrucaoSql);

    return database.executar(instrucaoSql);
}

function obterFkEndereco(email){
    console.log("ACESSEI O USUARIO MODEL \n \n\t\t >> Se aqui der erro de 'Error: connect ECONNREFUSED',\n \t\t >> verifique suas credenciais de acesso ao banco\n \t\t >> e se o servidor de seu BD está rodando corretamente. \n\n function obterFkEndereco():", email);
    var instrucaoSql = `
    SELECT idEndereco, logradouro FROM endereco join usuarioEndereco on fkEndereco = idEndereco join usuario on fkUsuario = idUsuario where email = '${email}';
    `;
console.log("Executando a instrução SQL: \n" + instrucaoSql);
return database.executar(instrucaoSql);
}

function cadastrarUsuarioEndereco(fkUsuario, fkEndereco){
    console.log("ACESSEI O USUARIO MODEL \n \n\t\t >> Se aqui der erro de 'Error: connect ECONNREFUSED',\n \t\t >> verifique suas credenciais de acesso ao banco\n \t\t >> e se o servidor de seu BD está rodando corretamente. \n\n function obterFkEndereco():", fkEndereco, fkEndereco);
    var instrucaoSql = `
    INSERT INTO usuarioEndereco values (${fkUsuario}, ${fkEndereco}, 1);
    `;
console.log("Executando a instrução SQL: \n" + instrucaoSql);
return database.executar(instrucaoSql);
}

module.exports = {
    autenticar,
    cadastrar,
    obterFkEndereco,
    cadastrarUsuarioEndereco
};