CREATE DATABASE sentinela;
USE sentinela;

CREATE TABLE enderecoEmpresa (
    idenderecoEmpresa INT PRIMARY KEY AUTO_INCREMENT,
    fkEmpresa INT NOT NULL,
    cep INT NOT NULL,
    numero INT NOT NULL,
    logradouro VARCHAR(50) NOT NULL,
    estado VARCHAR(50) NOT NULL,
    cidade VARCHAR(45) NOT NULL,
    complemento VARCHAR(45),
    FOREIGN KEY (fkEmpresa) REFERENCES empresa(idEmpresa)
);

CREATE TABLE empresa (
    idEmpresa INT PRIMARY KEY AUTO_INCREMENT,
    razaoSocial VARCHAR(45) NOT NULL,
    cnpj CHAR(14) NOT NULL UNIQUE,
    categoria VARCHAR(20) NOT NULL,
    dataInicio DATETIME NOT NULL
);

CREATE TABLE maquina (
    idmaquina INT PRIMARY KEY AUTO_INCREMENT,
    fkEmpresa INT NOT NULL,
    modelo VARCHAR(45) NOT NULL,
    SO VARCHAR(45) NOT NULL,
    serialNumber VARCHAR(45) NOT NULL UNIQUE,
    status TINYINT NOT NULL,
    setor VARCHAR(15),
    FOREIGN KEY (fkEmpresa) REFERENCES empresa(idEmpresa)
);

CREATE TABLE colaborador (
    idUsuario INT PRIMARY KEY AUTO_INCREMENT,
    fkEmpresa INT NOT NULL,
    nome VARCHAR(45) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    telefone CHAR(11) NOT NULL,
    senha CHAR(64) NOT NULL,
    tipoUsuario INT NOT NULL,
    dataCriacao DATETIME NOT NULL,
    FOREIGN KEY (fkEmpresa) REFERENCES empresa(idEmpresa)
);

CREATE TABLE componente (
    idcomponente INT PRIMARY KEY AUTO_INCREMENT,
    fkMaquina INT NOT NULL,
    tipo VARCHAR(7) NOT NULL,
    modeloComponente VARCHAR(45),
    valor FLOAT NOT NULL,
    minimo FLOAT NOT NULL,
    maximo FLOAT NOT NULL,
    FOREIGN KEY (fkMaquina) REFERENCES maquina(idmaquina)
);

CREATE TABLE historico (
    idhistorico INT PRIMARY KEY AUTO_INCREMENT,
    fkComponente INT NOT NULL,
    dataCaptura DATETIME NOT NULL,
    valor FLOAT NOT NULL,
    FOREIGN KEY (fkComponente) REFERENCES componente(idcomponente)
);

CREATE TABLE alerta (
    idalerta INT PRIMARY KEY AUTO_INCREMENT,
    fkComponente INT NOT NULL,
    dataCaptura DATETIME NOT NULL,
    valor FLOAT NOT NULL,
    FOREIGN KEY (fkComponente) REFERENCES componente(idcomponente)
);
