
import streamlit as st

st.set_page_config(
    page_title="ModaStore PRO",
    page_icon="👗",
    layout="wide"
)

# Carregar o estilo visual
with open("styles.css", "r", encoding="utf-8") as arquivo:
    st.markdown(
        f"<style>{arquivo.read()}</style>",
        unsafe_allow_html=True
    )

# Páginas do sistema
pagina_inicio = st.Page(
    "pages/Home.py",
    title="Início",
    icon="🏠",
    default=True
)

pagina_cadastro = st.Page(
    "pages/Cadastro.py",
    title="Cadastrar roupas",
    icon="➕"
)

pagina_produtos = st.Page(
    "pages/Produtos.py",
    title="Produtos e estoque",
    icon="👚"
)

pagina_vendas = st.Page(
    "pages/Vendas.py",
    title="Vendas",
    icon="🛍️"
)

pagina_dashboard = st.Page(
    "pages/Dashboard.py",
    title="Dashboard",
    icon="📊"
)

pagina_relatorios = st.Page(
    "pages/Relatorios.py",
    title="Relatórios",
    icon="📄"
)

navegacao = st.navigation([
    pagina_inicio,
    pagina_cadastro,
    pagina_produtos,
    pagina_vendas,
    pagina_dashboard,
    pagina_relatorios
])

navegacao.run()
