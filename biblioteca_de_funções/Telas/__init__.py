from PySimpleGUI import PySimpleGUI as sg


#definição de fonte

font_geral = ('Berlin Sans FB Demi Negrito', 15)
font_input = ('Berlin Sans FB',10)

tamanho = (500,600)


def tela_login(user_login = '',user_senha=''):

    sg.theme('Black')

    janela = [
        [sg.Column([[sg.Image(r'img\login.png')]],justification='c')],

        [sg.Text('Login:', font=font_geral,justification='c', size=(25,0))],
        [sg.Column([[sg.Input(user_login,key='-user-', size=(35,0), justification='c')]], justification='c')],

        [sg.Text('Senha:', font=font_geral, justification='c', size=(25,0))],
        [sg.Column([[sg.Input(user_senha,key='-senha-', size=(35,0), justification= 'c',password_char='*')]], justification='c')],

        [sg.Column([[sg.Checkbox('Lembrar', font=font_geral)]], justification='c')],

        [sg.Text(' ', key='-info_user-', justification='c', font=font_geral, text_color='darkgreen'),
        sg.Text(' ',key='-info_user_erro-', justification='c', font=font_geral, text_color='darkred')],

        [sg.Column([[sg.Button('Entrar', font=font_geral)]], justification='c')],
    ]
    return sg.Window('gera', finalize=True, size=tamanho, layout = janela)

def tela_menu():

    sg.theme('Black')

    janela = [
        [sg.Column([[sg.Image('')]], justification='c')],

    ]
