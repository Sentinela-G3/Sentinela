var express = require("express");
var router = express.Router();

var usuarioController = require("../controllers/usuarioController");

router.post("/cadastrar", function (req, res) {
    usuarioController.cadastrar(req, res);
})

router.post("/autenticar", function (req, res) {
    usuarioController.autenticar(req, res);
});

router.post("/obterFkEndereco", function (req, res){
    usuarioController.obterFkEndereco(req, res);
});

router.get("/obterFkCargo", function (req, res){
    usuarioController.obterFkCargo(req, res);
});

router.post("/cadastrarUsuarioEndereco", function (req, res){
    usuarioController.cadastrarUsuarioEndereco(req, res);
})

router.post("/obterIdFuncionario", function(req, res){
    usuarioController.obterIdFuncionario(req, res);
})

router.post("/editarFuncionario", function(req, res){
    usuarioController.editarFuncionario(req, res);
})

router.post("/editarFuncionarioAdd", function(req, res){
    usuarioController.editarFuncionarioAdd(req, res);
})

router.post("/editarFuncionarioDel", function(req, res){
    usuarioController.editarFuncionarioDel(req, res)
})

module.exports = router;