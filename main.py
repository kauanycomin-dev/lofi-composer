from escala import gerar_escala_maior
from progressao import gerar_progressao
from melodia import gerar_melodia
from exportador import exportar_midi
from persistencia import Composicao, salvar_composicao

def main():
    tom = "C"
    bpm = 110

    # Definição da Estrutura Musical (Bossa Nova Típica)
    # Cada número representa um grau da escala maior
    secoes = {
        "Intro": [1, 1, 1, 1],                      # 4 compassos (I)
        "Parte A": [1, 6, 2, 5] * 4,                 # 16 compassos (I - vi - ii - V)
        "Parte B": [4, 4, 1, 1, 2, 5, 1, 5] * 2,     # 16 compassos (IV - I - ii - V)
        "Outro": [1, 6, 2, 5] * 3                   # 12 compassos (I - vi - ii - V)
    }

    # Junta todas as seções em uma lista única de graus (Total: 48 compassos)
    graus_completos = []
    for nome_secao, graus in secoes.items():
        graus_completos.extend(graus)

    # Duração calculada: 48 compassos * ~2.18s por compasso ≈ 1m44s
    print(f"--- Gerando Bossa Nova Completa (~1m44s) no tom de {tom} ---")
    print(f"Total de compassos: {len(graus_completos)}")

    # 2. Execução do Pipeline Musical
    escala = gerar_escala_maior(tom)
    progressao = gerar_progressao(escala, graus_completos, tamanho=4)
    melodia = gerar_melodia(escala, progressao, notas_por_compasso=4)

    # 3. Persistência dos Dados
    comp = Composicao(
        tom=tom,
        escala=escala,
        graus=graus_completos,
        progressao=progressao,
        melodia=melodia,
        bpm=bpm
    )
    salvar_composicao(comp, "bossa_nova_completa.json")

    # 4. Exportação MIDI
    exportar_midi(
        progressao=progressao,
        melodia=melodia,
        nome_arquivo="bossa_nova_completa.mid",
        bpm=bpm
    )

if __name__ == "__main__":
    main()