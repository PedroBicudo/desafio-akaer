
from typing import List


def ex1_resolucao():
    total_pecas = int(input("Digite o total de pecas (ex: 1): "))
    pecas_recebidas_input = input("Digite as pecas recebidas (ex: 1 2 3 4): ")
    pecas_recebidas = [int(peca) for peca in pecas_recebidas_input.split()]

    print(obtem_peca_faltando(total_pecas, pecas_recebidas))

def obtem_peca_faltando(total_pecas: int, pecas_recebidas: List[int]):
    pecas = {i for i in range(1, total_pecas+1)}
    peca_faltando = pecas.difference(pecas_recebidas)
    return peca_faltando.pop()

def main():
    try:
        ex1_resolucao()
    
    except ValueError as _:
        print("[ERRO] Verifique se as entradas foram informadas corretamente")


if __name__ == "__main__":
    main()