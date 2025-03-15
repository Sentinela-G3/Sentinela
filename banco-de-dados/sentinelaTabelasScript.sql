create database sentinela;
use sentinela;

CREATE TABLE cargo (
	idCargo INT PRIMARY KEY AUTO_INCREMENT,
    nomeCargo VARCHAR(45),
    nivelAcesso INT
);

CREATE TABLE empresa (
    idEmpresa INT AUTO_INCREMENT PRIMARY KEY,
    nomeFantasia VARCHAR(45),
    cnpj CHAR(14),
    categoria VARCHAR(45),
    dataInicio DATE,
    status VARCHAR(13)
);

CREATE TABLE usuario (
    idUsuario INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(45),
    email VARCHAR(45),
    cpf CHAR(11),
    contato CHAR(11),
    senha CHAR(64),
    fkCargo INT,
    fkDono INT,
    constraint fkUsuarioCargo foreign key (fkCargo) references cargo (idCargo),
    constraint fkUsuarioDono foreign key (fkDono) references empresa (idEmpresa)
);

CREATE TABLE endereco (
    idEndereco INT AUTO_INCREMENT PRIMARY KEY,
    logradouro VARCHAR(45),
    cep CHAR(8),
    estado CHAR(2),
    complemento VARCHAR(45),
    fkEmpresa INT,
    status VARCHAR(13),
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

CREATE TABLE modelo (
    idModelo INT AUTO_INCREMENT PRIMARY KEY,
    nomeModelo VARCHAR(45),
    fkEmpresa INT,
    status VARCHAR(13),
    constraint fkModeloEmpresa foreign key (fkEmpresa) references empresa (idEmpresa)
);

CREATE TABLE maquina (
    idMaquina INT AUTO_INCREMENT PRIMARY KEY,
    status VARCHAR(13),
    setor VARCHAR(45),
    serial VARCHAR(45),
    fkEndereco INT,
    fkModelo INT,
    FOREIGN KEY (fkEndereco) REFERENCES endereco(idEndereco),
    FOREIGN KEY (fkModelo) REFERENCES modelo(idModelo)
);

CREATE TABLE componente (
    idComponente INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(45),
    modelo VARCHAR(45),
    fkMaquina INT,
    FOREIGN KEY (fkMaquina) REFERENCES maquina(idMaquina),
    status VARCHAR(13)
);

CREATE TABLE tipo (
    idTipo INT AUTO_INCREMENT PRIMARY KEY,
    tipoDado VARCHAR(45),
    fkComponente INT,
    constraint fkTipoComponente foreign key (fkComponente) references componente (idComponente)
);

CREATE TABLE dados (
	idDados INT AUTO_INCREMENT PRIMARY KEY,
    valor FLOAT,
    tempoColeta DATETIME,
    alerta TINYINT,
    fkTipo INT,
    constraint fkDadosTipo foreign key (fkTipo) references tipo (idTipo)
);

insert into empresa values
(2, 'Quicktron', '11111111111111', 'fabricante', '2025-02-25', 'ativo');

insert into cargo values
(1, 'Gerente', 1),
(2, 'Analista', 3);

insert into usuario values
(1, 'Ronaldo Alves', 'ronaldoalves@quicktron.com', 12345678901, 12345678901, 'Quicktron#123', 2, null);

insert into endereco values
(1, 'Rua João Silva', '04911111', 'sp', '', 2, 'ativo');

insert into usuarioEndereco  values
(1, 1, 2);

        SELECT idUsuario, nome, email, fkCargo, idEmpresa FROM usuario join usuarioEndereco on idUsuario = fkUsuario join endereco on 
idEndereco = fkEndereco join empresa on idEmpresa = fkEmpresa WHERE email = 'ronaldoalves@quicktron.com' AND senha = 'Quicktron#123'; 
insert into modelo values
(default, 'M60', 2, 'ativo');

insert into maquina values
(default, "ativo", 'Setor 1', "EG209", 1, 1);

insert into componente values
(1, 'Processador', 'Ryzen 3', 1, 'ativo'),
(2, 'Memoria', 'XPG Gammix D35', 1, 'ativo'),
(3, 'Bateria', 'Cr2032', 1, 'ativo'),
(4, 'redeChip', 'PCI-EXPRESS', 1, 'ativo'),
(5, 'Armazenamento', 'Kingston A400', 1, 'ativo');

insert into tipo values
(1, "Tempo da CPU ativa em porcentagem", 1),
(2, "Tempo inativo da CPU em porcentagem", 1),
(3, "Porcentagem atual de uso da CPU", 1),
(4, "Frequência da CPU", 1),
(5, "Memória disponivel", 2),
(6, "Memória utilizada em porcentagem", 2),
(7, "Memória não utilizada", 2),
(8, "Memória total", 2),
(9, "Bateria atual em porcentagem", 3),
(10, "Quantidade de bytes enviado", 4),
(11, "Armazenamento disponivel em bytes", 5),
(12, "Armazenamento total em bytes", 5);

select * from usuario;

select * from empresa;

select * from endereco;

select * from modelo;

select * from usuarioEndereco;

SELECT idModelo, nomeModelo from modelo where fkEmpresa = 2;

INSERT INTO maquina (serial, fkEndereco, fkModelo, status) VALUES ('ababa', '1', '1', 'ativo');