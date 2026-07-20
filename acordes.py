from typing import List

def gerar_acorde(escala_notas: List[str], indices: List[int]) -> List[str]:
    """
    Extrai notas específicas da escala por índice (empilhamento de terças).
    """
    return [escala_notas[idx % len(escala_notas)] for idx in indices]