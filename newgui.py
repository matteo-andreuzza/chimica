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

    numero=int(values[0])
    print("#### Calcolatore formula minima di un composto chimmico ####")
    
    
    layout = [[sg.Button('Ok')] ]
    for i in range(numero):
        layout.append([sg.Text("inserisci il simbolo dell'elemento " + str(i))],)
        layout.append([sg.Input()],)
        layout.append([sg.Text("inserisci la percentuale dell'elemento" + str(i))],)
        layout.append([sg.Input()],)
        
        # Create the window
    window = sg.Window('Window Title', layout)      # Part 3 - Window Defintion

    # Display and interact with the Window
    event, values = window.read()                   # Part 4 - Event loop or Window.read call

    # Do something with the information gathered
    print('Hello', values[0], "! Thanks for trying PySimpleGUI")

    # Finish up by removing from the screen
    window.close() 

    
    
    lde = []
    for i in range(numero):
        print("passaggio " + str(i))
        print("numero"  + str(numero))
        print(str(numero))
        try:
            qsim1 = float(str(values[i+1]))/a[values[i]]
        except ValueError:
            print("exept")
            qsim1 = float(str(values[i+2]))/a[values[i+1]]
        lde.append(qsim1)
        print(lde)

    lde.sort()
    qmin = lde[0]
    lde.reverse()
    print(lde)
    for i in range(numero):
        print("[debug] indice for : " + str(i))
        print("[debug] posizione lde : " + str(lde[i]))
        per1 = lde[i]  / qmin
        print("presenza elemento " + str(i+1) + " : " + str(per1))
formulaMin()