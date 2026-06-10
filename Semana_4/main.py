import os
import json
from datetime import datetime

def gerenciar_gitkeeps(diretorio_raiz = "."):
    arquivos_criados = []
    arquivos_removidos = []

    for pasta_atual, subpastas, arquivos in os.walk(diretorio_raiz):

        if 'logs' in subpastas:
            subpastas.remove('logs')

        if ".git" in subpastas:
            subpastas.remove(".git")
        
        caminho_gitkeep = os.path.join(pasta_atual, ".gitkeep")
        tem_gitkeep = '.gitkeep' in arquivos

        arquivos_validos = [arq for arq in arquivos if arq != ".gitkeep"]
        total_itens = len(subpastas) + len(arquivos_validos)

        if total_itens == 0 and not tem_gitkeep:
            with open(caminho_gitkeep, 'w') as f:
                pass
            arquivos_criados.append(caminho_gitkeep)
        else:
            if tem_gitkeep:
                os.remove(caminho_gitkeep)
                arquivos_removidos.append(caminho_gitkeep) 

    return arquivos_criados, arquivos_removidos

def registrar_log(criados, removidos, pasta_logs = "logs", arquivo_log = "log.json"):
    if not os.path.exists(pasta_logs):
        os.makedirs(pasta_logs)

    caminho_log = os.path.join(pasta_logs, arquivo_log)
    agora = datetime.now().isoformat()

    novo_registro = {
        'data_hora' : agora,
        'criados' : criados,
        'removidos' : removidos
    }

    historico_logs = []
    if os.path.exists(caminho_log):
        try:
            with open(caminho_log, 'r', encoding = 'utf-8') as f:
                historico_logs = json.load(f)
        except json.JSONDecodeError:
            pass

    historico_logs.append(novo_registro)

    with open(caminho_log, 'w', encoding = 'utf-8') as f:
        json.dump(historico_logs, f, ensure_ascii = False, indent = 4)

def main():
    criados, removidos = gerenciar_gitkeeps()
    registrar_log(criados, removidos)
    print(f"Arquivos .gitkeep criados: {len(criados)}")
    print(f"Arquivos .gitkeep removidos: {len(removidos)}")

if __name__ == "__main__":
    main()