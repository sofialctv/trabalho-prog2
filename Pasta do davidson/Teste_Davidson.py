#Algoritmo de ordenacao mergesort
def mSort(l,dic):
	if len(l) > 1:
		meio = len(l) // 2
		lEsq = l[:meio]
		lDir = l[meio:]
		
		mSort(lEsq,dic)
		mSort(lEsq,dic)
		
		return merge(l, dic, lEsq, lDir)
		
def merge(l, dic, lEsq, lDir,):
  #Declaracao de var.
  i = 0
  j = 0
  k = 0

  while i < len(lEsq) and j < len(lDir):
		
    ntfinal_aluno1 = 0
    ntfinal_aluno2 = 0

    m1 = lEsq[i]
    m2 = lDir[j]
		
    nome1, semestre1, notas1, faltas1 = dic[m1]
    nome2, semestre2, notas2, faltas2 = dic[m2]

    #Calculos da nota final do aluno 1
    ntfinal_aluno1 += notas1[0] + notas1[1] + notas1[2] + notas1[3]

    if faltas1 == 0:
        ntfinal_aluno1 += 2

    if ntfinal_aluno1 > 100:
        ntfinal_aluno1 = 100

    #Calculos da nota final do aluno 2
    ntfinal_aluno2 += notas2[0] + notas2[1] + notas2[2] + notas2[3]

    if faltas2 == 0:
        ntfinal_aluno2 += 2

    if ntfinal_aluno2 > 100:
        ntfinal_aluno2 = 100 

    #Teste do ano
    if semestre1[0] < semestre2[0]:
          l[k] = lEsq[i]
          i += 1

    elif semestre1[0] > semestre2[0]:
          l[k] = lDir[j]
          j += 1

    #Se o ano for igual, ele testara o período em que o aluno ingressou.
    elif semestre1[1] < semestre2[1]:
          l[k] = lEsq[i]
          i += 1

    elif semestre1[1] > semestre2[1]:
          l[k] = lDir[j]
          j += 1

    #Se o ano e período de ingresso forem iguais, ele testara a nota final do aluno.
    else:
      if ntfinal_aluno1 < ntfinal_aluno2:
        l[k] = lEsq[i]
        i += 1

      elif ntfinal_aluno1 > ntfinal_aluno2:
        l[k] = lDir[j]
        j += 1

      #Caso as notas sejam iguais, ele testara o pelo nome.
      else:
        if nome1 < nome2:
          l[k] = lEsq[i]
          i += 1

        elif nome1 > nome2:
          l[k] = lDir[j]
          j += 1

        #Caso haja empate em todos os testes, ele testara a matricula.
        else:
          if m1 < m2:
            l[k] = lEsq[i]
            i += 1

          elif m1 > m2:
            l[k] = lDir[j]
            j += 1
    k += 1

  while i < len(lEsq):
    l[k] = lEsq[i]
    i += 1			

  while j < len(lDir):
    l[k] = lDir[j]
    j += 1
    k += 1

		

import pickle
def main():

  #arquiv = input('Escreva o diretório do arquivo:')
  arquiv = 'C:\\Users\\Davidson\\Desktop\\Coisas aleatorias\\Programas Py\\trabalho-prog2\\entradas\\entrada10.bin'
  matriculas = []
  with open(arquiv,'rb') as file:
      
      dic = pickle.load(file)

      for matricula in dic:
          matriculas.append(matricula)

      for i in range (len(matriculas)):
        print(matriculas[i], dic[matriculas[i]][1])
      print('----------------------------')
      mSort(matriculas,dic)
      for i in range (len(matriculas)):
        print(matriculas[i], dic[matriculas[i]][1])

if __name__ == '__main__':
   main()