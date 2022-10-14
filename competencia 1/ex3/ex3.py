import pandas as pd
import numpy as np

def ex3_resolucao(df_arquivo: pd.DataFrame):
    df_arquivo['Start Time'] = pd.to_datetime(
        df_arquivo['Start Time'], dayfirst=True
    )
    df_arquivo['End Time'] = pd.to_datetime(df_arquivo['End Time'])

    df_saida = df_arquivo.groupby(
        by=['User Name', df_arquivo['Start Time'].dt.date, 'License Type']

    ).agg(
        min_time=("Start Time", np.min),
        max_time=("End Time", np.max)

    ).reset_index()

    df_saida.rename({
        "Start Time": "Day"
    }, axis=1, inplace=True)

    df_saida['Duration'] = df_saida.apply(
        lambda linha: obtem_diferenca_entre_tempos_em_horas(linha), 
        axis=1
    )

    df_saida = df_saida[['User Name', 'License Type', 'Day', 'Duration']]

    nome_arquivo = "resolucao_ex3"
    df_saida.to_excel(f"{nome_arquivo}.xlsx")
    print(f"O arquivo foi salvo como \"{nome_arquivo}.xlsx\"")


def obtem_diferenca_entre_tempos_em_horas(linha: pd.Series):
    diferenca_tempo = linha['max_time'] - linha['min_time']

    if diferenca_tempo.days > 0:
        return diferenca_tempo

    return str(diferenca_tempo).split(" ")[-1]

def obtem_dia(linha: pd.Series):
    return linha['Start Time'].strftime("%d/%m/%Y")

def main():
    import time
    tempo_inicio = time.time()
    try:
        ex3_resolucao(pd.read_excel("DadosLicencas1.xlsx"))
    
    except RuntimeError as _:
        print("[ERRO] Verifique se o arquivo 'DadosLicencas1.xlsx' existe")
    tempo_fim = time.time()
    print(f"Total de segundos: {tempo_fim - tempo_inicio}")


if __name__ == "__main__":
    main()