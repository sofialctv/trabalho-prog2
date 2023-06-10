import pickle

# ORDENAÇÃO DOS ALUNOS - Função auxiliar
def compara_Alunos(m1, m2, planilha):

    nome_Aluno1, semestre_Aluno1, notas_Aluno1, faltas_Aluno1 = planilha[m1]
    nome_Aluno2, semestre_Aluno2, notas_Aluno2, faltas_Aluno2 = planilha[m2]

    # Aproveitando o nome da variável, apenas estou dando um novo valor a ela. A partir de agora, a var. deixa de ser uma tupla e passa a ser a soma dos nº que continha.

    # notas_Aluno = (notaP1, notaTrabalho, notaMaratona, bonusExercícios)

    notas_Aluno1 = sum(notas_Aluno1)
    notas_Aluno2 = sum(notas_Aluno2)

    # Calculando os pontos extras das faltas & Garantindo que a nota nunca ultrapassará 100 pontos

    if faltas_Aluno1 == 0 and notas_Aluno1 <= 98: 
        notas_Aluno1 += 2
    elif faltas_Aluno1 == 0 and notas_Aluno1 == 99:
        notas_Aluno1 += 1

    if faltas_Aluno2 == 0 and notas_Aluno2 <= 98: 
        notas_Aluno2 += 2
    elif faltas_Aluno2 == 0 and notas_Aluno2 == 99:
        notas_Aluno2 += 1


# COMPARAR SEMESTRES [...]


# MAIN: Função principal
def main():
    # Utilizando método 'with open' p/ otimizar o código: assim, não precisamos lembrar de fechar o arquivo posteriormente
    
    with open('entrada.bin', 'rb') as arq:      # 'arq' é a variável que será usada p/ se referir ao objeto de arquivo
        planilha = pickle.load(arq)             # Lendo o dicionário do arquivo binário com uma único comando

    matriculas = list(planilha.keys())          # Criando lista apenas com as matrículas dos alunos, que são as chaves do dicionário (planilha)

    # comparaMatricula


if __name__ == '__main__':
    main()