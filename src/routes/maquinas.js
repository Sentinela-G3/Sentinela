var express = require("express");
var router = express.Router();

var maquinaController = require("../controllers/maquinaController");

router.post("/cadastrar", function (req, res) {
    maquinaController.cadastrar(req, res);
})

router.post("/obterFkModelo", function (req, res) {
    maquinaController.obterFkModelo(req, res);
})

router.post("/obterMaquinas", function (req, res){
    maquinaController.obterMaquinas(req, res)
})

router.post("/editar", function(req, res){
    maquinaController.editar(req, res)
})

router.post("/excluir", function(req, res){
    maquinaController.excluir(req, res)
})

module.exports = router;