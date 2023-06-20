#                  Trabalho Prático | Programação II               #
# Grupo: David de Assis, Davidson de Carvalho & Sofia de Alcantara #
# Algoritmo de Ordenação Utilizado:             MergeSort          #


import pickle

def comparacao(m1, m2, dicionario):      

    nome_Aluno1, semestre_Aluno1, notas_Aluno1, faltas_Aluno1 = dicionario[m1]
    nome_Aluno2, semestre_Aluno2, notas_Aluno2, faltas_Aluno2 = dicionario[m2]
        
    notaFinal_Aluno1 = 0
    notaFinal_Aluno2 = 0
    
    ano1 = semestre_Aluno1[0]
    ano2 = semestre_Aluno2[0]

    periodo1 = semestre_Aluno1[1]
    periodo2 = semestre_Aluno2[1]
    
    # Cálculo dos pontos extras das faltas + Garantindo que a nota nunca ultrapassará 100 pontos

    notaFinal_Aluno1 = sum(notas_Aluno1)

    if faltas_Aluno1 == 0:
         notaFinal_Aluno1 += 2
    
    if notaFinal_Aluno1 > 100:
         notaFinal_Aluno1 = 100

    notaFinal_Aluno2 = sum(notas_Aluno2)

    if faltas_Aluno2 == 0:
         notaFinal_Aluno2 += 2
    
    if notaFinal_Aluno2 > 100:
         notaFinal_Aluno2 = 100
    
    #  Testando o ano e período dos alunos
    if ano1 < ano2: return True
    if ano1 > ano2: return False
    
    if periodo1 < periodo2: return True
    if periodo1 > periodo2: return False

    # Testando a nota final
    if notaFinal_Aluno1 < notaFinal_Aluno2: return True
    if notaFinal_Aluno1 > notaFinal_Aluno2: return False

    # Testando o nome
    if nome_Aluno1 > nome_Aluno2: return True
    if nome_Aluno1 < nome_Aluno2: return False

    # Testando a matrícula
    if m1 > m2: return True
    if m1 < m2: return False


# ALGORITMO DE ORDENÇÃO - Dividindo a sequência ao meio. Ou seja, separando a lista de matrícula em listas menores.

def mSort(lista, dicionario):
        
	if len(lista) > 1:
                
		meio = len(lista) // 2
		lista_Esquerda = lista[: meio]
		lista_Direita = lista[meio: ]
    
		mSort(lista_Esquerda, dicionario)
		mSort(lista_Direita, dicionario)
		
		merge(lista, dicionario, lista_Esquerda, lista_Direita)

def merge(lista, dicionario, lista_Esquerda, lista_Direita):
     
    i = 0
    j = 0
    k = 0    

    while i < len(lista_Esquerda) and j < len(lista_Direita):
    
        m1 = lista_Esquerda[i]
        m2 = lista_Direita[j]
    
        if comparacao(m1, m2, dicionario): 
            lista[k] = lista_Esquerda[i]
            i += 1

        else:
            lista[k] = lista_Direita[j]
            j += 1
        
        k += 1

    while i < len(lista_Esquerda):
        lista[k] = lista_Esquerda[i]
        i += 1
        k += 1

    while j < len(lista_Direita):
        lista[k] = lista_Direita[j]
        j += 1
        k += 1

# MAIN: Função principal - Abrindo o arquivo de entrada
def main():

    lista_Matriculas = []                       
    
    with open('entrada.bin', 'rb') as file:

        dicionario = pickle.load(file)            

    for chave in dicionario:                      
        lista_Matriculas.append(chave)

    mSort(lista_Matriculas, dicionario)
 
    with open('saida.txt', 'w', encoding=' utf8') as arq:
        for chave in range(len(lista_Matriculas)-1, -1, -1):
             
            msg = ''
            nota_final = 0
            soma_notas = 0
        
            _, _, notas, faltas = dicionario[lista_Matriculas[chave]]

            soma_notas += notas[0] + notas[1] + notas[2]

            msg += f'{notas[0]}+{notas[1]}+{notas[2]}'

            if notas[3] > 0:
                soma_notas += notas[3]
                msg += f' +{notas[3]}E'

            if faltas == 0:
                soma_notas += 2
                msg += ' +2P'
            
            if soma_notas > 100:
                nota_final = 100
            else: 
                nota_final = soma_notas

            arq.write(f'{dicionario[lista_Matriculas[chave]][1][0]}/{dicionario[lista_Matriculas[chave]][1][1]} {lista_Matriculas[chave]} {dicionario[lista_Matriculas[chave]][0]} - {nota_final} ({msg} = {soma_notas})\n')

if __name__ == '__main__':
    main()
