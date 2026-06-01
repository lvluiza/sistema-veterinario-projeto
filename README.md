# Projeto-Integrador
Projeto Intregrador - Primeiro Semetres de SIstemas de Informação
Integrantes: Augusto, Felipe, Gabriela, Guilherme e Luiza. 
Projeto Integrador - Sistema Veterinário

Objetivo:
Garantir persistência de dados utilizando MySQL.

Tecnologias utilizadas:
- Python
- MySQL
- SQL

Funcionalidades:
- Cadastro de tutores
- Cadastro de funcionários
- Cadastro de pets
- Registro de atendimentos veterinários
- Controle de prioridade e status

Entidades do banco:
- funcionario
- tutor
- pet
- atendimento

Relacionamentos:
- Um tutor pode possuir vários pets.
- Um pet pertence a apenas um tutor.
- Um atendimento pertence a um pet.
- Um atendimento é realizado por um funcionário.

Integridade referencial:
O sistema utiliza FOREIGN KEY para impedir registros órfãos.

Exemplos:
- Não é possível cadastrar um pet sem tutor.
- Não é possível cadastrar atendimento sem pet.
- Não é possível cadastrar atendimento sem funcionário.

Arquivos:
- sistema.py
- banco.sql
- README.txt
