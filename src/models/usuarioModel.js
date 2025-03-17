var database = require("../database/config")

function autenticar(email, senha) {
    console.log("ACESSEI O USUARIO MODEL \n \n\t\t >> Se aqui der erro de 'Error: connect ECONNREFUSED',\n \t\t >> verifique suas credenciais de acesso ao banco\n \t\t >> e se o servidor de seu BD está rodando corretamente. \n\n function autenticar(): ", email, senha)
    var instrucaoSql = `
        SELECT idUsuario, nome, email, fkCargo, idEmpresa, fkDono, nivelAcesso FROM usuario join usuarioEndereco on idUsuario = fkUsuario join endereco on idEndereco = fkEndereco join empresa on idEmpresa = fkEmpresa join cargo on fkCargo = idCargo WHERE email = '${email}' AND senha = SHA2('${senha}', 256) AND usuario.status = 'ativo' group by idUsuario, idEmpresa;
    `;
    console.log("Executando a instrução SQL: \n" + instrucaoSql);
    return database.executar(instrucaoSql);
}

function cadastrar(nome, email, cpf, contato, cargo, senha) {
    console.log("ACESSEI O USUARIO MODEL \n \n\t\t >> Se aqui der erro de 'Error: connect ECONNREFUSED',\n \t\t >> verifique suas credenciais de acesso ao banco\n \t\t >> e se o servidor de seu BD está rodando corretamente. \n\n function cadastrar():", nome, email, cpf, contato, cargo, senha);
    var instrucaoSql = `
        INSERT INTO usuario (nome, email, cpf, contato, fkCargo, senha) VALUES ('${nome}', '${email}', '${cpf}', '${contato}', ${cargo}, SHA2('${senha}', 256));
    `;
    console.log("Executando a instrução SQL: \n" + instrucaoSql);

    return database.executar(instrucaoSql);
}

function obterFkEndereco(email){
    console.log("ACESSEI O USUARIO MODEL \n \n\t\t >> Se aqui der erro de 'Error: connect ECONNREFUSED',\n \t\t >> verifique suas credenciais de acesso ao banco\n \t\t >> e se o servidor de seu BD está rodando corretamente. \n\n function obterFkEndereco():", email);
    var instrucaoSql = `
    SELECT idEndereco, logradouro FROM endereco join usuarioEndereco on fkEndereco = idEndereco join usuario on fkUsuario = idUsuario where email = '${email}' and endereco.status = 'ativo';
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

function obterFkCargo(){
    var instrucaoSql = `
    SELECT * FROM cargo where idCargo != 1; 
     `;
 console.log("Executando a instrução SQL: \n" + instrucaoSql);
 return database.executar(instrucaoSql);
}

function obterIdFuncionario(nivelAcesso){
    var instrucaoSql = `
    select usuario.*, fkEndereco from usuario join cargo on fkCargo = idCargo left join usuarioEndereco on fkUsuario = idUsuario where cargo.nivelAcesso > ${nivelAcesso} group by idUsuario, fkEndereco;
     `;
 console.log("Executando a instrução SQL: \n" + instrucaoSql);
 return database.executar(instrucaoSql);
}

function editarFuncionario(idUsuario, contato, fkCargo, fkEndereco, fkEnderecoNovo){
    var instrucaoSql = `
    UPDATE usuario join usuarioEndereco on fkUsuario = idUsuario set usuario.contato = '${contato}', usuario.fkCargo = ${fkCargo}, usuarioEndereco.fkEndereco = ${fkEnderecoNovo} where idUsuario = ${idUsuario} and usuarioEndereco.fkEndereco = ${fkEndereco};
     `;
 console.log("Executando a instrução SQL: \n" + instrucaoSql);
 return database.executar(instrucaoSql);
}

function editarFuncionarioAdd(idUsuario, fkEndereco){
    var instrucaoSql = `
    INSERT INTO usuarioEndereco (fkEndereco, fkUsuario) values (${fkEndereco}, ${idUsuario});
     `;
 console.log("Executando a instrução SQL: \n" + instrucaoSql);
 return database.executar(instrucaoSql);
}

function editarFuncionarioDel(idUsuario, fkEndereco){
    var instrucaoSql = `
    DELETE FROM usuarioEndereco where fkEndereco = ${fkEndereco} and fkUsuario =  ${idUsuario};
     `;
 console.log("Executando a instrução SQL: \n" + instrucaoSql);
 return database.executar(instrucaoSql);
}

module.exports = {
    autenticar,
    cadastrar,
    obterFkEndereco,
    cadastrarUsuarioEndereco,
    obterFkCargo,
    obterIdFuncionario,
    editarFuncionario,
    editarFuncionarioAdd,
    editarFuncionarioDel
};