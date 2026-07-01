from escala import gerar_escala_maior

def gerar_acorde(escala_notas, indices): 
    # Extrai notas específicas de uma escala pra formar um acorde 
    return [escala_notas[i] for i in indices] 

if __name__ == "__main__":
    notas_do = gerar_escala_maior('C')  # Gera a escala maior de Dó
    print(f'Escala: {notas_do}')

    triade = gerar_acorde(notas_do, [0, 2, 4])  # Gera a tríade de Dó maior (C, E, G )
    print(f'Tríade (acorde básico): {triade}')

    com_setima = gerar_acorde(notas_do, [0, 2, 4, 6])
    print(f'Com sétima: {com_setima}')  # Gera acorde com sétima (C, E, G, B)