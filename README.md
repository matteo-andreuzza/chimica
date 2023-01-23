# chimica
è una questione di chimica
![alt text](https://i.ytimg.com/vi/qJylPiqVYI8/maxresdefault.jpg)

Questa è la prima versione dell'applicazione in python 🐍per calcolare la **formula minima** 🧪 di un composto chimico. Questa applicazione fa al caso tuo se:
- sei uno studente 📖 e devi calcolare la formula minima velocemente🏃‍♂️
- sei un programmatore/una programmatrice🧑‍💻👩‍💻 e stai imparando 📖
- stai imparando Python🐍 e vuoi capire come utilizzarlo e come funziona⚙️
- qualsiasi altro utilizzo


Durante la realizzazione di questa applicazione, ho realizzato una [serie di video](https://www.youtube.com/watch?v=qJylPiqVYI8&t=6s) sul mio [canale YouTube](https://www.youtube.com/@matteoandreuzza). Guardando questi video potrai capire come ho pensato e realizzato l'applicazione.

## Installazione:
Per installare l'app vai [sezione delle releases](https://github.com/matteo-andreuzza/chimica/releases/tag/0.1.1-beta) e segui la procedura indicata.

## Aspetti tecnici per programmatori
L'applicazione utilizza 4 moduli Python:
- [PySimpleGUI ](https://pypi.org/project/PySimpleGUI/)
- [Pandas](https://pypi.org/project/pandas/)
- Time
- Sys


Il funzionamento dell'applicazione è semplice e l'ho illustrato esaustivamente nel mio video YouTube. Qui un veloce riassunto:


- L'applicazione chiede il numero di elementi contenuti nel composto tramite una finestra
- Se viene inserito un carattere diverso da un numero, l'applicazione sengala l'errore e si riavvia
- Vengono chiesti all'utente simbolo chimico e presenza percentuale di ogni elemento. L'array che descrive il layout della finestra(con testi e campi di testo) viene popolato con un ciclo for, che inserisce nel suddetto array, tante coppie testo-campo di testo quanti sono gli elementi. 
- Dopo che l'utente ha inserito i dati, il programma li legge e gli archivia. Questi valori possono essere reperiti utilizzando `values[n]`, dove n è la posizione del dato, la quale viene assegnata in base all'ordine in cui i dati vengono inseriti.
- Quando i dati sono stati presi, vengono effettuati i calcoli necessari a determinare la formula minima. 
- I risultati delle operazioni vengono mostrati da una finestra.

## Contribuire
Se hai voglia di contribuire per rendere migliore l'applicazione, sentiti libero di forkare la repo e creare una pull request.

## errori
Se riscontri degli errori segnalameli qui su GitHub oppure alla mia mail andreuzzayt@outlook.it .
