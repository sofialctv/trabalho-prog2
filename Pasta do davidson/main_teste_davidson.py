
import pickle
# MAIN: Função principal
def main():
    ListaMatriculas = []

def main():
    ListaMatriculas = []

    arquiv = input('Escreva o diretório do arquivo:')

    with open(arquiv,'rb') as file:
      
        panilha = pickle.load(file)

        for matricula in panilha:
              ListaMatriculas.append(matricula)             

        for elem in ListaMatriculas:
            print(elem, panilha[elem][0], panilha[elem][1], panilha[elem][2], panilha[elem][3])

            

        

    # comparaMatricula


if __name__ == '__main__':
    main()