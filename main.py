# .....................
#       Imports            
# .....................

from services import (
    atualizar_status,
    buscar_email_funcionario,
    buscar_telefone_tutor,
    calcular_prioridade,
    criar_atendimento,
    criar_funcionario,
    criar_pet,
    criar_tutor,
    estatisticas_por_prioridade,
    estatisticas_por_status,
    listar_atendimentos,
    listar_pets,
    listar_tutores,
    login_funcionario,
    obter_severidade,
    obter_urgencia,
    prioridade_para_tela,
    status_para_tela,
)


# .........................
#  Aparência e interface :3   
# .........................

LARGURA = 78


def linha():
    print("─" * LARGURA)


def titulo(texto):
    print("\n╔" + "═" * LARGURA + "╗")
    print("║" + texto.center(LARGURA) + "║")
    print("╚" + "═" * LARGURA + "╝")
    print()


def subtitulo(texto):
    print("\n" + "─" * LARGURA)
    print(texto.center(LARGURA))
    print("─" * LARGURA)
    print()


def sucesso(mensagem):
    print(f"\n[OK] {mensagem}")


def erro(mensagem):
    print(f"\n[ERRO] {mensagem}")


def aviso(mensagem):
    print(f"\n[AVISO] {mensagem}")


def opcao(numero, texto):
    print(f"\n   [{numero}] {texto}")


def pausa():
    input("\nPressione ENTER para continuar...")


# ................................
# Funções de validação e leitura            
# ................................

def ler_inteiro(mensagem):
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            erro("Digite um número válido.")


def ler_decimal(mensagem):
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            erro("Digite um número válido.")


# .........................
#   Funcionários e Login            
# .........................

def cadastrar_funcionario():
    titulo("CADASTRO DE FUNCIONÁRIO")

    while True:
        nome = input("Nome: ").strip()
        if nome == "" or len(nome) < 2 or not nome.replace(" ", "").isalpha():
            erro("Nome inválido! Use apenas letras e digite um nome real.")
        else:
            break

    while True:
        email = input("Email: ").strip()
        if "@" not in email or "." not in email or len(email) < 5:
            erro("Formato de e-mail inválido! Certifique-se de usar '@' e '.'.")
        elif buscar_email_funcionario(email) is not None:
            aviso("Esse e-mail já está sendo utilizado. Tente novamente.")
        else:
            break

    while True:
        senha = input("Senha: ").strip()
        if len(senha) < 6:
            erro("Senha muito curta! A senha deve ter pelo menos 6 caracteres.")
        else:
            break

    id_funcionario = criar_funcionario(nome=nome, email=email, senha=senha)

    if id_funcionario is not None:
        sucesso(f"Funcionário cadastrado com sucesso! ID: {id_funcionario}")


# .........................
#        Tutores            
# .........................

def cadastrar_tutor():
    titulo("CADASTRO DE TUTOR")

    while True:
        nome = input("Nome do tutor: ").strip()
        if nome == "" or len(nome) < 2 or not nome.replace(" ", "").isalpha():
            erro("Nome inválido! Use apenas letras e digite um nome real.")
        else:
            break

    while True:
        telefone = input("Telefone: ").strip()
        if telefone == "":
            erro("Telefone obrigatório.")
        elif buscar_telefone_tutor(telefone) is not None:
            aviso("Esse telefone já está cadastrado.")
        else:
            break

    email = input("Email: ").strip()
    id_tutor = criar_tutor(nome=nome, telefone=telefone, email=email)

    if id_tutor is not None:
        sucesso(f"Tutor cadastrado com sucesso! ID: {id_tutor}")


def mostrar_tutores():
    tutores = listar_tutores()

    if tutores == []:
        aviso("Nenhum tutor cadastrado.")
        return False

    subtitulo("TUTORES CADASTRADOS")

    print(f"{'ID':<6} {'Nome':<28} {'Telefone':<18} {'Email'}")
    linha()
    print()

    for tutor in tutores:
        print(f"{tutor[0]:<6} {tutor[1]:<28} {tutor[2]:<18} {tutor[3]}")

    return True


# .........................
#          Pets          
# .........................

def cadastrar_pet():
    titulo("CADASTRO DE PET")

    if not mostrar_tutores():
        aviso("Cadastre um tutor primeiro.")
        return

    print()
    nome = input("Nome do pet: ").strip()
    especie = input("Espécie: ").strip()
    raca = input("Raça (opcional): ").strip()
    idade = ler_inteiro("Idade: ")
    peso = ler_decimal("Peso (kg): ")
    altura = ler_decimal("Altura (cm): ")
    id_tutor = ler_inteiro("ID do tutor: ")

    id_pet = criar_pet(
        nome=nome,
        especie=especie,
        raca=raca,
        idade=idade,
        peso=peso,
        altura=altura,
        id_tutor=id_tutor,
    )

    if id_pet is not None:
        sucesso(f"Pet cadastrado com sucesso! ID do pet: {id_pet}")


def mostrar_pets():
    pets = listar_pets()

    if pets == []:
        aviso("Nenhum pet cadastrado.")
        return False

    subtitulo("PETS CADASTRADOS")

    print(f"{'ID':<6} {'Nome':<24} {'Espécie':<18} {'Tutor'}")
    linha()
    print()

    for pet in pets:
        print(f"{pet[0]:<6} {pet[1]:<24} {pet[2]:<18} {pet[3]}")

    return True


# .........................
#      Atendimentos            
# .........................

def abrir_atendimento(id_funcionario):
    titulo("ABERTURA DE ATENDIMENTO")

    if not mostrar_pets():
        aviso("Cadastre um pet primeiro.")
        return

    print()
    id_pet = ler_inteiro("Digite o ID do pet: ")
    descricao = input("Observações: ").strip()

    if descricao == "":
        erro("A descrição não pode ficar vazia.")
        return

    nivel_severidade = obter_severidade()
    nivel_urgencia = obter_urgencia()

    score, prioridade = calcular_prioridade(nivel_severidade, nivel_urgencia)

    id_atendimento = criar_atendimento(
        id_pet=id_pet,
        id_funcionario=id_funcionario,
        descricao=descricao,
        severidade=nivel_severidade,
        urgencia=nivel_urgencia,
        score=score,
        prioridade=prioridade,
    )

    if id_atendimento is not None:
        titulo("RESULTADO FINAL")
        print(f"Score calculado: {score}")
        print(f"Prioridade de atendimento: {prioridade}")
        sucesso(f"Atendimento registrado com sucesso! ID: {id_atendimento}")


def imprimir_atendimentos(atendimentos):
    if atendimentos == []:
        aviso("Nenhum atendimento encontrado.")
        return

    titulo("LISTA DE ATENDIMENTOS")

    for atendimento in atendimentos:
        print(f"Atendimento #{atendimento[0]}")
        linha()
        print(f"Pet............. {atendimento[1]}")
        print(f"Tutor........... {atendimento[2]}")
        print(f"Funcionário..... {atendimento[3]}")
        print(f"Prioridade...... {prioridade_para_tela(atendimento[4])}")
        print(f"Status.......... {status_para_tela(atendimento[5])}")
        print(f"Data............ {atendimento[6]}")
        print()
        print("Descrição:")
        print(f"{atendimento[7]}")
        linha()
        print()


# .........................
#   Consultas e Cadastros            
# .........................

def menu_verificar_cadastros():
    while True:
        titulo("VERIFICAR CADASTROS")
        opcao("1", "Visualizar tutores cadastrados")
        opcao("2", "Visualizar pets cadastrados")
        opcao("3", "Voltar ao menu principal")

        escolha = input("\nEscolha uma opção: ")

        if escolha == "1":
            titulo("TUTORES CADASTRADOS")
            mostrar_tutores()
            pausa()

        elif escolha == "2":
            titulo("PETS CADASTRADOS")
            mostrar_pets()
            pausa()

        elif escolha == "3":
            break

        else:
            erro("Opção inválida! Digite 1, 2 ou 3.")


def menu_consultas():
    while True:
        titulo("CONSULTAS DE ATENDIMENTOS")
        opcao("1", "Listar todos os atendimentos")
        opcao("2", "Listar por status")
        opcao("3", "Listar por prioridade")
        opcao("4", "Listar por tutor")
        opcao("5", "Voltar")

        escolha_menu = input("\nEscolha uma opção: ")

        if escolha_menu == "1":
            imprimir_atendimentos(listar_atendimentos())

        elif escolha_menu == "2":
            subtitulo("FILTRAR POR STATUS")
            opcao("1", "Aberto")
            opcao("2", "Em progresso")
            opcao("3", "Finalizado")
            escolha = input("\nEscolha o status: ")

            if escolha == "1":
                status = "aberto"
            elif escolha == "2":
                status = "em_progresso"
            elif escolha == "3":
                status = "finalizado"
            else:
                erro("Opção inválida.")
                continue

            imprimir_atendimentos(listar_atendimentos("status", status))

        elif escolha_menu == "3":
            subtitulo("FILTRAR POR PRIORIDADE")
            opcao("1", "Baixa")
            opcao("2", "Média")
            opcao("3", "Alta")
            escolha = input("\nEscolha a prioridade: ")

            if escolha == "1":
                prioridade = "baixa"
            elif escolha == "2":
                prioridade = "media"
            elif escolha == "3":
                prioridade = "alta"
            else:
                erro("Opção inválida.")
                continue

            imprimir_atendimentos(listar_atendimentos("prioridade", prioridade))

        elif escolha_menu == "4":
            if not mostrar_tutores():
                continue
            id_tutor = ler_inteiro("\nDigite o ID do tutor: ")
            imprimir_atendimentos(listar_atendimentos("tutor", id_tutor))

        elif escolha_menu == "5":
            break

        else:
            erro("Opção inválida.")


# .......................
#  Status e Estatísticas           
# .......................

def menu_atualizar_status():
    titulo("ATUALIZAÇÃO DE STATUS")

    imprimir_atendimentos(listar_atendimentos())

    id_atendimento = ler_inteiro("Digite o ID do atendimento: ")

    subtitulo("NOVO STATUS")
    opcao("1", "Aberto")
    opcao("2", "Em progresso")
    opcao("3", "Finalizado")
    escolha = input("\nEscolha o novo status: ")

    if escolha == "1":
        novo_status = "aberto"
    elif escolha == "2":
        novo_status = "em_progresso"
    elif escolha == "3":
        novo_status = "finalizado"
    else:
        erro("Opção inválida.")
        return

    if atualizar_status(id_atendimento, novo_status):
        sucesso("Status atualizado com sucesso.")


def menu_estatisticas():
    titulo("ESTATÍSTICAS DO SISTEMA")

    subtitulo("TOTAL DE ATENDIMENTOS POR STATUS")
    for status, total in estatisticas_por_status():
        print(f"{status_para_tela(status):<20} {total}")

    subtitulo("TOTAL DE ATENDIMENTOS POR PRIORIDADE")
    for prioridade, total in estatisticas_por_prioridade():
        print(f"{prioridade_para_tela(prioridade):<20} {total}")

# .........................
#         Menu's    
# .........................

def painel_interno(id_funcionario):
    while True:
        titulo(f"PAINEL DE CONTROLE | OPERADOR ID: {id_funcionario}")
        opcao("1", "Cadastrar tutor")
        opcao("2", "Cadastrar pet")
        opcao("3", "Registrar novo atendimento")
        opcao("4", "Consultar atendimentos")
        opcao("5", "Verificar cadastros")
        opcao("6", "Atualizar status")
        opcao("7", "Estatísticas")
        opcao("8", "Cadastrar novo funcionário")
        opcao("9", "Sair da conta (Logout)")

        escolha = input("\nEscolha uma opção: ")

        if escolha == "1":
            cadastrar_tutor()

        elif escolha == "2":
            cadastrar_pet()

        elif escolha == "3":
            abrir_atendimento(id_funcionario)

        elif escolha == "4":
            menu_consultas()

        elif escolha == "5":
            menu_verificar_cadastros()

        elif escolha == "6":
            menu_atualizar_status()

        elif escolha == "7":
            menu_estatisticas()

        elif escolha == "8":
            cadastrar_funcionario()

        elif escolha == "9":
            print("\nSaindo da conta...")
            break

        else:
            erro("Opção inválida.")


def run():
    titulo("SISTEMA DE GESTÃO VETERINÁRIA")

    while True:
        titulo("PORTAL DO VETERINÁRIO")
        opcao("1", "Entrar (Login de Funcionário)")
        opcao("2", "Cadastrar funcionário")
        opcao("3", "Sair do Sistema")

        escolha = input("\nEscolha uma opção: ")

        if escolha == "1":
            titulo("LOGIN")
            id_funcionario = login_funcionario()

            if id_funcionario is not None:
                painel_interno(id_funcionario)

        elif escolha == "2":
            titulo("NOVO FUNCIONÁRIO")
            cadastrar_funcionario()

        elif escolha == "3":
            print("\nEncerrando o sistema... Até logo!")
            break

        else:
            erro("Opção inválida! Digite 1, 2 ou 3.")


if __name__ == "__main__":
    run()
    # Isso faz o programa rodar apenas quando este arquivo é executado diretamente :)
