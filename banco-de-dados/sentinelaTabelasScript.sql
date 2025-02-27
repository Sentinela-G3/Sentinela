create database sentinela;
use sentinela;

CREATE TABLE usuario (
    idUsuario INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(45),
    sobrenome VARCHAR(45),
    email VARCHAR(45),
    cpf CHAR(11),
    contato CHAR(11),
    cargo VARCHAR(45),
    senha CHAR(64)
);

CREATE TABLE empresa (
    idEmpresa INT AUTO_INCREMENT PRIMARY KEY,
    nomeFantasia VARCHAR(45),
    cnpj CHAR(14),
    categoria VARCHAR(45),
    dataInicio DATE
);

CREATE TABLE endereco (
    idEndereco INT AUTO_INCREMENT PRIMARY KEY,
    logradouro VARCHAR(45),
    cep CHAR(8),
    estado CHAR(2),
    complemento VARCHAR(45),
    fkEmpresa INT,
    FOREIGN KEY (fkEmpresa) REFERENCES empresa(idEmpresa)
);

CREATE TABLE usuarioEndereco (
    fkUsuario INT,
    fkEndereco INT,
    acesso INT,
    PRIMARY KEY (fkUsuario, fkEndereco),
    FOREIGN KEY (fkUsuario) REFERENCES usuario(idUsuario),
    FOREIGN KEY (fkEndereco) REFERENCES endereco(idEndereco)
);

CREATE TABLE maquina (
    idMaquina INT AUTO_INCREMENT PRIMARY KEY,
    status VARCHAR(13),
    nomeModelo VARCHAR(45),
    fabricanteModelo VARCHAR(45),
    fkEndereco INT,
    fkEmpresa INT,
    FOREIGN KEY (fkEndereco) REFERENCES endereco(idEndereco),
    FOREIGN KEY (fkEmpresa) REFERENCES empresa(idEmpresa)
);

CREATE TABLE componente (
    idComponente INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(45),
    modelo VARCHAR(45),
    fkMaquina INT,
    FOREIGN KEY (fkMaquina) REFERENCES maquina(idMaquina)
);

CREATE TABLE processador (
    idProcessador INT AUTO_INCREMENT PRIMARY KEY,
    porcentagemUso DECIMAL(4,1),
    tempoAtivoPorcentagem DECIMAL(4,1),
    tempoInativoPorcentagem DECIMAL(4,1),
    frequencia float,
    tempoColeta DATETIME,
    alerta TINYINT,
    fkComponente INT,
    FOREIGN KEY (fkComponente) REFERENCES componente(idComponente)
);

CREATE TABLE memoria (
    idMemoria INT AUTO_INCREMENT PRIMARY KEY,
    memoriaInutilizada FLOAT,
    capacidadeDisp FLOAT,
    capacidadeTotal FLOAT,
    porcentagemUso DECIMAL(4,1),
    tempoColeta DATETIME,
    alerta TINYINT,
    fkComponente INT,
    FOREIGN KEY (fkComponente) REFERENCES componente(idComponente)
);

CREATE TABLE bateria (
    idBateria INT AUTO_INCREMENT PRIMARY KEY,
    porcentagemAtual INT,
    tempoRestante INT,
	tempoColeta DATETIME,
    alerta TINYINT,
    fkComponente INT,
    FOREIGN KEY (fkComponente) REFERENCES componente(idComponente)
);

CREATE TABLE armazenamento (
    idArmazenamento INT AUTO_INCREMENT PRIMARY KEY,
    capacidadeTotal FLOAT,
    capacidadeDisp FLOAT,
    tempoColeta DATETIME,
    alerta TINYINT,
    fkComponente INT,
    FOREIGN KEY (fkComponente) REFERENCES componente(idComponente)
);

CREATE TABLE redeChip (
    idRedeChip INT AUTO_INCREMENT PRIMARY KEY,
    byteEnviado INT,
    tempoColeta DATETIME,
    alerta TINYINT,
    fkComponente INT,
    FOREIGN KEY (fkComponente) REFERENCES componente(idComponente)
);

insert into empresa values
(default, 'Quicktron', '11111111111111', 'fabricante', '2025-02-25');

insert into endereco values
(default, 'Rua João Silva', '04911111', 'sp', '', 1);

insert into maquina values
(default, 'ativo', 'M60', 'Quicktron', 1, 1);

insert into componente values
(default, 'Processador', 'Ryzen 3', 1),
(default, 'Memoria', 'XPG Gammix D35', 1),
(default, 'Bateria', 'Cr2032', 1),
(default, 'redeChip', 'PCI-EXPRESS', 1),
(default, 'Armazenamento', 'Kingston A400', 1);
