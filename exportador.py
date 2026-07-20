from music21 import stream, note, chord, tempo, instrument
from typing import List

def exportar_midi(progressao: List[List[str]], melodia: List[str], nome_arquivo: str = "output.mid", bpm: int = 110) -> None:
    """
    Único ponto de contato com a biblioteca music21.
    Converte as estruturas de dados puras do Python em um Score MIDI com duas pistas (Part):
    1. Melodia (Linha vocal/solo)
    2. Acompanhamento (Acordes)
    """
    score = stream.Score()
    
    # Part 1: Melodia
    p1 = stream.Part()
    p1.insert(0, instrument.AcousticGuitar()) # Violão / Guitarra Bossa
    p1.insert(0, tempo.MetronomeMark(number=bpm))
    
    for n in melodia:
        # Define oitava 4 para a melodia
        m21_note = note.Note(f"{n}4")
        m21_note.quarterLength = 1.0  # Semínima
        p1.append(m21_note)
        
    # Part 2: Acordes
    p2 = stream.Part()
    p2.insert(0, instrument.AcousticGuitar())
    p2.insert(0, tempo.MetronomeMark(number=bpm))
    
    for ac in progressao:
        # Define oitava 3 para a harmonia (fundo)
        notas_com_oitava = [f"{n}3" for n in ac]
        m21_chord = chord.Chord(notas_com_oitava)
        m21_chord.quarterLength = 4.0  # Duram 1 compasso inteiro (4 tempos)
        p2.append(m21_chord)
        
    score.insert(0, p1)
    score.insert(0, p2)
    
    # Exporta para arquivo MIDI
    score.write('midi', fp=nome_arquivo)
    print(f"Sucesso: Arquivo MIDI exportado como '{nome_arquivo}'!")