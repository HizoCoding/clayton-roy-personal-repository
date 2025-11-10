import tkinter as tk
from tkinter import filedialog
import PySimpleGUI as sg
from math import *

def Load_File(row_information):
        
        file_types = [("Text Files", "*.txt")]
        file_path = filedialog.askopenfilename(filetypes=file_types)
        i = 0
        
        # opens file_path in read only as a file variable
        with open(file_path, "r") as file:
                
                #store file.readline() in variable content
                #readline will read 1 line incrementally of a file
                content = file.readline()
                
                #store content.split(",") in lines variable.
                #.split(",") parses out commas from the input data
                lines = content.split(",")
                
                #prints lines
                print(lines)
                
                #line is set to first piece of data in lines
                # the for loop will iterate through all lines before exiting
                for line in lines:
                        
                        #row_information.append(line) which means line will get added to our list
                        row_information.append(line)
                        
                        #prints row_information 
                        # this is strictly for testing purposes not used in final product.
                        print(row_information)
                        
                lines.close()
                        

                        
                        
                        
        
        
def Save_File(rows):
        
        with open('Accounts.txt', 'w') as file:
                file.write(rows)
                
        ##https://realpython.com/read-write-files-python/

        file.close()

def Add_Account(row_information):
        
        
        
        
        
        layout = [[sg.Text('Account'), sg.Input()],
                  [sg.Text('Username'), sg.Input()],
                  [sg.Text('Password'), sg.Input()],
                  [sg.Text('Rank'), sg.Input()],
                  [sg.Text('LP'), sg.Input()],
                  [sg.Text('Win Rate'), sg.Input()],
                  [sg.Text('Win/Loss'), sg.Input()],
                  [sg.OK(), sg.Cancel()]]
        
        window = sg.Window('Account Wizard', layout)
        
        event , values = window.read()
        
        while True:
                if event == "OK":
                        for i in values:
                                
                                row_information.append(values[i])
                                
                        break
                        
                
                if event == "Cancel":
                        break
        
       
        window.close()