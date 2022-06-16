entrada =[]

while True:
    #Dá input do item da lista, que entra como string por padrão
    dado = input("Digite um item: ")

    #Testa se o valor inputado é um número
    if dado.isdigit():
        #Se for um número, transforma em inteiro e adiciona na lista
        entrada.append(int(dado))
    else:
        #Se for string, apenas adiciona na lista como está
        entrada.append(dado)

    teste = input('Deseja incluir mais um item? (s ou n): ')
    if teste == 'n':
        print('Fim \n')
        break
    else:
        continue

#Leitura da lista gerada com o input e dos tipos
#Esta parte não faz parte do código, apenas para demonstrar em tela os tipos
for i in entrada:
    print(f'{i} Tipo {type(i)}')

lista_inteiros = list()
lista_strings = list()

#Gera as listas com apenas strings e a lista com apenas inteiros
for i in entrada:
    if type(i) == int:
        lista_inteiros.append(i)
    else:
        lista_strings.append(i)

print(f'Lista de inteiros:  {lista_inteiros} \n')
print(f'Lista de strings:  {lista_strings} \n')

