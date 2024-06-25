import streamlit as st
from time import sleep
from crud import read_all_users


def login():
    with st.container(border=True):
        st.markdown('Bem-vindo a tela de login')
        users = read_all_users()
        users = {user.name: user for user in users}
        username = st.selectbox(
            'Selecione o usuário',
            list(users.keys())
        )
        pwd_user = st.text_input(
            'Digite sua senha',
            type='password'
        )
        if st.button('Logar'):
            user = users[username]
            if user.check_password(pwd_user):
                st.success('Login efetuado com sucesso!!')
                st.session_state['user'] = user
                st.session_state['logado'] = True
                sleep(1)
                st.rerun()
            else:
                st.error('Senha incorreta')


def main():
    if not 'logado' in st.session_state:
        st.session_state['logado'] = False

    if not st.session_state['logado']:
        login()

    else:
        st.markdown('# Bem-vindo ao WebApp FériasIn')


if __name__ == '__main__':

    main()
