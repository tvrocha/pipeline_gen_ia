import streamlit as st
import contrato
from datetime import datetime, time


def main():

    # Titulo do CRM
    st.title('Sistema de CRM e Vendas da ZapFlow - FrontEnd Simples')

    # Inputs 
    email = st.text_input('Campo de texto para inserção do email do vendedor.')
    data = st.date_input('Campo para selecionar a data em que a venda foi realizada.', datetime.now())
    hora = st.time_input('Campo para selecionar a hora em que a venda foi realizada.', value=time(9, 0))
    valor = st.number_input('Campo numérico para inserir o valor monetário da venda realizada.')
    qtde = st.number_input('Campo numérico para inserir a quantidade de produtos vendidos.')
    produto = st.selectbox('Campo de seleção para escolher o produto vendido.', ["ZapFlow com Gemini", "ZapFlow com chatGPT", "ZapFlow com Llama3.0"])

    if st.button('Salvar'):
        st.write(f'E-mail do Vendedor: {email}')
        data_hora = datetime.combine(data, hora)
        st.write(f'Data/Hora: {data_hora}')


if __name__ == '__main__':
    main()
