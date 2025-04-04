CREATE DATABASE sentinela;
USE sentinela;

# SISTEMA APP WEB
CREATE TABLE empresa (
	id_empresa INT PRIMARY KEY AUTO_INCREMENT,
    razao_social VARCHAR(100) NOT NULL,
    cnpj CHAR(14) NOT NULL,
    categoria VARCHAR(50) NOT NULL,
    data_inicio DATE NOT NULL,
    status TINYINT NOT NULL
);

CREATE TABLE endereco_empresa (
	id_endereco INT PRIMARY KEY AUTO_INCREMENT,
    cep CHAR(9) NOT NULL,
    numero INT NOT NULL,
    logradouro VARCHAR(250) NOT NULL,
    estado VARCHAR(100) NOT NULL,
    cidade VARCHAR(100) NOT NULL,
    complemento VARCHAR(100) NOT NULL,
    fk_endereco_empresa INT UNIQUE NOT NULL,
    FOREIGN KEY (fk_endereco_empresa)
		REFERENCES empresa(id_empresa)
);

CREATE TABLE colaborador (
	id_usuario INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(250) NOT NULL,
    email VARCHAR(250) NOT NULL,
    telefone CHAR(11) NOT NULL,
    senha CHAR(64) NOT NULL,
    tipo INT NOT NULL,
    data_criacao DATE,
    fk_colaborador_empresa INT NOT NULL,
    FOREIGN KEY (fk_colaborador_empresa)
		REFERENCES empresa(id_empresa)
);

CREATE TABLE maquina (
	id_maquina INT PRIMARY KEY AUTO_INCREMENT,
    modelo VARCHAR(100) NOT NULL,
    so VARCHAR(100) NOT NULL,
    serial_number VARCHAR(100) NOT NULL,
    status TINYINT NOT NULL,
    setor VARCHAR(50) NOT NULL,
    fk_maquina_empresa INT NOT NULL,
    FOREIGN KEY (fk_maquina_empresa)
		REFERENCES empresa(id_empresa)
);

CREATE TABLE componente (
	id_componente INT PRIMARY KEY AUTO_INCREMENT,
    tipo VARCHAR(50) NOT NULL,
    modelo VARCHAR(100) NOT NULL,
    valor FLOAT NOT NULL,
    minimo FLOAT NOT NULL,
    maximo FLOAT NOT NULL,
    fk_componente_maquina INT NOT NULL,
    FOREIGN KEY (fk_componente_maquina)
		REFERENCES maquina(id_maquina)
);

# CAPTURA
CREATE TABLE historico (
	id_historico INT PRIMARY KEY AUTO_INCREMENT,
    data_captura DATETIME NOT NULL,
    valor FLOAT,
    fk_historico_componente INT NOT NULL,
    FOREIGN KEY (fk_historico_componente)
		REFERENCES componente(id_componente)
);

CREATE TABLE alerta (
	id_alerta INT PRIMARY KEY AUTO_INCREMENT,
    data_captura DATETIME NOT NULL,
    valor FLOAT,
    fk_alerta_componente INT NOT NULL,
    FOREIGN KEY (fk_alerta_componente)
		REFERENCES componente(id_componente)
);

INSERT INTO empresa (razao_social, cnpj, categoria, data_inicio, status)
VALUES ('TechGuard LTDA', '12345678000199', 'Segurança Digital', '2023-01-15', 1);

INSERT INTO endereco_empresa (cep, numero, logradouro, estado, cidade, complemento, fk_endereco_empresa)
VALUES (12345678, 100, 'Rua das Inovações', 'São Paulo', 'São Paulo', 'Próximo ao metrô', 1);

INSERT INTO colaborador (nome, email, telefone, senha, tipo, data_criacao, fk_colaborador_empresa)
VALUES ('João Silva', 'joao@techguard.com', '11999999999', 'abc123def456ghi789jkl012mno345pqr678stu901vwx234yza567bcd890efgh', 1, '2023-02-01', 1);

INSERT INTO maquina (modelo, so, serial_number, status, setor, fk_maquina_empresa)
VALUES ('Dell PowerEdge T40', 'Ubuntu Server 22.04', 'SN123456789', 1, 'TI', 1);

INSERT INTO componente (tipo, modelo, valor, minimo, maximo, fk_componente_maquina)
VALUES 
('CPU', 'Intel Xeon E-2224G', 35.0, 10.0, 90.0, 1),
('RAM', 'Kingston 16GB DDR4', 45.0, 20.0, 85.0, 1);

INSERT INTO historico (data_captura, valor, fk_historico_componente)
VALUES 
('2025-04-04 10:30:00', 40.2, 1),
('2025-04-04 10:30:00', 50.8, 2);

INSERT INTO alerta (data_captura, valor, fk_alerta_componente)
VALUES 
('2025-04-04 10:35:00', 95.0, 1);

SHOW TABLES;

SELECT * FROM endereco_empresa;
SELECT * FROM empresa;
SELECT * FROM colaborador;
SELECT * FROM maquina;
SELECT * FROM componente;
SELECT * FROM historico;
SELECT * FROM alerta;


