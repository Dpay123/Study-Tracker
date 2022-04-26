from turtle import left
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
l_size = (10,1)
r_size = (11,1)

col1 = [
    [sg.Text('Enter the results of your study period:')],
    [sg.Text("Date:", size=l_size), sg.InputText(date, key="Date", size=r_size)],
    [sg.Text("Start Time:", size=l_size), sg.InputText("00:00:00", key="Start Time", size=r_size)],
    [sg.Text("End Time:", size=l_size), sg.InputText(time, key="End Time", size=r_size)],
    [sg.Text('Weekday:', size=l_size), sg.Combo(days, default_value= day, size=r_size, key='Weekday')],
    [sg.Text('Hours:', size=(l_size)), sg.InputText(key='Hours', size=r_size)],
    [sg.Text('Activity:', size=(6,1)),
        sg.Checkbox('Coding', key='Coding'),
        sg.Checkbox('Courses', key='Courses')],
        [sg.Checkbox('Videos', key='Videos'),
        sg.Checkbox('Reading', key='Reading'),
        sg.Checkbox('Other', key='Other')],
    [sg.Text('Productivity Rating:', size=(14,1)), sg.Combo(['5', '4', '3', '2', '1'], key='Rating', size=l_size)],
    [sg.Submit(), sg.Button('Clear'), sg.Exit()]
]

frame1 = [sg.Text('Frame 1')]
frame2 = [sg.Text('Frame 2')]

col2 = [[sg.Text('Column 2')], frame1, frame2]

layout = [
    [sg.Column(col1),
    sg.VSeperator(),
    sg.Column(col2, element_justification='c')]
]

# pass to window
window = sg.Window('Study Tracker', layout, size=(500,300))

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

