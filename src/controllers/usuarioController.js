const { json } = require("express");
var usuarioModel = require("../models/usuarioModel");

function autenticar(req, res) {
    var email = req.body.emailServer;
    var senha = req.body.senhaServer;

    if (email == undefined) {
        res.status(400).send("Seu email está undefined!");
    } else if (senha == undefined) {
        res.status(400).send("Sua senha está indefinida!");
    } else {

        usuarioModel.autenticar(email, senha)
            .then(
                function (resultadoAutenticar) {
                    console.log(`\nResultados encontrados: ${resultadoAutenticar.length}`);
                    console.log(`Resultados: ${JSON.stringify(resultadoAutenticar)}`);

                    if (resultadoAutenticar.length == 1) {
                        console.log(resultadoAutenticar);
                        res.json({
                            idEmpresa: resultadoAutenticar[0].idEmpresa,
                            email: resultadoAutenticar[0].email,
                            fkCargo: resultadoAutenticar[0].fkCargo,
                            nivelAcesso: resultadoAutenticar[0].nivelAcesso
                        })
                    } else if (resultadoAutenticar.length == 0) {
                        res.status(403).send("Email e/ou senha inválido(s)");
                    } else {
                        res.status(403).send("Mais de um usuário com o mesmo login e senha!");
                    }
                }
            ).catch(
                function (erro) {
                    console.log(erro);
                    console.log("\nHouve um erro ao realizar o login! Erro: ", erro.sqlMessage);
                    res.status(500).json(erro.sqlMessage);
                }
            );
    }

}

function cadastrar(req, res) {
    // Crie uma variável que vá recuperar os valores do arquivo cadastro.html
    var nome = req.body.nomeServer;
    var email = req.body.emailServer;
    var cpf = req.body.cpfServer;
    var contato = req.body.contatoServer;
    var cargo = req.body.cargoServer;
    var senha = req.body.senhaServer;

    // Faça as validações dos valores
    if (nome == undefined) {
        res.status(400).send("Seu nome está undefined!");
    } else if (email == undefined) {
        res.status(400).send("Seu email está undefined!");
    } else if (cpf == undefined) {
        res.status(400).send("Seu cpf está undefined!");
    } else if (contato == undefined) {
        res.status(400).send("Seu contato está undefined!");
    } else if (cargo == undefined) {
        res.status(400).send("Seu cargo está undefined!");
    } else if (senha == undefined) {
        res.status(400).send("Sua senha está undefined!");
    } else {

        // Passe os valores como parâmetro e vá para o arquivo usuarioModel.js
        usuarioModel.cadastrar(nome, email, cpf, contato, cargo, senha)
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
}

function obterFkEndereco(req, res){
    var email = req.body.emailServer;

    usuarioModel.obterFkEndereco(email)
    .then(
        function (resultado) {
            res.json(resultado);
        }
    ).catch(
        function (erro) {
            console.log(erro);
            console.log(
                "\nHouve um erro ao tentar obter os endereços! Erro: ",
                erro.sqlMessage
            );
            res.status(500).json(erro.sqlMessage);
        }
    );
}   

function cadastrarUsuarioEndereco(req, res){
    var fkUsuario = req.body.fkUsuarioServer;
    var fkEndereco = req.body.enderecoServer;

    usuarioModel.cadastrarUsuarioEndereco(fkUsuario, fkEndereco)
    .then(
        function (resultado) {
            res.json(resultado);
        }
    ).catch(
        function (erro) {
            console.log(erro);
            console.log(
                "\nHouve um erro ao tentar cadastrar o endereço do usuário! Erro: ",
                erro.sqlMessage
            );
            res.status(500).json(erro.sqlMessage);
        }
    );

}

function obterFkCargo(req, res){

    usuarioModel.obterFkCargo()
    .then(
        function (resultado) {
            res.json(resultado);
        }
    ).catch(
        function (erro) {
            console.log(erro);
            console.log(
                "\nHouve um erro ao tentar obter os cargos! Erro: ",
                erro.sqlMessage
            );
            res.status(500).json(erro.sqlMessage);
        }
    );
}

function obterIdFuncionario(req, res){
    var nivelAcesso = req.body.nivelAcessoServer;

    usuarioModel.obterIdFuncionario(nivelAcesso)
    .then(
        function (resultado) {
            res.json(resultado);
        }
    ).catch(
        function (erro) {
            console.log(erro);
            console.log(
                "\nHouve um erro ao tentar obter os funcionarios! Erro: ",
                erro.sqlMessage
            );
            res.status(500).json(erro.sqlMessage);
        }
    );
}

function editarFuncionario(req, res){
    var idUsuario = req.body.idUsuarioServer;
    var contato = req.body.contatoServer;
    var fkCargo = req.body.fkCargoServer;
    var fkEndereco = req.body.fkEnderecoServer;
    var fkEnderecoNovo = req.body.fkEnderecoNovoServer;
    
    usuarioModel.editarFuncionario(idUsuario, contato, fkCargo, fkEndereco, fkEnderecoNovo)
    .then(
        function (resultado) {
            res.json(resultado);
        }
    ).catch(
        function (erro) {
            console.log(erro);
            console.log(
                "\nHouve um erro ao tentar editar os funcionarios! Erro: ",
                erro.sqlMessage
            );
            res.status(500).json(erro.sqlMessage);
        }
    );    
}

function editarFuncionarioAdd(req, res){
    var idUsuario = req.body.idUsuarioServer;
    var fkEndereco = req.body.fkEnderecoServer;

    usuarioModel.editarFuncionarioAdd(idUsuario, fkEndereco)
    .then(
        function (resultado) {
            res.json(resultado);
        }
    ).catch(
        function (erro) {
            console.log(erro);
            console.log(
                "\nHouve um erro ao tentar editar os funcionarios! Erro: ",
                erro.sqlMessage
            );
            res.status(500).json(erro.sqlMessage);
        }
    );    
}

function editarFuncionarioDel(req, res){
    var idUsuario = req.body.idUsuarioServer;
    var fkEndereco = req.body.fkEnderecoServer;

    usuarioModel.editarFuncionarioDel(idUsuario, fkEndereco)
    .then(
        function (resultado) {
            res.json(resultado);
        }
    ).catch(
        function (erro) {
            console.log(erro);
            console.log(
                "\nHouve um erro ao tentar editar os funcionarios! Erro: ",
                erro.sqlMessage
            );
            res.status(500).json(erro.sqlMessage);
        }
    );    
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
}