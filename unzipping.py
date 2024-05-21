
import os
import shutil

path_name = r'G:\Drives compartilhados\Corrosion Segmentation Data\project_modec\MV30\EQUIP_AI_DELIVERY_05172024\alt_predictions'
file_name = os.listdir(path_name)
Output = r'C:\Users\Operacao\Pictures\MV30 MASK'


def descompactar(arquivo, pasta_destino):
   
    arquivo_completo = os.path.join(path_name, arquivo)

    if arquivo.endswith('.zip'):
   
        shutil.unpack_archive(arquivo_completo, pasta_destino)
        print(f'Arquivo {arquivo} descompactado com sucesso!')

for arquivo in os.listdir(path_name):
    
    if os.path.isfile(os.path.join(path_name, arquivo)):
        descompactar(arquivo, Output)
