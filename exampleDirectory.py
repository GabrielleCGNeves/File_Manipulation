import os
import shutil
import glob

# Declaração das variáveis
directory = 'Senai'
parent_dir = 'C:\\Users\\Aluno\\Documents\\' # Pode ser usado caminho relativo: "./"
path = os.path.join(parent_dir, directory)

# Criação do diretório
# os.makedirs(path) pra linux
os.mkdir(path)
print("Diretório '% s' foi criado" % directory)

# Tratativa de erro 1
try:
    os.makedirs(path, exist_ok = True)
    print("Diretório '%s' criado com successo" % directory)
except OSError as error:
    print("Diretório '%s' não foi criado" % directory)

# Tratativa de erro 2
caminho = 'C:\\Users\\Aluno\\Documents\\Senai\\'

if os.path.exists(caminho):
    print('O diretório existe')
else:
    print('O diretório não existe')

# Renomear caminho do diretório
caminho_antigo = 'C:\\Users\\Aluno\\Documents\\Senai\\'
caminho_novo = 'C:\\Users\\Aluno\\Documents\\Python\\'
os.rename(caminho_antigo, caminho_novo)

# Procurar arquivo  --------- TESTAR
arquivos_txt = glob.glob("*.txt")
print(f"Arquivos txt: {arquivos_txt}")

# Mover arquivo
diretorio_origem = "C:\\Users\\Aluno\\Documents\\Python\\"
diretorio_destino = "C:\\Users\\Aluno\\Documents\\"

for doc in os.listdir(diretorio_origem):
    diretorio_origem = os.path.join(diretorio_origem, doc)
    diretorio_destino = os.path.join(diretorio_destino, doc)
    shutil.move(diretorio_origem, diretorio_destino)
    print("Arquivo movido com sucesso.")

# Copiar arquivo
for doc in os.listdir(diretorio_origem):
    diretorio_origem = os.path.join(diretorio_origem, doc)
    diretorio_destino = os.path.join(diretorio_destino, doc)
    shutil.copy(diretorio_origem, diretorio_destino)
    print("Arquivo copiado com sucesso.")

# Renomear arquivo
prefixo = "novo_"

for doc in os.listdir(diretorio_origem):
    novo_nome = prefixo + doc
    os.rename(os.path.join(diretorio_origem, doc), os.path.join(diretorio_origem, novo_nome))
    print("Arquivo renomeado com sucesso.")

# Excluir arquivo
extensao = ".txt"

for novo_doc in os.listdir(diretorio_origem):
    if novo_doc.endswith(extensao):
        os.remove(os.path.join(diretorio_origem, novo_doc))
        print("Arquivo deletado com sucesso")