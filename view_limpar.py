import PySimpleGUI as sg


sg.theme('DarkBlue14')
layout = [
    [sg.Text('Limpar as tabelas:')],
    [sg.Checkbox('Pessoa')],
    [sg.Checkbox('Acidente')],
    [sg.Checkbox('Via')],
    [sg.Checkbox('Veiculos')],
    [sg.Push(), sg.Button('Limpar Tabela')]
]

window = sg.Window('Limpeza de Tabelas', layout=layout, size=(300, 200))

while True:
    event, values = window.read()
    print(event)
    if event == sg.WIN_CLOSED:
        break
    elif values[0] or values[1] or values[2] or values[3]:
        nomes_tabelas = ''
        if values[0]:
            nomes_tabelas += '- Pessoa \n'
        if values[1]:
            nomes_tabelas += '- Acidente \n'
        if values[2]:
            nomes_tabelas += '- Via \n'
        if values[3]:
            nomes_tabelas += '- Veiculos \n'

        text = sg.PopupYesNo(
            'Deseja limpar as tabelas selecionas ?\n{}'.format(nomes_tabelas)).upper()

        if text == 'YES':
            if values[0]:
                #sg.popup('Tabela Pessoa Limpando')
                print('Rodou limpeza PESSOA')
                print(values[0])
            if values[1]:
                #sg.popup('Tabela Acidente Limpando')
                print('Rodou limpeza ACIDENTE')
            if values[2]:
                #sg.popup('Tabela Via Limpando')
                print('Rodou limpeza VIA')
            if values[3]:
                #sg.popup('Tabela Veiculos Limpando')
                print('Rodou limpeza VEICULOS')
        else:
            continue
        sg.popup('Tabelas Limpas: \n{}'.format(nomes_tabelas))

window.close()
exit()
