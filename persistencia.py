import json
from dataclasses import dataclass, asdict
from typing import List

@dataclass
class Composicao:
    tom: str
    escala: List[str]
    graus: List[int]
    progressao: List[List[str]]
    melodia: List[str]
    bpm: int

def salvar_composicao(comp: Composicao, nome_arquivo: str = "composicao.json") -> None:
    """
    Salva os metadados e estrutura da composição em JSON local.
    Justificativa: JSON + Dataclass é a solução mais leve, transparente e sem dependências 
    adicionais (como SQLAlchemy ou SQLite) para salvar a estrutura pura de dados do backend.
    """
    with open(nome_arquivo, "w", encoding="utf-8") as f:
        json.dump(asdict(comp), f, indent=4, ensure_ascii=False)
    print(f"Composição salva em '{nome_arquivo}'.")

def carregar_composicao(nome_arquivo: str = "composicao.json") -> Composicao:
    """
    Carrega uma composição salva anteriormente.
    """
    with open(nome_arquivo, "r", encoding="utf-8") as f:
        dados = json.load(f)
    return Composicao(**dados)