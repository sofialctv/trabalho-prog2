# OBSERVAÇÕES
Documento contendo todos os apontamentos do grupo em relação ao trabalho. Utilizaremos para nos guiarmos ao longo da execução da tarefa.

# DADOS
* Se apresentam em forma de **DICIONÁRIO**
* É *obrigatória* leitura dos dados de entrada pela biblioteca ```pickle```

## Estrutura do Dicionário
* CHAVE: matrícula do aluno - num int

VALOR          | Estrutura | Exemplo
---------------| --------- | --------------------- 
Nome           | Tupla     | ("Martim Carvalho")
Semestre Letivo| Tupla     | (ano, perído)
Notas do aluno | Tupla     | (n1, n2, n3, bonusTotal)
Num de faltas  | int       | (35)


*Exemplo:*
```python

prog2 = {'123': (("Larissa"), (2023, 1), (30, 42, 10, 1), 8), "234" : (("Caio"), (2022, 2), (21, 2, 8, 0), 35)}
```

## NOTA FINAL
notaFinal = nota1 (Prova1) + nota2 (Trabalho) + nota3 (Maratona) + bonusExercícios

* **A notaFinal não pode ultrapassar 100 pts!**
```python

if notaFinal > 100: 
    notalFinal == 100
print notaFinal
```

### Bônus é calculado por:
Bônus          | Pontos  | Como deve aparecer no código
---------      | ------  | --------------------- 
bonusExercícios|    1    |  3E
bonusPresença  |    2    |  2P

* bonusTrabalho é acresido diretamente na nota2

# PRINCIPAL OBJETIVO

* Criar lista contendo APENAS os nº de matrícula dos alunos

## Critérios de ordenação da lista
    1. 