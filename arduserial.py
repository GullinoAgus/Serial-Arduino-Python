import PySimpleGUI as sg
import numpy as np
import pandas as pd
import serial
import serial.tools.list_ports as serailpl

ser = serial.Serial(timeout=0.1)
data = []
receiving = False
puertos = [ports.device for ports in list(serailpl.comports())]

sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('Ingresar puerto COM'), sg.Combo(puertos)],
            [sg.Button('Ok'), sg.Button('Finish')],
            [sg.Listbox(values=data, key='texto', size=(30,10), )] 
        ]

# Create the Window
window = sg.Window('Serial Read', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.Read(timeout=0)
    if event == sg.WIN_CLOSED: # if user closes window or clicks cancel
        break
    
    if event == 'Ok':
        if values[0]:
            ser.setPort(values[0])
            ser.open()
            receiving = True
        else:
            sg.popup('Error: Puerto no seleccionado', title='Error' )
    elif event == 'Finish':
        ser.close()
        receiving = False

    if receiving:
        try:
            reading = ser.read()
            data.append(int(reading))
            window.find_element('texto').Update(values=data)
        except:
            pass

datframe = pd.DataFrame(data)
datframe.to_csv('./hola.csv', index=False, header=False)
datframe.to
ser.close()
window.close()