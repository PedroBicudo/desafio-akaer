import numpy as np
import pandas as pd


def ex4_resolucao(df_banco: pd.DataFrame, df_licencas_esp: pd.DataFrame):
    df_licencas_esp.loc[
        df_licencas_esp['Start Time'].isin(df_banco['Start Time']) &
        df_licencas_esp['End Time'].isin(df_banco['End Time']),
        ['User Name']
    
    ] = df_banco.loc[
            df_banco['Start Time'].isin(df_licencas_esp['Start Time']) &
            df_banco['End Time'].isin(df_licencas_esp['End Time']),
            ['User Name']
    ].values

    nome_arquivo = "resolucao_ex4"
    df_licencas_esp.to_excel(f"{nome_arquivo}.xlsx")
    print(f"O arquivo foi salvo como \"{nome_arquivo}.xlsx\"")


def main():
    import time
    tempo_inicio = time.time()
    try:
        ex4_resolucao(
            pd.read_excel("DadosLicencas1.xlsx"),
            pd.read_excel("DadosLicencas2.xlsx")
        )
    
    except RuntimeError as _:
        print("[ERRO] Verifique se os arquivos 'DadosLicencas1.xlsx' ou 'DadosLicencas2.xlsx' existe")
    tempo_fim = time.time()
    print(f"Total de segundos: {tempo_fim - tempo_inicio}")


if __name__ == "__main__":
    main()
