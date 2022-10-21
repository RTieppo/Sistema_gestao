from PySimpleGUI import PySimpleGUI as sg

from biblioteca_de_funções import Telas

janela_login = Telas.tela_login()

while True:
    Windows, eventos, valores = sg.read_all_windows(timeout=1000)

    if Windows == janela_login and eventos == sg.WIN_CLOSED:
        break