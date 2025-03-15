var express = require("express");
var router = express.Router();

var maquinaController = require("../controllers/maquinaController");

router.post("/cadastrar", function (req, res) {
    maquinaController.cadastrar(req, res);
})

router.post("/obterFkModelo", function (req, res) {
    console.log("to na rota")
    maquinaController.obterFkModelo(req, res);
})


module.exports = router;