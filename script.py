import os
import csv
import shutil
import re

raiz = os.chdir('.')
lista_raiz = os.listdir(raiz)
for tabela in lista_raiz:
    if tabela == 'script.py' or tabela == '.git' or tabela == 'NOVA_QUERY.sql':
        continue
    novo_path = tabela.replace('.csv', '')
    if( not os.path.exists(novo_path)):
        os.mkdir(novo_path)
        shutil.copy(tabela, novo_path)
        os.chdir(novo_path)

    arquivo_csv = tabela
    with open(arquivo_csv, "r", encoding="utf8") as arquivo:
        arquivo_csv = csv.reader(arquivo, delimiter=",")

        def substituir_caracteres_especiais(caminho):
            return re.sub(r'[<>:"/\\|?*]', '_', caminho).strip()

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
            # relatorio_formatado = "" .join(filter(str.isalnum, relatorio))
            
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
