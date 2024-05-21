
import os
import shutil

path_name = r'G:\Drives compartilhados\Corrosion Segmentation Data\project_modec\MV30\EQUIP_AI_DELIVERY_05172024\3d_mask'
file_name = os.listdir(path_name)
Output = r'C:\Users\Operacao\Pictures\MV30 3D MASK'


def descompactar(arquivo, pasta_destino):
   
    arquivo_completo = os.path.join(path_name, arquivo)

    if arquivo.endswith('.zip'):
        try:
            shutil.unpack_archive(arquivo_completo, pasta_destino)
            print(f'Arquivo {arquivo} descompactado com sucesso!')
        except Exception as e:
            print(f'Erro ao descompactar o arquivo {arquivo}: {e}')
            pass  # Continue with the next file
        
for arquivo in os.listdir(path_name):
    
    if os.path.isfile(os.path.join(path_name, arquivo)):
        descompactar(arquivo, Output)
