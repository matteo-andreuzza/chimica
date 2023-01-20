import pandas as pd
import sys
import PySimpleGUI as sg

def formulaMin():
    data= pd.read_csv("table.csv")
    df =data
    print(df)
    a = df.set_index('Symbol').to_dict()['AtomicMass']
    print(a)


    # Define the window's contents
    layout = [  [sg.Text("inserisci il numero di elementi presenti nel composto")],     # Part 2 - The Layout
                [sg.Input()],
                [sg.Button('Ok')] ]
    # Create the window
    window = sg.Window('Window Title', layout)      # Part 3 - Window Defintion

    # Display and interact with the Window
    event, values = window.read()                   # Part 4 - Event loop or Window.read call

    # Do something with the information gathered
    print('Hello', values[0], "! Thanks for trying PySimpleGUI")

    # Finish up by removing from the screen
    window.close()    



    print("#### Calcolatore formula minima di un composto chimmico ####")
    if int(values[0]) == 2:
        layout = [ 
            [sg.Text("inserisci il simbolo del primo elemento")],     # Part 2 - The Layout
            [sg.Input()],
            [sg.Text("inserisci la percentuale primo elemento")],  # Part 2 - The Layout
            [sg.Input()],            
            [sg.Text("inserisci il simbolo del secondo elemento")],     # Part 2 - The Layout
            [sg.Input()],
            [sg.Text("inserisci la percentuale del secondo elemento")],     # Part 2 - The Layout
            [sg.Input()],
            [sg.Button('Ok')] ]

        # Create the window
        window = sg.Window('Window Title', layout)      # Part 3 - Window Defintion

        # Display and interact with the Window
        event, values = window.read()                   # Part 4 - Event loop or Window.read call

        # Do something with the information gathered
        print('Hello', values[0], "! Thanks for trying PySimpleGUI")

        # Finish up by removing from the screen
        window.close()    
        print("inserisci la percentuale di ogni elemento")
        s1 = str(values[0])
        p1 = str(values[1])
        s2 = str(values[2])
        p2 = str(values[3])
        if (float(values[1]) + float(values[3]) != 100.0):
            sg.popup("non puoi mettere valori la cui somma non faccia 100")
            print("non puoi mettere valori la cui somma non faccia 100")
            formulaMin()
        qsim1 = float(p1)/a[s1]
        qsim2 = float(p2)/a[s2]
        
        lde  = [qsim1, qsim2]
        lde.sort()
        qmin = lde[0]
        per1 = qsim1  / qmin
        per2 = qsim2 / qmin
        sg.popup("presenza primo elemento " + str(per1))
        sg.popup("presenza secondo elemento " + str(per2))
    elif int(values[0]) == 3:
        layout = [ 
                [sg.Text("inserisci il simbolo del primo elemento")],     # Part 2 - The Layout
                [sg.Input()],
                [sg.Text("inserisci la percentuale primo elemento")],  # Part 2 - The Layout
                [sg.Input()],            
                [sg.Text("inserisci il simbolo del secondo elemento")],     # Part 2 - The Layout
                [sg.Input()],
                [sg.Text("inserisci la percentuale del secondo elemento")],     # Part 2 - The Layout
                [sg.Input()],
                [sg.Text("inserisci il simbolo del terzo elemento")],     # Part 2 - The Layout
                [sg.Input()],
                [sg.Text("inserisci la percentuale del terzo elemento")],     # Part 2 - The Layout
                [sg.Input()],
                [sg.Button('Ok')] ]

        # Create the window
        window = sg.Window('Window Title', layout)      # Part 3 - Window Defintion

        # Display and interact with the Window
        event, values = window.read()                   # Part 4 - Event loop or Window.read call

        # Do something with the information gathered
        print('Hello', values[0], "! Thanks for trying PySimpleGUI")

        # Finish up by removing from the screen
        window.close()    
        print("inserisci la percentuale di ogni elemento")
        s1 = str(values[0])
        p1 = str(values[1])
        s2 = str(values[2])
        p2 = str(values[3])
        s3 = str(values[4])
        p3 = str(values[5])
        if (float(values[1]) + float(values[3]) + float(values[5])!= 100.0):
            sg.popup("non puoi mettere valori la cui somma non faccia 100")
            print("non puoi mettere valori la cui somma non faccia 100")
            formulaMin()
        qsim1 = float(p1)/a[s1]
        qsim2 = float(p2)/a[s2]
        qsim3 = float(p3)/a[s3]
        
        lde  = [qsim1, qsim2, qsim3]
        lde.sort()
        qmin = lde[0]
        per1 = qsim1  / qmin
        per2 = qsim2 / qmin
        per3 = qsim3 / qmin
        sg.popup("presenza primo elemento " + str(per1))
        sg.popup("presenza secondo elemento " + str(per2))
        sg.popup("presenza terzo elemento " + str(per3))
    else:
        print("numero non supportato")


    # Finish up by removing from the screen
    window.close()  
    
formulaMin()