# unzipping_file_zip


Este projeto contém um script Python que descompacta arquivos `.zip` em um diretório específico. Ele percorre uma pasta específica, verifica se os arquivos são arquivos `.zip` e os descompacta no mesmo local ou em um local especificado.

## Requisitos

- Python 3.x
- Biblioteca `shutil` (parte da biblioteca padrão do Python)
- Biblioteca `os` (parte da biblioteca padrão do Python)

## Como Usar

1. Clone o repositório para sua máquina local:
    ```sh
    git clone https://github.com/seu-usuario/descompactador-de-arquivos.git
    ```

2. Navegue até o diretório do projeto:
    ```sh
    cd unzipping_file_zip
    ```

3. Certifique-se de que você tem uma pasta chamada `Pasta para descompactar` no mesmo diretório que o script Python. Coloque seus arquivos `.zip` nesta pasta.

4. Execute o script:
    ```sh
    python descompactador.py
    ```

## Estrutura do Projeto
descompactador-de-arquivos/
│
├── Pasta para descompactar/ # Coloque seus arquivos .zip aqui
│ ├── arquivo1.zip
│ ├── arquivo2.zip
│ └── ...
│
├── descompactador.py # Script Python para descompactar arquivos
└── README.md # Este arquivo

