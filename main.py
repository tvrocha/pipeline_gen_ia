import streamlit as st
from contrato import Vendas, ProdutoEnum
from datetime import datetime, time
from pydantic import ValidationError
from db import salvar_no_postgres


def main():

    # Titulo do CRM
    st.title('Sistema de CRM - FrontEnd Simples')

    lista_selectbox = [
        "Loja Física",
        "Loja Online",
        "Terceiros",
    ]

    # Inputs
    email = st.text_input('E-mail do vendedor:')
    data = st.date_input('Data da venda:', datetime.now())
    hora = st.time_input('Hora da venda:', value=time(9, 0))
    valor = st.number_input('Valor da venda:')
    qtde = st.number_input('Unidades vendidas:')
    produto = st.selectbox('Selecione o método da venda:', lista_selectbox)

    if st.button('Salvar'):

        try:
            data_hora = datetime.combine(data, hora)

            venda = Vendas(
                email=email,
                data=data_hora,
                valor=valor,
                qtde=qtde,
                produto=produto
            )

            salvar_no_postgres(venda)

        except ValidationError as e:

            st.write(f'Erro: {e}')


if __name__ == '__main__':
    main()
