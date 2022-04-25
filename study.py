import PySimpleGUI as sg
import pandas as pd
import datetime

# add some color
sg.theme('DarkAmber')

# path to excel
EXCEL_FILE = 'study.xlsx'
df = pd.read_excel(EXCEL_FILE)

get_date = datetime.datetime.now()
date = get_date.strftime("%x")
time = get_date.strftime("%X")
day = get_date.strftime("%A")
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

layout = [
    [sg.Text('Enter the results of your study period:')],
    [sg.Text("Date", size=(15,1)), sg.InputText(date, key="Date", size=(15,1))],
    [sg.Text("Time", size=(15,1)), sg.InputText(time, key="Time", size=(15,1))],
    [sg.Text('Weekday', size=(15,1)), sg.Combo(days, default_value= day, key='Weekday', size=(15,1))],
    [sg.Text('Study Time (hrs)', size=(15,1)), sg.InputText(key='Study Hours', size=(15,1))],
    [sg.Text('Activity', size=(15,1)), sg.InputText(key='Activity', size=(15,1))],
    [sg.Text('Productivity Rating', size=(15,1)), sg.Combo(['5', '4', '3', '2', '1'], key='Rating', size=(15,1))],
    [sg.Submit(), sg.Button('Clear'), sg.Exit()]
]

# pass to window
window = sg.Window('Study Tracker', layout)

def clear_input():
    for key in values:
        window[key]('')
    return None

while True:
    event, values = window.read()
    print(event, values)
    if event in (sg.WIN_CLOSED,'Exit'):
        break
    if event == 'Clear':
        clear_input()
    if event == 'Submit':
        df = df.append(values, ignore_index=True)
        df.to_excel(EXCEL_FILE, index=False)
        sg.popup('Data saved')
        clear_input()
window.close()

