
import streamlit as st
import pandas as pd
from storage import listar_produtos, listar_vendas

st.title("📄 Relatórios")
st.write("Consulte e exporte os dados da sua loja.")

produtos = listar_produtos()
vendas = listar_vendas()

st.subheader("👚 Relatório de produtos")

if produtos:
    df_produtos = pd.DataFrame(produtos)

    colunas_produtos = [
        "codigo", "nome", "categoria", "tamanho",
        "cor", "marca", "preco", "custo", "estoque"
    ]

    df_produtos = df_produtos[colunas_produtos]

    st.dataframe(
        df_produtos,
        use_container_width=True,
        hide_index=True
    )

    csv_produtos = df_produtos.to_csv(
        index=False
    ).encode("utf-8-sig")

    st.download_button(
        "⬇️ Baixar relatório de produtos",
        data=csv_produtos,
        file_name="relatorio_produtos.csv",
        mime="text/csv"
    )
else:
    st.info("Não existem produtos cadastrados.")

st.divider()
st.subheader("🛍️ Relatório de vendas")

if vendas:
    df_vendas = pd.DataFrame(vendas)

    st.dataframe(
        df_vendas,
        use_container_width=True,
        hide_index=True
    )

    csv_vendas = df_vendas.to_csv(
        index=False
    ).encode("utf-8-sig")

    st.download_button(
        "⬇️ Baixar relatório de vendas",
        data=csv_vendas,
        file_name="relatorio_vendas.csv",
        mime="text/csv"
    )
else:
    st.info("Não existem vendas registradas.")

st.divider()

faturamento = sum(v["total"] for v in vendas)
pecas_vendidas = sum(v["quantidade"] for v in vendas)

col1, col2 = st.columns(2)

col1.metric("Faturamento total", f"R$ {faturamento:.2f}")
col2.metric("Peças vendidas", pecas_vendidas)
