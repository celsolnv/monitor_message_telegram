def inverter_linhas_log(caminho_arquivo):
    # Lê o arquivo e armazena todas as linhas em uma lista
    with open(caminho_arquivo, "r") as arquivo:
        linhas = arquivo.readlines()

    # Inverte a ordem das linhas
    linhas_invertidas = linhas[::-1]

    # Escreve as linhas invertidas em um novo arquivo ou sobrescreve o original
    with open(caminho_arquivo, "w") as arquivo:
        arquivo.writelines(linhas_invertidas)
