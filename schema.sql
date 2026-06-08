CREATE DATABASE IF NOT EXISTS vet_db;

USE vet_db;

CREATE TABLE IF NOT EXISTS funcionario (
    id_funcionario INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    senha VARCHAR(100) NOT NULL
);


CREATE TABLE IF NOT EXISTS tutor (
    id_tutor INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(50) NOT NULL,
    telefone VARCHAR(20) NOT NULL UNIQUE,
    email VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS pet (
    id_pet INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(50) NOT NULL,
    especie VARCHAR(30) NOT NULL,
    raca VARCHAR(30),
    idade INT,
    peso DECIMAL(5,2) NOT NULL,
    altura DECIMAL(5,2) NOT NULL,
    id_tutor INT NOT NULL,

    FOREIGN KEY (id_tutor)
    REFERENCES tutor(id_tutor)
);

CREATE TABLE IF NOT EXISTS atendimento (
    id_atendimento INT AUTO_INCREMENT PRIMARY KEY,

    id_pet INT NOT NULL,
    id_funcionario INT NOT NULL,

    data_inicio DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    data_final DATETIME,

    descricao TEXT NOT NULL,

    severidade INT NOT NULL,
    urgencia INT NOT NULL,
    score INT NOT NULL,

    prioridade ENUM('baixa', 'media', 'alta') NOT NULL,

    status ENUM(
        'aberto',
        'em_progresso',
        'finalizado'
    ) NOT NULL DEFAULT 'aberto',

    observacoes TEXT,

    FOREIGN KEY (id_pet)
    REFERENCES pet(id_pet),

    FOREIGN KEY (id_funcionario)
    REFERENCES funcionario(id_funcionario)
);
