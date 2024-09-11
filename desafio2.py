import textwrap

menu = """
Selecione uma das opções

[d] Depositar
[s] Sacar
[e] Extrato
[nc] Nova Conta
[l] Lista Contas
[nu] Novo Usuário
[q] Sair

=> """

LIMITE_SAQUE = 3
AGENCIA = '0001'
saldo = 0
limite = 500
extrato  = ''
numero_saques = 0
usuarios = []
contas = []


def depositar(saldo, valor, extrato):
    if valor > 0:
        saldo += valor
        extrato += f'Deposito: R$ {valor:.2f}\n'
        print('\n Deposito efetuado com Sucesso!')
    else:
        print('O valor a ser depositado não pode ser inferior ou igual a zero. Valor informado ')
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    saldo_baixo = valor > saldo
    limite_baixo = valor > limite
    saques_baixo = numero_saques >= limite_saques

    if limite_baixo:
        print('Valor informado superior ao limite diario R$ '+ str(limite))
    elif saldo_baixo:
        print('Valor informado R$ '+ valor + ' esta acima do seu saldo R$ '+ str(saldo)+ ' Saque não efetivado')
    elif saques_baixo:
        print('Limite de saque por dia atingido')
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print('Saque realizado com Sucesso, volte sempre!')
    else:
        print('Valro informado inválido')
    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print('\n EXTRATO ')
    print('Sem movimentação' if not extrato else extrato)
    print(f'\nsaldo: R$ {saldo:.2f}')
    print('\n_______')

def criar_usuario(usuarios):
    cpf = input('Digite o CPF sem traços ou pontos: ')
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print('CPF já cadastrado para outro usuário')
        return
    
    nome = input('Digite o nome: ')
    data_nascimento = input('Digite a data de nascimento - dd-mm-aaaa : ')
    endereco = input('Informe o endereço - Logradouro, nr - bairro - cidade/sigla estado: ')

    usuarios.append({'nome':nome, 'data_nascimento':data_nascimento, 'cpf': cpf, 'endereco':endereco})
    print('Usuário cadastrado com sucesso')

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario['cpf'] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input('Digite o cpf: ')
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print('\n Conta criada com sucesso')
        return {'agencia':agencia, 'numero_conta':numero_conta, 'usuario':usuario}
    
    print('\n Usuário nao encontrado')

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agencia: {conta['agencia']}
            C/C: {conta['numero_conta']}
            Titular: {conta['usuarios']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))


while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input('Digite o valor do deposito: '))
        saldo, extrato = depositar(saldo, valor, extrato)  
    
    elif opcao == "s":
        valor = float(input('Digite o valor do saque: '))
        saldo, extrato = sacar(saldo = saldo, valor = valor, extrato = extrato, limite = limite, numero_saques = numero_saques, limite_saques = LIMITE_SAQUE)
              
    elif opcao == "e":
        exibir_extrato(saldo, extrato = extrato)    

    elif opcao == "q":
        break

    elif opcao == 'nu':
        criar_usuario(usuarios)
    
    elif opcao == 'nc':
        numero_conta = len(contas) + 1
        conta = criar_conta(AGENCIA, numero_conta, usuarios)
        if conta:
            contas.append(conta)
    
    elif opcao == 'lc':
        listar_contas(contas)
    
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")