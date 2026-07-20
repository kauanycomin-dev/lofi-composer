from escala import gerar_escala_maior
from progressao import gerar_progressao
from melodia import gerar_melodia
from exportador import exportar_midi
from persistencia import Composicao, salvar_composicao

def main():
    # 1. Configurações da Composição
    tom = "C"
    graus = [1, 6, 2, 5]  # Progressão I-vi-ii-V clássica da Bossa Nova
    bpm = 110

    print(f"--- Gerando composição no tom de {tom} maior ---")
    
    # 2. Lógica Teórica em Python puro
    escala = gerar_escala_maior(tom)
    print(f"Escala Maior ({tom}): {escala}")
    
    progressao = gerar_progressao(escala, graus, tamanho=4)
    print("\nProgressão de Acordes (com 7ª):")
    for g, ac in zip(graus, progressao):
        print(f" Grau {g}: {ac}")
        
    melodia = gerar_melodia(escala, progressao, notas_por_compasso=4)
    print(f"\nMelodia Gerada ({len(melodia)} notas): {melodia}")
    
    # 3. Persistência
    comp = Composicao(
        tom=tom,
        escala=escala,
        graus=graus,
        progressao=progressao,
        melodia=melodia,
        bpm=bpm
    )
    salvar_composicao(comp)
    
    # 4. Exportação MIDI (Único ponto de contato com music21)
    exportar_midi(progressao, melodia, nome_arquivo="bossa_nova_demo.mid", bpm=bpm)

if __name__ == "__main__":
    main()