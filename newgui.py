import pandas as pd
import sys
import PySimpleGUI as sg
import time

def formulaMin():
    data= pd.read_csv("table.csv")
    df =data
    print(df)
    a = df.set_index('Symbol').to_dict()['AtomicMass']
    print(a)
    layout = [  [sg.Text("inserisci il numero di elementi presenti nel composto")],     # Part 2 - The Layout
                [sg.Input()],
                [sg.Button('Ok')] ]
    window = sg.Window('Window Title', layout)      # Part 3 - Window Defintion
    event, values = window.read()                   # Part 4 - Event loop or Window.read call
    print('Hello', values[0], "! Thanks for trying PySimpleGUI")
    window.close()    
    try:
        numero=int(values[0])
    except ValueError:
        layout = [  [sg.Text("Non puoi inserire valori diversi da numeri, premi OK per riavviare l'app")],     # Part 2 - The Layout
            [sg.Button('Ok')] ]
        window = sg.Window('Conferma riavvio app', layout)      # Part 3 - Window Defintion
        event, values = window.read()                   # Part 4 - Event loop or Window.read call
        window.close()   
        formulaMin()
    layout = [[sg.Button('Ok')], ]
    for i in range(numero):
        layout.append([sg.Text("inserisci il simbolo dell'elemento " + str(i))],)
        layout.append([sg.Input()],)
        layout.append([sg.Text("inserisci la percentuale dell'elemento" + str(i))],)
        layout.append([sg.Input()],)
    window = sg.Window('Window Title', layout)      # Part 3 - Window Defintion
    event, values = window.read()                   # Part 4 - Event loop or Window.read call
    print('Hello', values[0], "! Thanks for trying PySimpleGUI")
    window.close() 
    lde = []
    for i in range(numero+(numero-1)):
        if i % 2 != 0:
            print("skipped")
            continue
        print("passaggio " + str(i))
        print("numero"  + str(numero))
        try:
            qsim1 = float(str(values[i+1]))/a[values[i]]
        except ValueError:
            layout = [  [sg.Text("non puoi inserire valori diversi da numeri, conferma riavvio APP")],     # Part 2 - The Layout
                [sg.Button('Ok')] ]
            window = sg.Window('Conferma riavvio app', layout)      # Part 3 - Window Defintion
            event, values = window.read()                   # Part 4 - Event loop or Window.read call
            window.close()   
            formulaMin()
        lde.append(qsim1)
        print(lde)
    lde.sort()
    qmin = lde[0]
    print(lde)
    layout = []
    for i in range(numero):
        print("[debug] indice for : " + str(i))
        print("[debug] posizione lde : " + str(lde[i]))
        per1 = lde[i]  / qmin
        layout.append([sg.Print("presenza elemento " + str(i+1) + " : " + str(per1))],)
    try: 
        window = sg.Window('Window Title', layout)      # Part 3 - Window Defintion
    except AttributeError:
        pass
    event, values = window.read()                   # Part 4 - Event loop or Window.read call
    time.sleep(5)
    layout = [  [sg.Text("Premi OK per chiudere")],     # Part 2 - The Layout
                [sg.Button('Ok')] ]
    window = sg.Window('Conferma chiusura', layout)      # Part 3 - Window Defintion
    event, values = window.read()                   # Part 4 - Event loop or Window.read call
    window.close()    
    window.close()    
try:
    formulaMin()
except TypeError:
    print("errore, restart")
    layout = [  [sg.Text("Premi OK per far ripartire l'app")],     # Part 2 - The Layout
            [sg.Button('Ok')] ]
    window = sg.Window('Conferma chiusura', layout)      # Part 3 - Window Defintion
    event, values = window.read()                   # Part 4 - Event loop or Window.read call
    window.close()   
    formulaMin()


