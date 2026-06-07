from database import get_connection


# Dicionários criados para futura integração com banco de dados automação :p
# Dict tipo de problema (severidade 1, 2 ou 3)
severidade_dict = {
    "check-up": 1,
    "vacina": 1,
    "alergia": 1,
    "ferimento superficial": 1,

    "diarreia": 2,
    "febre": 2,
    "vômito": 2,
    "infecção leve": 2,
    "imobilidade": 2,

    "ferimento grave": 3,
    "fratura": 3,
    "convulsão": 3,
    "dificuldade respiratória": 3,
    "trauma": 3,
    "infecção grave": 3
}

# Dict estado do animal (urgência 1, 2 ou 3)
urgencia_dict = {
    "nenhum sintoma": 1,
    "sintoma leve": 1,

    "sintoma persistente": 2,
    "sintoma com agravamento": 2,

    "grave desconforto": 3,
    "grave dor": 3,
    "agônico": 3,
    "perda de consciência": 3
}


def test_database():
    connection = get_connection()

    if connection:
        print("Service conseguiu se conectar ao banco!")
        connection.close()


def prioridade_para_banco(prioridade):
    if prioridade == "Baixa":
        return "baixa"
    elif prioridade == "Média":
        return "media"
    else:
        return "alta"


def prioridade_para_tela(prioridade):
    if prioridade == "baixa":
        return "Baixa"
    elif prioridade == "media":
        return "Média"
    else:
        return "Alta"


def status_para_tela(status):
    if status == "aberto":
        return "Aberto"
    elif status == "em_progresso":
        return "Em progresso"
    else:
        return "Finalizado"


# Obter severidade
def obter_severidade():
    print("=== TIPO DE PROBLEMA ===")
    print("1 - Check-up")
    print("2 - Vacina")
    print("3 - Alergia")
    print("4 - Ferimento superficial")
    print("5 - Diarreia")
    print("6 - Febre")
    print("7 - Vômito")
    print("8 - Infecção leve")
    print("9 - Imobilidade")
    print("10 - Ferimento grave")
    print("11 - Fratura")
    print("12 - Convulsão")
    print("13 - Dificuldade respiratória")
    print("14 - Trauma")
    print("15 - Infecção grave")

    while True:
        try:
            opcao = int(input("Escolha uma opção: "))
        except ValueError:
            print("Opção inválida. Digite um número.")
        else:
            if 1 <= opcao <= 15:
                if opcao in [1, 2, 3, 4]:
                    return 1
                elif opcao in [5, 6, 7, 8, 9]:
                    return 2
                else:
                    return 3
            else:
                print("Número fora do intervalo.")


# Obter urgência
def obter_urgencia():
    print("\n=== ESTADO DO ANIMAL ===")
    print("1 - Nenhum sintoma")
    print("2 - Sintoma leve")
    print("3 - Sintoma persistente")
    print("4 - Sintoma com agravamento")
    print("5 - Grave desconforto")
    print("6 - Grave dor")
    print("7 - Agônico")
    print("8 - Perda de consciência")

    while True:
        try:
            opcao = int(input("Escolha uma opção: "))
        except ValueError:
            print("Opção inválida. Digite um número.")
        else:
            if 1 <= opcao <= 8:
                if opcao in [1, 2]:
                    return 1
                elif opcao in [3, 4]:
                    return 2
                else:
                    return 3
            else:
                print("Número fora do intervalo.")


# Calcular prioridade
# LEMBRETE: NO BANCO ESTÁ SEM ACENTO!
def calcular_prioridade(severidade, urgencia):
    score = severidade * urgencia

    if score <= 3:
        return score, "Baixa"
    elif score <= 6:
        return score, "Média"
    else:
        return score, "Alta"


def buscar_email_funcionario(email):
    connection = get_connection()
    if connection is None:
        return None

    cursor = connection.cursor()
    cursor.execute("SELECT email FROM funcionario WHERE email = %s", (email,))
    resultado = cursor.fetchall()
    connection.close()

    if resultado == []:
        return None
    else:
        return resultado


def buscar_telefone_tutor(telefone):
    connection = get_connection()
    if connection is None:
        return None

    cursor = connection.cursor()
    cursor.execute("SELECT telefone FROM tutor WHERE telefone = %s", (telefone,))
    resultado = cursor.fetchall()
    connection.close()

    if resultado == []:
        return None
    else:
        return resultado


def criar_funcionario(nome, email, senha):
    connection = get_connection()
    if connection is None:
        return None

    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO funcionario (nome, email, senha) VALUES (%s, %s, %s)",
        (nome, email, senha)
    )
    connection.commit()
    id_funcionario = cursor.lastrowid
    connection.close()
    return id_funcionario



def criar_usuario_adm(nome, email, senha):
    return criar_funcionario(nome, email, senha)


def criar_tutor(nome, telefone, email):
    connection = get_connection()
    if connection is None:
        return None

    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO tutor (nome, telefone, email) VALUES (%s, %s, %s)",
        (nome, telefone, email)
    )
    connection.commit()
    id_tutor = cursor.lastrowid
    connection.close()
    return id_tutor


def criar_user(nome, telefone, email):
    return criar_tutor(nome, telefone, email)


def tutor_existe(id_tutor):#Isso é para verificar se o tutor existe antes de cadastrar um pet, evitando erros de chave estrangeira!
    connection = get_connection()
    if connection is None:
        return False

    cursor = connection.cursor()
    cursor.execute(
        "SELECT id_tutor FROM tutor WHERE id_tutor = %s",
        (id_tutor,)
    )

    resultado = cursor.fetchone()
    connection.close()

    if resultado is None:
        return False
    else:
        return True


def criar_pet(nome, especie, raca, idade, peso, altura, id_tutor):
    # Verifica se o tutor existe antes de tentar cadastrar o pet
    if not tutor_existe(id_tutor):
        print("Erro: tutor não encontrado. Cadastre o tutor antes de cadastrar o pet.")
        return None

    connection = get_connection()
    if connection is None:
        return None

    cursor = connection.cursor()

    try:
        cursor.execute(
            """
            INSERT INTO pet (nome, especie, raca, idade, peso, altura, id_tutor)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            """,
            (nome, especie, raca, idade, peso, altura, id_tutor)
        )

        connection.commit()
        id_pet = cursor.lastrowid
        return id_pet

    except Exception as erro:
        print("Erro ao cadastrar pet:", erro)
        return None

    finally:
        connection.close()

def listar_tutores():
    connection = get_connection()
    if connection is None:
        return []

    cursor = connection.cursor()
    cursor.execute("SELECT id_tutor, nome, telefone, email FROM tutor ORDER BY nome")
    resultado = cursor.fetchall()
    connection.close()
    return resultado



def mostrar_usuarios_client():
    return listar_tutores()


def listar_pets():
    connection = get_connection()
    if connection is None:
        return []

    cursor = connection.cursor()
    cursor.execute(
        """
        SELECT pet.id_pet, pet.nome, pet.especie, tutor.nome
        FROM pet
        INNER JOIN tutor ON pet.id_tutor = tutor.id_tutor
        ORDER BY pet.nome
        """
    )
    resultado = cursor.fetchall()
    connection.close()
    return resultado


def criar_atendimento(id_pet, id_funcionario, descricao, severidade, urgencia, score, prioridade):
    connection = get_connection()
    if connection is None:
        return None

    prioridade_banco = prioridade_para_banco(prioridade)

    cursor = connection.cursor()
    cursor.execute(
        """
        INSERT INTO atendimento
        (id_pet, id_funcionario, descricao, severidade, urgencia, score, prioridade, status)
        VALUES (%s, %s, %s, %s, %s, %s, %s, 'aberto')
        """,
        (id_pet, id_funcionario, descricao, severidade, urgencia, score, prioridade_banco)
    )
    connection.commit()
    id_atendimento = cursor.lastrowid
    connection.close()
    return id_atendimento



def criar_request(id_pet, id_funcionario, descricao, severidade, urgencia, score, prioridade):
    return criar_atendimento(id_pet, id_funcionario, descricao, severidade, urgencia, score, prioridade)


def login_funcionario():
    email = input("Digite o seu E-mail de login: ")
    email_limpo = email.strip()

    connection = get_connection()
    if connection is None:
        return None

    cursor = connection.cursor()
    cursor.execute(
        "SELECT id_funcionario, nome, email, senha FROM funcionario WHERE email = %s",
        (email_limpo,)
    )
    usuario_encontrado = cursor.fetchall()
    connection.close()

    if not usuario_encontrado:
        print("E-mail não encontrado!")
        return None

    senha = input("Digite a sua senha: ")
    senha_limpa = senha.strip()
    senha_salva_no_banco = usuario_encontrado[0][3]

    if senha_limpa != senha_salva_no_banco:
        print("Senha incorreta!")
        return None

    else:
        nome_funcionario = usuario_encontrado[0][1]
        id_funcionario = usuario_encontrado[0][0]

        print(f"Login realizado com sucesso! Bem-vindo(a), {nome_funcionario}.")
        return id_funcionario



def login_adm():
    return login_funcionario()


def listar_atendimentos(filtro=None, valor=None):
    connection = get_connection()
    if connection is None:
        return []

    comando = """
        SELECT atendimento.id_atendimento,
               pet.nome,
               tutor.nome,
               funcionario.nome,
               atendimento.prioridade,
               atendimento.status,
               atendimento.data_inicio,
               atendimento.descricao
        FROM atendimento
        INNER JOIN pet ON atendimento.id_pet = pet.id_pet
        INNER JOIN tutor ON pet.id_tutor = tutor.id_tutor
        INNER JOIN funcionario ON atendimento.id_funcionario = funcionario.id_funcionario
    """

    parametros = ()

    if filtro == "status":
        comando += " WHERE atendimento.status = %s"
        parametros = (valor,)
    elif filtro == "prioridade":
        comando += " WHERE atendimento.prioridade = %s"
        parametros = (valor,)
    elif filtro == "tutor":
        comando += " WHERE tutor.id_tutor = %s"
        parametros = (valor,)

    comando += " ORDER BY atendimento.data_inicio DESC"

    cursor = connection.cursor()
    cursor.execute(comando, parametros)
    resultado = cursor.fetchall()
    connection.close()
    return resultado


def buscar_status_atendimento(id_atendimento):
    connection = get_connection()
    if connection is None:
        return None

    cursor = connection.cursor()
    cursor.execute(
        "SELECT status FROM atendimento WHERE id_atendimento = %s",
        (id_atendimento,)
    )
    resultado = cursor.fetchone()
    connection.close()

    if resultado is None:
        return None
    return resultado[0]


def atualizar_status(id_atendimento, novo_status):
    status_atual = buscar_status_atendimento(id_atendimento)

    if status_atual is None:
        print("Atendimento não encontrado!")
        return False

    if status_atual == "finalizado":
        print("Não é permitido reabrir ou alterar um atendimento finalizado.")
        return False

    connection = get_connection()
    if connection is None:
        return False

    cursor = connection.cursor()

    if novo_status == "finalizado":
        cursor.execute(
            """
            UPDATE atendimento
            SET status = %s, data_final = NOW()
            WHERE id_atendimento = %s
            """,
            (novo_status, id_atendimento)
        )
    else:
        cursor.execute(
            """
            UPDATE atendimento
            SET status = %s
            WHERE id_atendimento = %s
            """,
            (novo_status, id_atendimento)
        )

    connection.commit()
    connection.close()
    return True


def estatisticas_por_status():
    connection = get_connection()
    if connection is None:
        return []

    cursor = connection.cursor()
    cursor.execute(
        """
        SELECT status, COUNT(*)
        FROM atendimento
        GROUP BY status
        """
    )
    resultado = cursor.fetchall()
    connection.close()
    return resultado


def estatisticas_por_prioridade():
    connection = get_connection()
    if connection is None:
        return []

    cursor = connection.cursor()
    cursor.execute(
        """
        SELECT prioridade, COUNT(*)
        FROM atendimento
        GROUP BY prioridade
        """
    )
    resultado = cursor.fetchall()
    connection.close()
    return resultado
