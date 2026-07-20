from typing import List

# Mapeamento simples de notas para facilidade de leitura
NOTAS = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

def gerar_escala_maior(nota_inicial: str) -> List[str]:
    """
    Gera a escala maior a partir de uma nota fundamental aplicando o padrão T-T-ST-T-T-T-ST.
    """
    nota_inicial = nota_inicial.upper()
    idx_inicio = NOTAS.index(nota_inicial)
    
    # Intervalos em semitons: Tom (2), Tom (2), Semitom (1), Tom (2), Tom (2), Tom (2), Semitom (1)
    intervalos = [0, 2, 4, 5, 7, 9, 11]
    
    escala = [NOTAS[(idx_inicio + i) % 12] for i in intervalos]
    return escala
          