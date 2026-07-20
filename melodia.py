import random
from typing import List

def gerar_melodia(escala_notas: List[str], progressao: List[List[str]], notas_por_compasso: int = 4) -> List[str]:
    """
    Gera uma linha melódica sobre a progressão de acordes.
    Regra: Nos tempos fortes (início de bloco), prioriza notas do acorde atual (target notes).
    Nos tempos fracos, escolhe notas da escala maior.
    """
    melodia = []
    
    for acorde in progressao:
        for i in range(notas_por_compasso):
            if i == 0:
                # Tempo forte: seleciona uma nota que pertence ao acorde atual
                nota = random.choice(acorde)
            else:
                # Tempo fraco: seleciona qualquer nota da escala maior
                nota = random.choice(escala_notas)
            melodia.append(nota)
            
    return melodia