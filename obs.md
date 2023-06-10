# 📝 Anotações
Esse documento contém os apontamentos do grupo em relação ao trabalho, o qual utilizaremos como guia ao longo da execução da tarefa.

## Dados
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

## Nota Final
A nota final (nF) é calculada por:
$$
nF = nota1 (Prova1) + nota2 (Trabalho) + nota3 (Maratona) + bonusExercícios
$$

* **A notaFinal não pode ultrapassar 100 pts!**
    ```python
    if notaFinal > 100: 
        notaFinal == 100
    ```

### *Sugestão:* faça uam estrutura de IF & ELSE que impeça que a nota seja maior que 100, utilize AND. Isso irá economizar linhas.

<br>

### Bônus é calculado por:
Bônus          | Pontos  | Como deve aparecer no código
---------      | ------  | --------------------- 
bonusExercícios|    1    |  3E
bonusPresença  |    2    |  2P

* bonusTrabalho é acresido **diretamente** na nota2
* bonusPresença é sempre 0 ou 2

```python
if numFaltas == 0: 
    notaFinal += bonusPresença
```

# 🎯 Principal Objetivo do Trabalho

* Criar lista contendo APENAS os nº de matrícula dos alunos

## Critérios de ordenação da lista

1. Semestre (do mais recente para o mais antigo)
2. Em caso de empate, pela nota final (da maior para a menor)
3. Em caso de novo empate, em ordem alfabética do nome
4. Caso ainda haja empate, em ordem crescente de matrícula

* **Os caracteres são ordenados de acordo com suas posições na tabela UTF-8**

## Comparando Matrículas
O método de ordenação deve utilizar uma única função de comparação que **recebe duas matrículas m1 e m2**, além do dicionário de alunos, e retorna:

* TRUE, caso matrícula 1 (m1) apareça ANTES da matrícula 2 (m2)
* FALSE, caso contrário