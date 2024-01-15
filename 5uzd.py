import PySimpleGUI as sg 
layout=[ 
    [sg.Text('ievadi savu vārdu'),sg.InputText(key='-IN-',enable_events=True)], 
    [sg.Text('ievadi savu uzvārdu'),sg.InputText(key='-INN-', enable_events=True)], 
    [sg.Button('OK')]    
         
] 
 
window=sg.Window('Ziema', layout) 
while True: 
    event, values=window.read() 
    if event==sg.WIN_CLOSED: 
        break 
    if event=='OK': 
        print(values['-IN-']) 
    window.close