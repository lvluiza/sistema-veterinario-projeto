# Projeto Integrador I – Sistema Veterinário

## Descrição do Projeto

O Sistema Veterinário foi desenvolvido como atividade da disciplina Projeto Integrador I do curso de Sistemas de Informação.

O sistema tem como objetivo auxiliar clínicas veterinárias no gerenciamento de funcionários, tutores, animais e atendimentos, permitindo o armazenamento organizado das informações e o acompanhamento dos casos registrados.

A aplicação foi desenvolvida utilizando Python e MySQL, com interface em terminal (CLI).

---

## Funcionalidades

O sistema permite:

* Cadastro de funcionários
* Login de funcionários
* Cadastro de tutores
* Cadastro de pets
* Registro de atendimentos veterinários
* Classificação automática de prioridade
* Consulta de atendimentos
* Atualização de status
* Estatísticas por prioridade
* Estatísticas por status


---

## Regra de Prioridade

A prioridade dos atendimentos é calculada automaticamente com base em dois critérios:

### Severidade

| Valor | Situação            |
| ----- | ------------------- |
| 1     | Problemas leves     |
| 2     | Problemas moderados |
| 3     | Problemas graves    |

### Urgência

| Valor | Situação       |
| ----- | -------------- |
| 1     | Baixa urgência |
| 2     | Média urgência |
| 3     | Alta urgência  |

### Cálculo

Prioridade = Severidade × Urgência

### Classificação

| Resultado | Prioridade |
| --------- | ---------- |
| 1 a 3     | Baixa      |
| 4 a 6     | Média      |
| 7 a 9     | Alta       |

---

## Tecnologias Utilizadas

* Python 3.11
* MySQL Workbench
* SQL
* GitHub

---

## Banco de Dados

### Entidades

* funcionario
* tutor
* pet
* atendimento

### Relacionamentos

* Um tutor pode possuir vários pets.
* Um pet pertence a apenas um tutor.
* Um atendimento pertence a um pet.
* Um atendimento é realizado por um funcionário.

### Integridade Referencial

O sistema utiliza chaves estrangeiras (FOREIGN KEY) para garantir a consistência dos dados.

Exemplos:

* Não é possível cadastrar um pet sem tutor.
* Não é possível registrar atendimento sem pet.
* Não é possível registrar atendimento sem funcionário.

---

## Estrutura do Projeto

```text
Projeto_Veterinaria/
│
├── main.py
├── services.py
├── database.py
├── schema.sql
├── README.md
```

### Arquivos

#### main.py

Responsável pela interface principal do sistema e navegação dos menus.

#### services.py

Contém as regras de negócio e funcionalidades do sistema.

#### database.py

Responsável pela conexão com o banco de dados MySQL.

#### schema.sql

Script de criação do banco de dados e das tabelas utilizadas pelo sistema.

---

## Instalação

### 1. Instalar dependências

```bash
python -m pip install mysql-connector-python
```

### 2. Criar o banco de dados

Executar o arquivo:

```text
schema.sql
```

no MySQL Workbench.

### 3. Configurar conexão

Editar o arquivo:

```python
database.py
```

e informar:

```text
host
user
password
database
```

de acordo com sua instalação local do MySQL.

---

## Execução

No terminal:

```bash
python main.py
```

ou

```bash
py main.py
```

---

## Integrantes

* Augusto Poinha
* Felipe Salvio
* Gabriela Saugo
* Guilherme Silva
* Luiza Leão

---

