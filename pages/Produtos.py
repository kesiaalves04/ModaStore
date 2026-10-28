
import streamlit as st
import pandas as pd
from storage import listar_produtos, salvar_produtos

st.title("👚 Produtos e estoque")

produtos = listar_produtos()

if not produtos:
    st.info("Nenhuma roupa cadastrada ainda.")
    st.stop()

pesquisa = st.text_input("🔎 Pesquisar por nome, código ou categoria")

filtrados = [
    p for p in produtos
    if pesquisa.lower() in (
        p["nome"] + " " + p["codigo"] + " " + p["categoria"]
    ).lower()
]

if filtrados:
    tabela = pd.DataFrame(filtrados)
    st.dataframe(
        tabela,
        use_container_width=True,
        hide_index=True
    )
else:
    st.warning("Nenhum produto encontrado.")

st.divider()
st.subheader("✏️ Atualizar estoque")

codigos = [p["codigo"] for p in produtos]

codigo_selecionado = st.selectbox(
    "Selecione o código do produto",
    codigos
)

produto = next(
    p for p in produtos
    if p["codigo"] == codigo_selecionado
)

st.write(f"**Produto:** {produto['nome']}")
st.write(f"**Estoque atual:** {produto['estoque']} peças")

novo_estoque = st.number_input(
    "Nova quantidade em estoque",
    min_value=0,
    value=int(produto["estoque"]),
    step=1
)

if st.button("Salvar estoque"):
    for p in produtos:
        if p["codigo"] == codigo_selecionado:
            p["estoque"] = int(novo_estoque)

    salvar_produtos(produtos)
    st.success("Estoque atualizado!")
    st.rerun()

st.divider()
st.subheader("🗑️ Excluir produto")

confirmar = st.checkbox(
    "Confirmo que desejo excluir o produto selecionado."
)

if st.button("Excluir produto", type="primary"):
    if confirmar:
        produtos = [
            p for p in produtos
            if p["codigo"] != codigo_selecionado
        ]

        salvar_produtos(produtos)
        st.success("Produto excluído.")
        st.rerun()
    else:
        st.warning("Marque a confirmação antes de excluir.")
