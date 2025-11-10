import PySimpleGUI as sg
from UI_Functions import *

def gui_start():
    
    toprow = [ 'Name', 'User', 'Password', 'Rank', 'LP', 'Win Rate', 'Win/Loss']
    rows = []
    row_information = []
    
    Account_table = sg.Table(values= rows, headings=toprow,
                             auto_size_columns=True,
                             display_row_numbers= False,
                             justification='center', key='-TABLE-',
                             selected_row_colors='black on white', 
                             enable_events= True,
                             expand_x=True,
                             expand_y=True,
                             enable_click_events=True)
    
    layout = [[sg.Button('Add'), sg.Button('Delete'), sg.Button('Save'), sg.Button('Quit'), sg.Button('Load')],
              [Account_table]]
    
    window = sg.Window('Window Title', layout)
    
    while True:
        event, values = window.read()          
        
        if event == sg.WINDOW_CLOSED or event == 'Quit':
            break
        
        if event == 'Add':
            row_information = []
            Add_Account(row_information)
            print(row_information)
            rows.append(row_information)
            Account_table.update(rows)
        
        if event == 'Delete':
             row_information = values['-TABLE-']
             rows.pop()
             Account_table.update(rows)               
        
        if event == 'Save':
            Save_File(rows)
            
        if event == 'Load':
            Load_File(row_information)
        
        window.close   
        
