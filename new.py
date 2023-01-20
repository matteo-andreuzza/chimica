import pandas as pd

data= pd.read_csv("table.csv")
df =data
print(df)
a = df.set_index('Symbol').to_dict()['AtomicMass']
print(a)

print("#### Calcolatore formula minima di un composto chimmico ####")
try:
    num = int(input("inserisci il numero di elementi che contiene il coposto"))
except ValueError:
    print("inserire un valore numerico")
    sys.exit(1) 
lde =[]
for i in range(num):
    print("inserisci la percentuale di ogni elemento")
    s1 = input("inserisci il simbolo del primo elemento")
    p1 = input("inserisci la percentuale del primo elemento")  
    qsim1 = float(p1)/a[s1]
    lde.append(qsim1)   
lde.sort()
qmin = lde[0]
lde.reverse()
print(lde)
for i in range(num):
    print("[debug] indice for : " + str(i))
    print("[debug] posizione lde : " + str(lde[i]))
    per1 = lde[i]  / qmin
    print("presenza elemento " + str(i+1) + " : " + str(per1))
