import pickle

# COMPARAÇÃO DOS ALUNOS
def compara_Alunos(m1, m2, planilha):

    nome_Aluno1, semestre_Aluno1, notas_Aluno1, faltas_Aluno1 = planilha[m1]
    nome_Aluno2, semestre_Aluno2, notas_Aluno2, faltas_Aluno2 = planilha[m2]
        
    ano1 = semestre_Aluno1[0]
    ano2 = semestre_Aluno2[0]

    periodo1 = semestre_Aluno1[1]
    periodo2 = semestre_Aluno2[1]


    notas_Aluno1 = sum(notas_Aluno1)
    notas_Aluno2 = sum(notas_Aluno2)    
    
    # Cálculo dos pontos extras das faltas + Garantindo que a nota nunca ultrapassará 100 pontos

    if faltas_Aluno1 == 0 and notas_Aluno1 <= 98: 
        notas_Aluno1 += 2
    elif faltas_Aluno1 == 0 and notas_Aluno1 == 99:
        notas_Aluno1 += 1

    if faltas_Aluno2 == 0 and notas_Aluno2 <= 98: 
        notas_Aluno2 += 2
    elif faltas_Aluno2 == 0 and notas_Aluno2 == 99:
        notas_Aluno2 += 1

# COMPARAÇÕES - Já escritas seguindo a ordem de desempate

    # Semestres
    if ano1 > ano2: return True
    if ano1 < ano2: return False

    if ano1 == ano2:
        if periodo1 > periodo2: return True
        if periodo1 < periodo2: return False

    # Nota final
    if notas_Aluno1 > notas_Aluno2: return True
    if notas_Aluno1 < notas_Aluno2: return False

    # Nome
    if nome_Aluno1 > nome_Aluno2: return True
    if nome_Aluno1 < nome_Aluno2: return False

    # Matrícula
    if m1 > m2: return True
    if m1 < m2: return False

# MAIN: Função principal - Abrindo o arquivo de entrada
def main():

    lista_Matriculas = []                       # Criando lista apenas com as matrículas dos alunos, que são as chaves do dicionário (planilha)
    
    with open('entrada.bin', 'rb') as arq:      # 'arq' é a variável que será usada p/ se referir ao objeto de arquivo
        planilha = pickle.load(arq)             # Lendo o dicionário do arquivo binário com uma único comando

    for chave in planilha:                      # Lembrando que as chaves do dicionário são as matrículas de cada aluno
        lista_Matriculas.append(chave)

    # ORDENAMatricula



    # Escrevendo o arquivo em formato txt


if __name__ == '__main__':
    main()