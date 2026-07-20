from typing import List
from acordes import gerar_acorde

def acorde_no_grau(escala_notas: List[str], grau: int, tamanho: int = 4) -> List[str]:
    """
    Gera um acorde a partir de qualquer grau da escala (1 a 7).
    Para Bossa Nova/Lo-Fi alegre, geramos acordes com sétima (tamanho 4: fundamental, 3ª, 5ª, 7ª).
    Usa o operador % para dar a volta na escala sem estourar índice.
    """
    idx_fundamental = grau - 1
    
    # Gera índices empilhando terças: 0, 2, 4, 6...
    indices = [(idx_fundamental + i * 2) % len(escala_notas) for i in range(tamanho)]
    
    return gerar_acorde(escala_notas, indices)

def gerar_progressao(escala_notas: List[str], graus: List[int], tamanho: int = 4) -> List[List[str]]:
    """
    Gera uma sequência de acordes baseada em uma lista de graus (ex: [1, 6, 2, 5] -> I-vi-ii-V).
    """
    return [acorde_no_grau(escala_notas, g, tamanho) for g in graus]