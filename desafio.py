menu = """
Selecione uma das opções

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato  = []
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = input('Digite o valor do deposito: ')
        valor_float = float(valor)
        if (valor_float <= 0 ):
             print('O valor a ser depositado não pode ser inferior ou igual a zero. Valor informado '+ '( '+ valor + ' )')
        else:
            saldo += valor_float
            extrato.append('Deposito - R$ '+ valor)
            print('\n Deposito efetuado com Sucesso!')
    elif opcao == "s":
        if (numero_saques < 3):
            valor = input('Digite o valor do saque: ')
            valor_float = float(valor)
            if(valor_float > limite):
                print('Valor informado superior ao limite diario R$ '+ str(limite))
            elif (valor_float > saldo):
                print('Valor informado R$ '+ valor + ' esta acima do seu saldo R$ '+ str(saldo)+ ' Saque não efetivado')
            else:
                saldo -= valor_float
                numero_saques += 1
                extrato.append('Saque - R$ '+ valor)
                print('Saque realizado com Sucesso, volte sempre!')                
        else:
            print('Limite de saque por dia atingido')    
    elif opcao == "e":
        print('EXTRATO \n')
        for dado in extrato: 
            print(dado)
        print('\nSaldo atual..... R$ '+ str(saldo))
    elif opcao == "q":
        break
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")