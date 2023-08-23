import os
import csv
import shutil

raiz = os.chdir('.')
lista_raiz = os.listdir(raiz)
for tabela in lista_raiz:
    if tabela == 'script.py':
        continue
    
    # verifica se a pasta já existe, se nao existir cria uma pasta e acessa ela
    novo_path = f"custom_{tabela}"
    if(not os.path.exists(f"custom_{tabela}")):
        os.mkdir(f"custom_{tabela}")
        shutil.copy(tabela, novo_path)
        os.chdir(novo_path)

    # le o csv que foi copiado para a pasta e cria os diretórios com os arquivos.php de acordo com os campos do csv
    arquivo_csv = tabela
    with open(arquivo_csv, "r") as arquivo:
        arquivo_csv = csv.reader(arquivo, delimiter=";")
        for i,linha in enumerate(arquivo_csv):
            if i == 0:
                continue

            relatorio = linha[1]
            if(not os.path.exists(relatorio)):
                os.mkdir(relatorio)

            os.chdir(relatorio)

            texto_index = linha[4]
            cria_index = open('Relatorio.index.php', 'w')
            cria_index.write(texto_index)
            cria_index.close()

            texto_config = linha[3]
            cria_config_php = open('Relatorio.php', 'w')
            cria_config_php.write(texto_config)
            cria_config_php.close()

            texto_view = linha[0]
            cria_view_php = open('Relatorio.view.php', 'w')
            cria_view_php.write(texto_view)
            cria_view_php.close()

            os.chdir('..')
        os.chdir('..')
