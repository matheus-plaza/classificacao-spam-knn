import pandas as pd
from sklearn.model_selection import train_test_split


def tratar_dados():
    print("Iniciando o processamento")

    # Carregar os dados originais
    # Como o spambase.data não tem cabeçalho, usamos header=None
    try:
        df = pd.read_csv('spambase.data', header=None)
        print(f"Dados carregados com sucesso! Total de instâncias: {len(df)}")
    except FileNotFoundError:
        print("Erro: O arquivo 'spambase.data' não foi encontrado no diretório atual.")
        return

    # A última coluna (índice 57) é a classe (0 para não-spam, 1 para spam)
    coluna_classe = 57

    # Separação dos Conjuntos (70% Treino / 30% Teste) mantendo a proporção (stratify)
    df_train, df_test = train_test_split(
        df,
        test_size=0.30,
        stratify=df[coluna_classe],
        random_state=42  # Mantém a reprodutibilidade do sorteio
    )

    print(f"Divisão concluída:")
    print(f" - Treinamento: {len(df_train)} instâncias.")
    print(f" - Teste: {len(df_test)} instâncias.")

    # Função para gerar o arquivo .arff com o cabeçalho exigido pelo WEKA
    def exportar_para_arff(dataframe, nome_arquivo):
        with open(nome_arquivo, 'w') as f:
            # Cabeçalho ARFF
            f.write("@relation spambase\n\n")

            # Escrevendo os 57 atributos numéricos
            for i in range(57):
                f.write(f"@attribute atributo_{i + 1} numeric\n")

            # Escrevendo o atributo nominal da classe
            f.write("@attribute class {0,1}\n\n")
            f.write("@data\n")

            # Escrevendo os dados separados por vírgula
            dataframe.to_csv(f, header=False, index=False)
        print(f"Arquivo '{nome_arquivo}' gerado com sucesso!")

    # Geração dos Entregáveis
    exportar_para_arff(df_train, 'spambase-train.arff')
    exportar_para_arff(df_test, 'spambase-test.arff')

    print("\nOs arquivos estão prontos para o WEKA.")


if __name__ == "__main__":
    tratar_dados()