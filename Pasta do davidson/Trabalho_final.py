#Funcao de comparacao.
def comparacao(m1,m2,dic):

  nome1, semestre1, notas1, faltas1 = dic[m1]
  nome2, semestre2, notas2, faltas2 = dic[m2]

  ntfinal_aluno1 = 0
  ntfinal_aluno2 = 0

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
    return True

  elif semestre1[0] > semestre2[0]:
    return False
    #Se o ano for igual, ele testara o período em que o aluno ingressou.
  elif semestre1[1] < semestre2[1]:
    return True

  elif semestre1[1] > semestre2[1]:
    return False

    #Se o ano e período de ingresso forem iguais, ele testara a nota final do aluno.
  else:
      if ntfinal_aluno1 < ntfinal_aluno2:
        return True

      elif ntfinal_aluno1 > ntfinal_aluno2:
        return False

      #Caso as notas sejam iguais, ele testara o pelo nome.
      else:
        if nome1 > nome2:
          return True

        elif nome1 < nome2:
          return False

        #Caso haja empate em todos os testes, ele testara a matricula.
        else:
          if m1 > m2:
              return True

          elif m1 < m2:
            return False



#Algoritmo de ordenacao mergesort
def mSort(l,dic):
	if len(l) > 1:
		meio = len(l) // 2
		lEsq = l[:meio]
		lDir = l[meio:]
		
		mSort(lEsq,dic)
		mSort(lDir,dic)
		
		merge(l,dic, lEsq, lDir)
                
		
def merge(l, dic, lEsq, lDir,):
  #Declaracao de var.
  i = 0
  j = 0
  k = 0

  while i < len(lEsq) and j < len(lDir):

    #m1 = lEsq[i] | m2 = lDir[j]
    if comparacao(lEsq[i],lDir[j],dic): 
      l[k] = lEsq[i]
      i += 1

    else:
      l[k] = lDir[j]
      j += 1
      
    k += 1

  while i < len(lEsq):
    l[k] = lEsq[i]
    i += 1
    k += 1

  while j < len(lDir):
    l[k] = lDir[j]
    j += 1
    k += 1

		

import pickle
def main():

  arquiv = input('Escreva o diretório do arquivo:')
  
  matriculas = []
  with open(arquiv,'rb') as file:
      
      dic = pickle.load(file)

      for matricula in dic:
          matriculas.append(matricula)
      
  mSort(matriculas, dic)

  f = open('saida.txt', 'w', encoding=' utf8')
  for matricula in range(len(matriculas)-1,-1,-1):

    msg = ''
    nota_final = 0
    soma_notas = 0

    _, _, notas, faltas = dic[matriculas[matricula]]

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

    f.write(f'{dic[matriculas[matricula]][1][0]}/{dic[matriculas[matricula]][1][1]} {matriculas[matricula]} {dic[matriculas[matricula]][0]} - {nota_final} ({msg} = {soma_notas})\n')
  f.close()
  

if __name__ == '__main__':
   main()