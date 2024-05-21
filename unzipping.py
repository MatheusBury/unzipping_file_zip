
import os
import shutil

path_name = 'Pasta para descompactar'
file_name = os.listdir(path_name)
Output = f'{path_name}'


def descompactar(arquivo, pasta_destino):
   
    arquivo_completo = os.path.join(path_name, arquivo)

    if arquivo.endswith('.zip'):
   
        shutil.unpack_archive(arquivo_completo, pasta_destino)
        print(f'Arquivo {arquivo} descompactado com sucesso!')

for arquivo in os.listdir(path_name):
    
    if os.path.isfile(os.path.join(path_name, arquivo)):
        descompactar(arquivo, Output)
