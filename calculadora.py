


print ('_'*10 + 'Bem vindo a calculadora' + '_'*10)
#Primeiro pedimos para o usuario dois numeros
num_1 = float(input('Digite o primeiro numero: '))
num_2 = float(input('Digite o segundo numero: '))
#Agora pedimos para o usuario escolher a operacao
print ( '[ 1 ] Soma \n[ 2 ] Subtracao \n[ 3 ] Multiplicacao \n[ 4 ] Divisao' )
escolha = int(input('Escolha a operacao que deseja fazer: '))
#Agora vamos fazer a condicional para cada operacao

    #Se o usuario escolher a opcao 1, faremos a soma
if escolha == 1:
    soma = num_1 + num_2
    print ('A soma entre {} e {} e igual a {}'.format(num_1, num_2, soma)) 
    
    #Se o usuario escolher a opcao 2, faremos a subtracao
elif escolha == 2:
    subtracao = num_1 - num_2
    print ('A subtracao entre {} e {} e igual a {}'.format(num_1, num_2, subtracao))
    
    #Se o usuario escolher a opcao 3, faremos a multiplicacao
elif escolha == 3:
    multiplicacao = num_1 * num_2
    print ('A multiplicacao entre {} e {} e igual a {}'.format(num_1, num_2, multiplicacao))
    
    #Se o usuario escolher a opcao 4, faremos a divisao
elif escolha == 4:
    divisao = num_1 / num_2
    print ('A divisao entre {} e {} e igual a {}'.format(num_1, num_2, divisao))
else:
    print ('Opcao invalida')
print ('_'*20 + 'FIM' + '_'*20)







