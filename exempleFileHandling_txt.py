#Escrevendo o nome e extensão do arquivo
arquivotxt = 'arquivo.txt'

#Criar arquivo e escrever uma linha
with open(arquivotxt, 'writed') as f:
    f.write('Arquivo criado\n')

#Leitura  de arquivo
f = open(arquivotxt, 'r')
conteudo = f.read()
print(conteudo)

#Leitura de arquivo e escrever uma linha
with open(arquivotxt, 'w') as f:
    f.write('Sobrescrever')


#Leitura de arquivo
print(open(arquivotxt,'r').read())

#Criar arquivo e escrever várias linhas
with open(arquivotxt, 'w') as f:
    f.write('Python 1 \n')
    f.write('Python 2 \n')
    f.write('Python 3 \n')

#Leitura d linhas
lines = []
with open(arquivotxt) as f:
    lines = f.readlines()

count = 0
for line in lines:
    count += 1
    print(f'linha {count} : {lines}')


#Mostra conteudo de linhas
lines

#Leitura com readline com while
with open(arquivotxt) as f:
    while True:
        line = f.readline()
        if not line:
            break
        print(line)

#Leitura com readline com for
with open(arquivotxt) as f:
    for line in f:
        print(line)

#Fechar arquivo para não corromper
f = open(arquivotxt, 'r')
conteudo = f.read()
f.close