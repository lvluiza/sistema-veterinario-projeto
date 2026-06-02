create database if not exists vet_db;

USE vet_db;

CREATE TABLE owner (
id_dono int auto_increment primary key,
nome varchar(20) not null,
telefone varchar(20)not null unique
);

CREATE TABLE pet ( 
    id_pet int auto_increment primary key,
    nome varchar (20) not null,
    especie varchar (20) not null,
    raca varchar (20),
    idade int, 
    peso decimal (5,2) not null,
    altura decimal (5,2) not null,
    dono_id int not null,
    foreign key (dono_id) references owner(id_dono)
);

-- Tabela responsável pelos atentimentos. O usuário não irá preencher os campos de gravidade, urgência e prioridade. 
-- Prioridade será calculada pelo sistema com base na gravidade e urgência. 
-- O campo end_date não é obrigatório, pois pode ser preenchido quando a consulta for concluída. 
CREATE TABLE appointment ( 
    id_app int auto_increment primary key, 
    id_pet int not null, 
    data_inicio date not null, 
    data_final date,
    status enum('open', 'in progress', 'closed') not null,
    descricao text,
    gravidade int not null,
    urgencia int not null,
    prioridade int not null,
    FOREIGN KEY (id_pet) REFERENCES pet(id)
);

-- Cadastro de usuários
CREATE TABLE IF not exists requester_user (
    id_dono INT AUTO_INCREMENT primary key,
    nome VARCHAR(100) not null,
    telefone VARCHAR(10) not null,
    email VARCHAR(120) not null
);
