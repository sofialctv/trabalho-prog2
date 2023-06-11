import pickle
with open('entrada10.bin','rb') as file:
    l = pickle.load(file)
    for matricula in l:
      l[matricula] = nome, semestre, notas, faltas

      print(f'{semestre}, {matricula}, {nome},[{notas} {faltas}] ')