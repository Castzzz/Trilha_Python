import os
import json
from datetime import datetime

def gerenciar_gitkeeps(diretorio_raiz = "."):
    #Lista para armazenar os caminhos dos arquivos .gitkeep criados e removidos
    arquivos_criados = []
    arquivos_removidos = []

    #Percorre o diretório raiz e suas subpastas
    for pasta_atual, subpastas, arquivos in os.walk(diretorio_raiz):
        
        #Remove 'logs' e '.git' da lista de subpastas para evitar criar .gitkeep nelas
        if 'logs' in subpastas:
            subpastas.remove('logs')

        if ".git" in subpastas:
            subpastas.remove(".git")
        
        
        caminho_gitkeep = os.path.join(pasta_atual, ".gitkeep")
        tem_gitkeep = '.gitkeep' in arquivos

        #Filtra pra considerar apenas oq não seja .gitkeep
        arquivos_validos = [arq for arq in arquivos if arq != ".gitkeep"]
        #Calcula o total de itens na pasta
        total_itens = len(subpastas) + len(arquivos_validos)

        #Se a pasta estiver vazia e não tiver .gitkeep, cria o arquivo .gitkeep
        if total_itens == 0 and not tem_gitkeep:
            with open(caminho_gitkeep, 'w') as f:
                pass
            arquivos_criados.append(caminho_gitkeep)
        #Se a pasta não tiver vazia e tiver .gitkeep, remove o arquivo .gitkeep
        else:
            if tem_gitkeep:
                os.remove(caminho_gitkeep)
                arquivos_removidos.append(caminho_gitkeep) 

    #Retorna as listas de arquivos criados e removidos
    return arquivos_criados, arquivos_removidos

def registrar_log(criados, removidos, pasta_logs = "logs", arquivo_log = "log.json"):
    #Se a pasta de logs não existir, cria a pasta
    if not os.path.exists(pasta_logs):
        os.makedirs(pasta_logs)

    #Define o caminho completo do arquivo de log
    caminho_log = os.path.join(pasta_logs, arquivo_log)
    #Datetima pra registrar a data e hora do log
    agora = datetime.now().isoformat()

    #Cria um dicionário com as informações do novo registro de log
    novo_registro = {
        'data_hora' : agora,
        'criados' : criados,
        'removidos' : removidos
    }

    historico_logs = []
    #Se o arquivo de log já existir, lê o conteúdo existente e adiciona ao histórico de logs
    if os.path.exists(caminho_log):
        try:
            with open(caminho_log, 'r', encoding = 'utf-8') as f:
                historico_logs = json.load(f)
        except json.JSONDecodeError:
            pass
    
    #Adiciona o novo registro ao histórico de logs
    historico_logs.append(novo_registro)

    with open(caminho_log, 'w', encoding = 'utf-8') as f:
        json.dump(historico_logs, f, ensure_ascii = False, indent = 4)


def main():
    #Gerencia os arquivos .gitkeep e registra o log das operações realizadas
    criados, removidos = gerenciar_gitkeeps()
    registrar_log(criados, removidos)
    #Exibe um resumo de quantos arquivos .gitkeep foram criados e removidos
    print(f"Arquivos .gitkeep criados: {len(criados)}")
    print(f"Arquivos .gitkeep removidos: {len(removidos)}")

if __name__ == "__main__":
    main()