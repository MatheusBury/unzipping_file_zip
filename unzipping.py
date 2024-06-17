
import os
import shutil

path_name = r'G:\Drives compartilhados\OPERATION PHOTOS\Modec\2024\Photos_onboarding_2024\INSP_files\Project_C'
file_name = os.listdir(path_name)
output = r'G:\Drives compartilhados\OPERATION PHOTOS\Modec\2024\Photos_onboarding_2024\360_resolucao_original\Project_C'


def descompactar(arquivo, pasta_destino):
   
    arquivo_completo = os.path.join(path_name, arquivo)

    if arquivo.endswith('.zip'):
        try:
            shutil.unpack_archive(arquivo_completo, pasta_destino)
            print(f'Arquivo {arquivo} descompactado com sucesso!')
        except Exception as e:
            print(f'Erro ao descompactar o arquivo {arquivo}: {e}')
            pass  # Continue with the next file
        
for folder in os.listdir(path_name):
    print(f'Processing folder: {folder}')
    
    if folder != 'PW_zipado': #aqui vc pode escolher uma pasta especifica

        full_path_folder = os.path.join(path_name, folder)
        list_full_path_folder = os.listdir(full_path_folder)

        for file in list_full_path_folder:
            file_path = os.path.join(full_path_folder,file)

            if os.path.isfile(file_path):
                descompactar(file_path, output)
            else:
                print(f'{file} is not a file.')
        else:
            print(f'Skipping file: {file}')


print(f'Total Folders : {len(folder)}')