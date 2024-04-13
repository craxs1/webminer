import os
import webbrowser

def open_html_file():
    # Obter o diretório atual
    current_directory = os.getcwd()
    
    # Definir o nome do arquivo HTML como index.html
    html_file_name = 'index.html'
    
    # Construir o caminho completo para o arquivo HTML na mesma pasta que o script
    html_file_path = os.path.join(current_directory, html_file_name)
    
    # Verificar se o arquivo HTML existe
    if os.path.exists(html_file_path):
        # Abrir o arquivo HTML no navegador padrão
        webbrowser.open('file://' + html_file_path)
    else:
        print("O arquivo HTML não foi encontrado.")

# Abrir o arquivo HTML
open_html_file()
