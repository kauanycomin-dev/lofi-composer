Algorithmic Lo-Fi / Bossa Nova Music Composer

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)
[![Status](https://img.shields.io/badge/Status-In%20Development-yellow?style=for-the-badge)]()

Um gerador algorítmico de composição musical em Python focado em **Bossa Nova e Lo-Fi**. 

O sistema aplica regras reais de teoria musical para construir progressões harmônicas com acordes estendidos e melodias coerentes, exportando o resultado final em formato **MIDI** estandardizado para qualquer DAW ou player.

---

## Destaques de Arquitetura & Design

* **Lógica Teórica em Python Puro:** Toda a construção de escalas, graus, empilhamento de terças (acordes com 7ª/9ª) e geração algorítmica de melodia é feita em Python puro, sem dependência de bibliotecas externas para a regra de negócio.
* **Módulo de Exportação Isolado:** A biblioteca `music21` é utilizada **exclusivamente** na camada final (`exportador.py`) para converter estruturas de dados em instâncias de `stream.Score` e gerar os arquivos MIDI.
* **Persistência Leve:** Estruturação dos dados da composição via `dataclass` e exportação nativa em JSON.

---

## Conceitos Musical-Algorítmicos Aplicados

1. **Construção de Escalas Maior:** Aplicação do padrão de intervalos `Tom - Tom - Semitom - Tom - Tom - Tom - Semitom` a partir de uma nota fundamental.
2. **Empilhamento de Terças & Graus:** Utilização do operador de módulo (`%`) para navegar circularmente pelos índices da escala, permitindo montar acordes estendidos (Tétrades) em qualquer grau ($I, ii, iii, IV, V, vi, vii^\circ$).
3. **Target Notes Melódicas:** A linha melódica prioriza notas pertencentes ao acorde atual nos **tempos fortes** (início do compasso) e notas gerais da escala nos **tempos fracos**, garantindo consonância harmônica.

---

## Estrutura do Projeto

```text
lofi-composer/
├── escala.py         # Lógica de geração da escala maior a partir da nota inicial
├── acordes.py        # Extração e empilhamento de notas por índice
├── progressao.py     # Generalização de acordes por grau da escala (módulo %)
├── melodia.py        # Algoritmo de criação da linha vocal/solo
├── exportador.py     # Integração com music21 (Score, Parts, Tempo e MIDI)
├── persistencia.py   # Dataclass e serialização JSON da composição
├── main.py           # Ponto de entrada do pipeline de geração
└── requirements.txt  # Dependência única do projeto (music21)
