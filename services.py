from database import get_connection


# ...................................
# Aparência e interface (funções) :3           
# ...................................

LARGURA = 78


def linha():
    print("─" * LARGURA)


def subtitulo(texto):
    print("\n" + "─" * LARGURA)
    print(texto.center(LARGURA))
    print("─" * LARGURA)
    print()


def erro(mensagem):
    print(f"\n[ERRO] {mensagem}")


def aviso(mensagem):
    print(f"\n[AVISO] {mensagem}")


def sucesso(mensagem):
    print(f"\n[OK] {mensagem}")


def opcao(numero, texto):
    print(f"\n   [{numero}] {texto}")


# .........................
#      Banco x Tela            
# .........................

# No banco os valores ficam sem acento.
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


# .............................
#  Sisteminha de Prioridades            
# .............................


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


# Obter severidade
def obter_severidade():
    subtitulo("TIPO DE PROBLEMA / SEVERIDADE")

    print("PROBLEMAS LEVES")
    opcao("1", "Check-up")
    opcao("2", "Vacina")
    opcao("3", "Alergia")
    opcao("4", "Ferimento superficial")

    print("\nPROBLEMAS MODERADOS")
    opcao("5", "Diarreia")
    opcao("6", "Febre")
    opcao("7", "Vômito")
    opcao("8", "Infecção leve")
    opcao("9", "Imobilidade")

    print("\nPROBLEMAS GRAVES")
    opcao("10", "Ferimento grave")
    opcao("11", "Fratura")
    opcao("12", "Convulsão")
    opcao("13", "Dificuldade respiratória")
    opcao("14", "Trauma")
    opcao("15", "Infecção grave")

    while True:
        try:
            escolha = int(input("\nEscolha uma opção: "))
        except ValueError:
            erro("Opção inválida. Digite um número.")
        else:
            if 1 <= escolha <= 15:
                if escolha in [1, 2, 3, 4]:
                    return 1
                elif escolha in [5, 6, 7, 8, 9]:
                    return 2
                else:
                    return 3
            else:
                aviso("Número fora do intervalo. Escolha uma opção de 1 a 15.")


# Obter urgência
def obter_urgencia():
    subtitulo("ESTADO DO ANIMAL / URGÊNCIA")

    print("BAIXA URGÊNCIA")
    opcao("1", "Nenhum sintoma")
    opcao("2", "Sintoma leve")

    print("\nMÉDIA URGÊNCIA")
    opcao("3", "Sintoma persistente")
    opcao("4", "Sintoma com agravamento")

    print("\nALTA URGÊNCIA")
    opcao("5", "Grave desconforto")
    opcao("6", "Grave dor")
    opcao("7", "Agônico")
    opcao("8", "Perda de consciência")

    while True:
        try:
            escolha = int(input("\nEscolha uma opção: "))
        except ValueError:
            erro("Opção inválida. Digite um número.")
        else:
            if 1 <= escolha <= 8:
                if escolha in [1, 2]:
                    return 1
                elif escolha in [3, 4]:
                    return 2
                else:
                    return 3
            else:
                aviso("Número fora do intervalo. Escolha uma opção de 1 a 8.")


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

# .........................
#  Teste Conexão Banco         
# .........................

def test_database():
    connection = get_connection()

    if connection:
        sucesso("Service conseguiu se conectar ao banco!")
        connection.close()


# .........................
#         Login            
# .........................

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
        erro("E-mail não encontrado.")
        return None

    senha = input("Digite a sua senha: ")
    senha_limpa = senha.strip()
    senha_salva_no_banco = usuario_encontrado[0][3]

    if senha_limpa != senha_salva_no_banco:
        erro("Senha incorreta.")
        return None

    nome_funcionario = usuario_encontrado[0][1]
    id_funcionario = usuario_encontrado[0][0]

    sucesso(f"Login realizado com sucesso! Bem-vindo(a), {nome_funcionario}.")
    return id_funcionario


# .........................
#         Tutores           
# .........................

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


def tutor_existe(id_tutor):
    # Isso é para verificar se o tutor existe antes de cadastrar um pet,
    # evitando erros de chave estrangeira.
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


def listar_tutores():
    connection = get_connection()
    if connection is None:
        return []

    cursor = connection.cursor()
    cursor.execute("SELECT id_tutor, nome, telefone, email FROM tutor ORDER BY nome")
    resultado = cursor.fetchall()
    connection.close()
    return resultado


# .........................
#         Pets            
# .........................

def criar_pet(nome, especie, raca, idade, peso, altura, id_tutor):
    # Verifica se o tutor existe antes de tentar cadastrar o pet.
    if not tutor_existe(id_tutor):
        erro("Tutor não encontrado. Cadastre o tutor antes de cadastrar o pet.")
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

    except Exception as erro_banco:
        print("\n[ERRO] Erro ao cadastrar pet:", erro_banco)
        return None

    finally:
        connection.close()


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


# .........................
#      Atendimentos            
# .........................

def pet_existe(id_pet):
    # Verifica se o pet existe antes de registrar um atendimento,
    # evitando erros de chave estrangeira.
    connection = get_connection()
    if connection is None:
        return False

    cursor = connection.cursor()
    cursor.execute(
        "SELECT id_pet FROM pet WHERE id_pet = %s",
        (id_pet,)
    )

    resultado = cursor.fetchone()
    connection.close()

    if resultado is None:
        return False
    else:
        return True


def criar_atendimento(id_pet, id_funcionario, descricao, severidade, urgencia, score, prioridade):
    if not pet_existe(id_pet):
        erro("Pet não encontrado. Cadastre o pet antes de registrar o atendimento.")
        return None

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
        erro("Atendimento não encontrado.")
        return False

    if status_atual == "finalizado":
        aviso("Não é permitido reabrir ou alterar um atendimento finalizado.")
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


# .........................
#       Atendimentos            
# .........................

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


