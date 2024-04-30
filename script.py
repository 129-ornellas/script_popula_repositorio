import os
import csv
import shutil
import re

csv.field_size_limit(2147483647)


def substituir_caracteres_especiais(caminho): 
    return re.sub(r'[<>:"/\\|?*]', '_', caminho).strip()

raiz = os.chdir('.')
csv_files = os.listdir(raiz)
for csv_file in csv_files:
    if csv_file == 'script.py' or csv_file == '.git' or csv_file == 'NOVA_QUERY.sql' or len(csv_file) <= 40:
        continue
    elif 40 < len(csv_file) < 43:
        os.rename(csv_file, csv_file[0:30] + '.csv')
        continue
    os.rename(csv_file, csv_file[0:40] + '.csv' )

# arquivo.csv

csv_files_formatados = os.listdir(raiz)

for arquivo_csv in csv_files_formatados:
    if arquivo_csv == 'script.py' or arquivo_csv == '.git' or arquivo_csv == 'NOVA_QUERY.sql':
        continue

    arquivo_csv = substituir_caracteres_especiais(arquivo_csv)
    novo_path = arquivo_csv.replace('.csv', '')

    if( not os.path.exists(novo_path)):        
        novo_path = substituir_caracteres_especiais(novo_path)
        os.mkdir(novo_path)
        shutil.copy(arquivo_csv, novo_path)
        os.chdir(novo_path)

    with open(arquivo_csv, "r", encoding="utf8") as arquivo:

        arquivo_csv = csv.reader(arquivo, delimiter=",")

        def criar_pasta_navegar(nome):
            os.mkdir(nome)
            os.chdir(nome)

        for i, linha in enumerate(arquivo_csv):
            if i == 0:
                continue

            agrupamento = substituir_caracteres_especiais(f"{linha[0]}")

            if not os.path.exists(agrupamento):
                criar_pasta_navegar(agrupamento)
            else:
                os.chdir(agrupamento)
            
            relatorio = substituir_caracteres_especiais(f"{linha[1]}")
            
            if(not os.path.exists(relatorio)):
                criar_pasta_navegar(relatorio)
            
            escrever = "w"

            titulos = ['Relatorio.php', 'Relatorio.view.php', 'index.php', 'ds_filtro.json', 'opcao_tipo_impressao.sql', 'insert_statement.sql', 'opcoes_impressao.sql', 'me_config.json']

            def cria_documento(titulo, escrever, texto):
                with open(titulo, escrever, encoding='utf-8') as documento:
                    documento.write(texto)
                    documento.close()
                
            indices_desconsiderados = [0, 1, 6, 11, 12, 13, 14, 15]
            for index, coluna in enumerate(linha):
                if index not in indices_desconsiderados:
                    if coluna == '':
                        continue
                    cria_documento(titulos[0], escrever, coluna)
                    titulos.remove(titulos[0])
                else:
                    continue
            os.chdir('../..')
    os.chdir('..')