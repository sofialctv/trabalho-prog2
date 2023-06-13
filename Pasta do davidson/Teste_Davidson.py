import pickle
def main():

  arquiv = input('Escreva o diretório do arquivo:')

  with open(arquiv,'rb') as file:
      
      l = pickle.load(file)

      for matricula in l:
          nome, semestre, notas, faltas = l[matricula]
          print(f'{semestre}, {matricula}, {nome},[{notas} {faltas}] ')

if __name__ == '__main__':
   main()