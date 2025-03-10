var express = require("express");
var router = express.Router();

var modeloController = require("../controllers/modeloController");

router.post("/cadastrar", function (req, res) {
    modeloController.cadastrar(req, res);
})

module.exports = router;