
import json
from pathlib import Path
from datetime import datetime

PASTA_DADOS = Path(__file__).parent / "dados"
ARQUIVO_PRODUTOS = PASTA_DADOS / "produtos.json"
ARQUIVO_VENDAS = PASTA_DADOS / "vendas.json"


def preparar_arquivo(caminho):
    PASTA_DADOS.mkdir(parents=True, exist_ok=True)

    if not caminho.exists():
        caminho.write_text("[]", encoding="utf-8")


def carregar(caminho):
    preparar_arquivo(caminho)

    try:
        return json.loads(caminho.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return []


def salvar(caminho, dados):
    preparar_arquivo(caminho)

    caminho.write_text(
        json.dumps(dados, ensure_ascii=False, indent=4),
        encoding="utf-8"
    )


def listar_produtos():
    return carregar(ARQUIVO_PRODUTOS)


def salvar_produtos(produtos):
    salvar(ARQUIVO_PRODUTOS, produtos)


def listar_vendas():
    return carregar(ARQUIVO_VENDAS)


def salvar_vendas(vendas):
    salvar(ARQUIVO_VENDAS, vendas)


def registrar_venda(codigo, quantidade, pagamento):
    produtos = listar_produtos()

    produto = next(
        (p for p in produtos if p["codigo"] == codigo),
        None
    )

    if produto is None:
        return False, "Produto não encontrado."

    if quantidade <= 0:
        return False, "A quantidade deve ser maior que zero."

    if produto["estoque"] < quantidade:
        return False, "Estoque insuficiente."

    total = produto["preco"] * quantidade
    produto["estoque"] -= quantidade

    venda = {
        "codigo": codigo,
        "produto": produto["nome"],
        "quantidade": quantidade,
        "preco_unitario": produto["preco"],
        "total": total,
        "pagamento": pagamento,
        "data": datetime.now().strftime("%d/%m/%Y %H:%M")
    }

    vendas = listar_vendas()
    vendas.append(venda)

    salvar_produtos(produtos)
    salvar_vendas(vendas)

    return True, "Venda registrada com sucesso!"
