
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from storage import listar_produtos, listar_vendas

st.title("📊 Dashboard da ModaStore")

produtos = listar_produtos()
vendas = listar_vendas()

faturamento = sum(v["total"] for v in vendas)
pecas_vendidas = sum(v["quantidade"] for v in vendas)
estoque_total = sum(p["estoque"] for p in produtos)

col1, col2, col3 = st.columns(3)

col1.metric("Faturamento", f"R$ {faturamento:.2f}")
col2.metric("Peças vendidas", pecas_vendidas)
col3.metric("Peças em estoque", estoque_total)

st.divider()

if produtos:
    st.subheader("📦 Estoque por categoria")

    df_produtos = pd.DataFrame(produtos)

    estoque_categoria = df_produtos.groupby(
        "categoria"
    )["estoque"].sum()

    fig, ax = plt.subplots()
    estoque_categoria.plot(kind="bar", ax=ax)
    ax.set_xlabel("Categoria")
    ax.set_ylabel("Quantidade")
    ax.set_title("Quantidade em estoque por categoria")
    plt.xticks(rotation=35, ha="right")
    fig.tight_layout()

    st.pyplot(fig)
    plt.close(fig)

    st.subheader("📏 Estoque por tamanho")

    estoque_tamanho = df_produtos.groupby(
        "tamanho"
    )["estoque"].sum()

    fig2, ax2 = plt.subplots()
    estoque_tamanho.plot(kind="bar", ax=ax2)
    ax2.set_xlabel("Tamanho")
    ax2.set_ylabel("Quantidade")
    ax2.set_title("Quantidade em estoque por tamanho")
    fig2.tight_layout()

    st.pyplot(fig2)
    plt.close(fig2)

    st.subheader("⚠️ Produtos com estoque baixo")

    estoque_baixo = [
        p for p in produtos
        if p["estoque"] <= 5
    ]

    if estoque_baixo:
        st.dataframe(
            pd.DataFrame(estoque_baixo)[
                ["nome", "codigo", "tamanho", "estoque"]
            ],
            use_container_width=True,
            hide_index=True
        )
    else:
        st.success("Nenhum produto com estoque baixo.")
else:
    st.info("Cadastre roupas para visualizar os gráficos.")

st.divider()
st.subheader("💰 Resumo das vendas")

if vendas:
    st.dataframe(
        pd.DataFrame(vendas),
        use_container_width=True,
        hide_index=True
    )
else:
    st.info("Ainda não há vendas para exibir.")
