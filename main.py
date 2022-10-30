import pandas as pd

data= pd.read_csv("table.csv")
df =data
print(df)
a = df.set_index('Symbol').to_dict()['AtomicMass']
print(a)

print("#### Calcolatore formula minima di un composto chimmico ####")
num = int(input("inserisci il numero di elementi che contiene il coposto"))
if num == 2:
    print("inserisci la percentuale di ogni elemento")
    s1 = input("inserisci il simbolo del primo elemento")
    p1 = input("inserisci la percentuale del primo elemento")
    s2 = input("inserisci il simbolo del secondo elemento")
    p2 = input("inserisci la percentuale del secondo elemento")    
    qsim1 = print("quantità di sostanza in moli del primo elementi: " + int(p1)/a[s1])
    qsim2 = print("quantità di sostanza in moli del secondo elementi: " + int(p2)/a[s2])
    lde  = [qsim1, qsim2]
    lde.sort()
    qmin = lde[0]
    per1 = qsim1  / qmin
    per2 = qsim2 / qmin
    print("presenza primo elemento " + per1)
    print("presenza secondo elemento " + per2)
elif num == 3:
    print("inserisci la percentuale di ogni elemento")
    s1 = input("inserisci il simbolo del primo elemento")
    p1 = input("inserisci la percentuale del primo elemento")
    s2 = input("inserisci il simbolo del secondo elemento")
    p2 = input("inserisci la percentuale del secondo elemento")    
    s3 = input("inserisci il simbolo del terzo elemento")
    p3 = input("inserisci la percentuale del terzo elemento")  
    
    qsim1 = float(p1)/a[s1]
    qsim2 = float(p2)/a[s2]
    qsim3 = float(p3)/a[s3]
    
    lde  = [qsim1, qsim2, qsim3]
    lde.sort()
    qmin = lde[0]
    per1 = qsim1  / qmin
    per2 = qsim2 / qmin
    per3 = qsim3 / qmin
    print("presenza primo elemento " + str(per1))
    print("presenza secondo elemento " + str(per2))
    print("presenza terzo elemento" + str(per3))
else:
    print("numero non supportato")

