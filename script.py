import os
import csv
import shutil

raiz = os.chdir('.')
lista_raiz = os.listdir(raiz)
for tabela in lista_raiz:
    if tabela == 'script.py' or tabela == '.git' or tabela == 'NOVA_QUERY.sql':
        continue
    
        

    # verifica se a pasta já existe, se nao existir cria uma pasta e acessa ela
    novo_path = tabela.replace('.csv', '')
    if( not os.path.exists(novo_path)):
        os.mkdir(novo_path)
        shutil.copy(tabela, novo_path)
        os.chdir(novo_path)

    # le o csv que foi copiado para a pasta e cria os diretórios com os arquivos.php de acordo com os campos do csv
    arquivo_csv = tabela
    with open(arquivo_csv, "r", encoding="utf8") as arquivo:
        arquivo_csv = csv.reader(arquivo, delimiter=",")
        def criar_pasta_navegar(nome):
            os.mkdir(nome)
            os.chdir(nome)

        for i, linha in enumerate(arquivo_csv):
            if i == 0:
                continue

            agrupamento = f"{linha[0]}"

            if(not os.path.exists(agrupamento)):
                criar_pasta_navegar(agrupamento)
            
            relatorio = f"{linha[1]}"
            relatorio_formatado = "" .join(filter(str.isalnum, relatorio))



            # relatorio = f"{[0]} - {[1]}
            # relatorio_formatado = "" .join(filter(str.isalnum, relatorio))
            
            if(not os.path.exists(relatorio)):
                criar_pasta_navegar(relatorio_formatado)
            
            # cria paste e acessa


            escrever = "w"

            def cria_documento(titulo, escrever, texto):
                documento = open(titulo, escrever)
                documento.write(texto)
                documento.close()
                
            texto_config = linha[2]
            # depois, alterar o alias das colunas na query para gerar uma lista e nomear os arquivos de acordo com os itens na lista, dessa forma
            # é possível fazer apenas um for chamando a função e essa lista para nomear os itens.

            cria_documento("Relatorio.php",escrever , texto_config)
            break
            
            texto_view = linha[3]
            texto_index = linha[4]
            texto_filtro = linha[5]
            
            cria_config_php = open("Relatorio.php", 'w')
            cria_config_php.write(texto_config)
            cria_config_php.close()

            cria_view_php = open('Relatorio.view.php', 'w')
            cria_view_php.write(texto_view)
            cria_view_php.close()

            cria_view_php = open('Relatorio.view.php', 'w')
            cria_view_php.write(texto_index)
            cria_view_php.close()

            cria_view_php = open('Relatorio.view.php', 'w')
            cria_view_php.write(texto_view)
            cria_view_php.close()

            os.chdir('..')
    os.remove(tabela)
    os.chdir('..')
    break
