import PySimpleGUI as sg
vidgeti = [
    [sg.Text('Имя'), sg.InputText(key='Игрок', default_text= 'Xlerian')],
    [sg.Text("Сложность"), sg.OptionMenu(values = ["Легко(5сек)","Нормально(4сек)","Сложно(3сек)","Хардкор(1сек)"], default_value = "Нормально(4сек)", key= 'Сложность')],
    [sg.Button('Выход'), sg.Button('Старт')]
]
a = 0
okno = sg.Window('Мяч', vidgeti)
while a == 0:
    sobytie = okno.read()
    if sobytie[0] == 'Выход' or sobytie[0] == 'Старт' or sobytie[0] == None:
        a = 1
    sobitiya = sobytie[1]
    sobitiya_knopok = sobytie[0]