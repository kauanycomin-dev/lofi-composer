from music21 import scale 

def gerar_escala_maior(nota_inicial):
    # Cria uma escala maior a partir da nota inicial fornecida
    escala = scale.MajorScale(nota_inicial)
    notas = escala.getPitches(f'{nota_inicial}4', f'{nota_inicial}5')  # Obtém as notas da escala no intervalo de uma oitava
    return [str(nota) for nota in notas]  # Retorna as notas como strings

if __name__ == "__main__":
    notas_do = gerar_escala_maior('C')  # Exemplo: gera a escala maior de Dó
    print(f'Escala de Dó maior: {notas_do}')

    notas_sol = gerar_escala_maior('G')  # Exemplo: gera a escala maior de Sol
    print(f'Escala de Sol maior: {notas_sol}')  
          