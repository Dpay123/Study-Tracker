from turtle import left
import PySimpleGUI as sg
import pandas as pd
import datetime
from random import choice
from topics import topics, vscode
# add some color
sg.theme('DarkAmber')

# path to excel
EXCEL_FILE = 'study.xlsx'
df = pd.read_excel(EXCEL_FILE)


get_date = datetime.datetime.now()
date = get_date.strftime("%x")
day = get_date.strftime("%A")
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
l_size = (10,1)
r_size = (11,1)

def chop(s):
    chop = 50
    char = '\n-'
    return char.join(s[i:i+chop] for i in range(0, len(s), chop))


col1 = [
    [sg.Text('Enter the results of your study period:', font='Arial 12 bold')],
    [sg.Text("Date:", size=l_size), sg.InputText(date, key="Date", size=r_size)],
    [sg.Text('Weekday:', size=l_size), sg.Combo(days, default_value= day, size=r_size, key='Weekday')],
    [sg.Text('Duration (hr):', size=(l_size)), sg.InputText(key='Duration', size=r_size)],
    [sg.Text('Type:', size=(l_size)), sg.Combo(['Coursework', 'Job Hunt', 'Coding', 'Video/Reading'], key="Type", size=r_size)],
    [sg.Text('Productivity Rating:', size=(14,1)), sg.Combo(['5', '4', '3', '2', '1'], key='Rating', size=l_size)],
    [sg.Submit(), sg.Button('Clear'), sg.Exit()]
]

col2 = [
    [sg.Text(text = 'Warmup: Spend 10-15 minutes exploring \nthe random topic below. Don\'t just skip \nboring/hard topics!', text_color='white', size=(40,3), font='bold')],
    [sg.Text(text=choice(topics), text_color='aqua', font='bold', size=(20,1), key="topic"), sg.Button('Reset')],

    [sg.HSeparator()],
    
    [sg.Text(text = "Today's VSCode Tooltip: ", text_color='white', font='Arial 10 italic bold'), sg.Text(choice(vscode)[0], key='tooltip_title', text_color='aqua', font='Arial 10 italic bold')],
    [sg.Text(text=chop(choice(vscode)[1]), text_color='aqua', key='tooltip', size=(40,3))]
]

layout = [
    [sg.Column(col1),
    sg.VSeperator(),
    sg.Column(col2)]
]

# pass to window
window = sg.Window('Study Tracker', layout, size=(650,220))

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
    if event == 'Reset':
        window.Element('topic').update(choice(topics))

        new_topic = choice(vscode)
        window.Element('tooltip_title').update(new_topic[0])
        window.Element('tooltip').update(chop(new_topic[1]))
window.close()

