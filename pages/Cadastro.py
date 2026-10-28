
import streamlit as st
from storage import listar_produtos, salvar_produtos

st.title("➕ Cadastro de roupas")
st.write("Preencha os dados para cadastrar uma nova peça.")

with st.form("form_cadastro"):
    nome = st.text_input("Nome da roupa *")
    
    col1, col2 = st.columns(2)

    with col1:
        categoria = st.selectbox(
            "Categoria",
            ["Camiseta", "Calça", "Vestido", "Saia",
             "Blusa", "Jaqueta", "Short", "Outro"]
        )

        tamanho = st.selectbox(
            "Tamanho",
            ["PP", "P", "M", "G", "GG", "XGG", "Único"]
        )

        cor = st.text_input("Cor")

    with col2:
        marca = st.text_input("Marca")
        codigo = st.text_input("Código único da peça")
        estoque = st.number_input(
            "Quantidade inicial",
            min_value=0,
            step=1
        )

    col3, col4 = st.columns(2)

    with col3:
        preco = st.number_input(
            "Preço de venda (R$)",
            min_value=0.01,
            value=49.90,
            step=1.0
        )

    with col4:
        custo = st.number_input(
            "Custo da peça (R$)",
            min_value=0.0,
            value=20.0,
            step=1.0
        )

    descricao = st.text_area("Descrição (opcional)")

    enviar = st.form_submit_button(
        "Cadastrar roupa",
        use_container_width=True
    )

if enviar:
    if not nome.strip():
        st.error("Informe o nome da roupa.")
    elif not codigo.strip():
        st.error("Informe um código para a roupa.")
    else:
        produtos = listar_produtos()

        codigo_existe = any(
            p["codigo"].lower() == codigo.strip().lower()
            for p in produtos
        )

        if codigo_existe:
            st.error("Esse código já está cadastrado.")
        else:
            produto = {
                "nome": nome.strip(),
                "categoria": categoria,
                "tamanho": tamanho,
                "cor": cor.strip(),
                "marca": marca.strip(),
                "codigo": codigo.strip(),
                "estoque": int(estoque),
                "preco": float(preco),
                "custo": float(custo),
                "descricao": descricao.strip()
            }

            produtos.append(produto)
            salvar_produtos(produtos)

            st.success("Roupa cadastrada com sucesso!")
            st.rerun()
