
import streamlit as st
import pandas as pd
from storage import listar_produtos, listar_vendas, registrar_venda

st.title("🛍️ Registro de vendas")

produtos = listar_produtos()

if not produtos:
    st.warning("Cadastre pelo menos uma roupa antes de vender.")
    st.stop()

disponiveis = [p for p in produtos if p["estoque"] > 0]

if not disponiveis:
    st.warning("Não existem peças disponíveis no estoque.")
    st.stop()

opcoes = {
    f"{p['nome']} | {p['codigo']} | R$ {p['preco']:.2f} | Estoque: {p['estoque']}":
    p
    for p in disponiveis
}

selecionado = st.selectbox(
    "Selecione a roupa",
    list(opcoes.keys())
)

produto = opcoes[selecionado]

quantidade = st.number_input(
    "Quantidade",
    min_value=1,
    max_value=int(produto["estoque"]),
    value=1,
    step=1
)

pagamento = st.selectbox(
    "Forma de pagamento",
    ["Pix", "Dinheiro", "Cartão de crédito", "Cartão de débito"]
)

total = produto["preco"] * quantidade

st.metric("Valor total", f"R$ {total:.2f}")

if st.button("Confirmar venda", use_container_width=True):
    sucesso, mensagem = registrar_venda(
        produto["codigo"],
        int(quantidade),
        pagamento
    )

    if sucesso:
        st.success(mensagem)
        st.rerun()
    else:
        st.error(mensagem)

st.divider()
st.subheader("📋 Vendas recentes")

vendas = listar_vendas()

if vendas:
    tabela = pd.DataFrame(vendas).iloc[::-1]
    st.dataframe(
        tabela.head(20),
        use_container_width=True,
        hide_index=True
    )
else:
    st.info("Nenhuma venda registrada ainda.")
