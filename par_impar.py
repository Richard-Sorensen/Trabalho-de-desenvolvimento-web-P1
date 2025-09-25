



#Primeiro pedimos para o usuario dois numeros
num_1 = int(input("Digite um numero: "))
num_2 = int(input("Digite outro numero: "))
#Primeiro vamos fazer a soma dos dois numeros
soma = num_1 + num_2
#Agora vamos verificar se a soma e par ou impar
pariedade = soma % 2
#Agora vamos adicionar a condicional
if pariedade == 0:
    print("A soma dos numeros {} e {} e {}, que e um numero par".format(num_1, num_2, soma))
else:
    print("A soma dos numeros {} e {} e {}, que e um numero impar".format(num_1, num_2, soma))
    
    
    
    
    
    
    
    
    