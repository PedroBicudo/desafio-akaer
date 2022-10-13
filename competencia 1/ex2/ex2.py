
from collections import namedtuple
from typing import List

Bota = namedtuple("Bota", ["numero", "lado"])

def ex2_resolucao():
    total_botas = int(input("Digite o total de botas: "))
    if total_botas % 2 != 0:
        raise ValueError("O total de botas deve ser par")
    
    botas = []
    for _ in range(total_botas):
        numero, lado = input("Digite o tamanho e pé da bota atual (ex: 40 D): ").split()
        botas.append(Bota(int(numero), lado))
    
    print(obtem_total_de_pares_corretos(botas))

def obtem_total_de_pares_corretos(botas: List[Bota]) -> int:
    par_esquerdo_freq_num = dict()
    par_direito_freq_num = dict()

    for bota in botas:
        if bota.lado == 'E':            
            par_esquerdo_freq_num.setdefault(bota.numero, 0)
            par_esquerdo_freq_num[bota.numero] += 1
        
        elif bota.lado == 'D':
            par_direito_freq_num.setdefault(bota.numero, 0)
            par_direito_freq_num[bota.numero] += 1   

    total_pares = 0
    for numero in par_esquerdo_freq_num:
        if numero in par_direito_freq_num:
            total_pares += min(par_direito_freq_num[numero], par_esquerdo_freq_num[numero])

    return total_pares


def main():
    try:
        ex2_resolucao()
    
    except ValueError as _:
        print("[ERRO] Verifique se as entradas foram informadas corretamente")


if __name__ == "__main__":
    main()