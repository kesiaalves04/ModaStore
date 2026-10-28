
import streamlit as st
from storage import listar_produtos, listar_vendas

st.title("👗 ModaStore PRO")
st.subheader("Sistema de gerenciamento de loja de roupas")

st.write(
    "Bem-vindo(a)! Aqui você pode cadastrar roupas, "
    "controlar o estoque, registrar vendas e consultar relatórios."
)

produtos = listar_produtos()
vendas = listar_vendas()

quantidade_produtos = len(produtos)
total_pecas = sum(p["estoque"] for p in produtos)
total_vendas = sum(v["total"] for v in vendas)

col1, col2, col3 = st.columns(3)

col1.metric("Modelos cadastrados", quantidade_produtos)
col2.metric("Peças em estoque", total_pecas)
col3.metric("Valor das vendas", f"R$ {total_vendas:.2f}")

st.divider()

st.subheader("✨ O que você deseja fazer?")

col1, col2 = st.columns(2)

with col1:
    if st.button("➕ Cadastrar roupa", use_container_width=True):
        st.switch_page("pages/Cadastro.py")

    if st.button("👚 Consultar produtos", use_container_width=True):
        st.switch_page("pages/Produtos.py")

with col2:
    if st.button("🛍️ Registrar venda", use_container_width=True):
        st.switch_page("pages/Vendas.py")

    if st.button("📊 Ver dashboard", use_container_width=True):
        st.switch_page("pages/Dashboard.py")

st.info("Utilize o menu lateral para acessar todas as páginas.")
