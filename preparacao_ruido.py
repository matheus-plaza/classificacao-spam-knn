import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import random

# Fixa a semente para garantir resultados reproduzíveis
random.seed(42)
np.random.seed(42)

# Lê o arquivo original preservando a estrutura
with open('spambase-train.arff', 'r', encoding='utf-8') as f:
    linhas = f.readlines()

# Localiza onde os dados começam
indice_inicio_dados = 0
for i, linha in enumerate(linhas):
    if linha.strip().lower().startswith('@data'):
        indice_inicio_dados = i + 1
        break

# Separa o cabeçalho intacto dos dados
cabecalho = linhas[:indice_inicio_dados]
linhas_dados = [linha.strip().split(',') for linha in linhas[indice_inicio_dados:] if linha.strip()]

# Cria o DataFrame e identifica a coluna da classe (última coluna)
df = pd.DataFrame(linhas_dados)
coluna_classe = df.columns[-1]

# Reduz os dados para 25% mantendo a proporção original de spam e não-spam
df_1_4, _ = train_test_split(df, train_size=0.25, stratify=df[coluna_classe], random_state=42)


# Função para aplicar ruído invertendo as classes
def aplicar_ruido(dataframe, nivel_ruido):
    df_ruidoso = dataframe.copy()

    # Separa os índices por classe
    idx_0 = df_ruidoso[df_ruidoso[coluna_classe] == '0'].index.tolist()
    idx_1 = df_ruidoso[df_ruidoso[coluna_classe] == '1'].index.tolist()

    # Calcula a quantidade de amostras que serão invertidas
    qtd_0 = int(len(idx_0) * nivel_ruido)
    qtd_1 = int(len(idx_1) * nivel_ruido)

    # Sorteia os índices
    inverter_0 = random.sample(idx_0, qtd_0)
    inverter_1 = random.sample(idx_1, qtd_1)

    # Aplica a inversão (0 vira 1, e 1 vira 0)
    df_ruidoso.loc[inverter_0, coluna_classe] = '1'
    df_ruidoso.loc[inverter_1, coluna_classe] = '0'

    return df_ruidoso


# Gera os conjuntos com os níveis de ruído especificados
df_1_4_5 = aplicar_ruido(df_1_4, 0.05)
df_1_4_10 = aplicar_ruido(df_1_4, 0.10)
df_1_4_20 = aplicar_ruido(df_1_4, 0.20)


# Função para salvar os no formato ARFF
def exportar_arff(dataframe, nome_arquivo):
    with open(nome_arquivo, 'w', encoding='utf-8') as f:
        f.writelines(cabecalho)  # Adiciona o cabeçalho original
        for _, row in dataframe.iterrows():
            f.write(','.join(row.astype(str)) + '\n')  # Adiciona os dados


# Salva os quatro arquivos
exportar_arff(df_1_4, 'spambase-train-1-4.arff')
exportar_arff(df_1_4_5, 'spambase-train-1-4-5.arff')
exportar_arff(df_1_4_10, 'spambase-train-1-4-10.arff')
exportar_arff(df_1_4_20, 'spambase-train-1-4-20.arff')

print("Processo concluído com sucesso!")
print("Foram gerados 4 arquivos ARFF perfeitamente compatíveis.")