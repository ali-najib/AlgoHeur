# Algorithms and Heuristics Project, by Ali Najib

Deze case gaat over het maken van **de** lijnvoering van intercitytreinen. Dat betekent dat er binnen een gegeven tijdsframe een aantal trajecten worden uitgezet. Een traject is een route van sporen en stations waarover treinen heen en weer rijden, en mag niet langer zijn dan het opgegeven tijdsframe. Het antwoord op de volgende vraag is de lijnvoering: Wat zijn de trajecten waarover de treinen gedurende de dag heen en weer rijden?

Een voorbeeldopdracht dat hieruit kan worden geformuleerd is: Maak een lijnvoering voor Noord- en Zuid-Holland met maximaal zeven trajecten binnen een tijdsframe van twee uur, waarbij alle verbindingen bereden worden.​

Ook kunnen lijnvoeringen worden geconstrueerd zodat ze voldoen aan bepaalde eisen (zoals de bovenstaande) en een bepaalde lijnvoeringsvoeringsoptimalisatie uitvoeren, zoals de maximalisatie van 
```
 K = p*10000 - (T*100 + Min)
```
waarbij ```p``` de fractie van de bereden verbindingen (dus tussen 0 en 1), ​
```T``` het aantal trajecten en ​```Min```  het aantal minuten in alle trajecten samen. Deze optimalisatie wordt uitgevoerd in dit project.

## Aan de slag
 Vereisten:
De code is geschreven in Python 3.8.9

### User Interface

Het gebruik van deze applicatie gaat via de file run.py. Alle relevante code-lines te runnen voor een gebruiker staan in die file.
Om een van de code-lines te runnen, verwijder de hashtag voor de desbetreffende codeline en run de file **run.py**. In Python3 gaat het runnen van de file als

```
python3 run.py
```

Merk op dat de variabelen ```iteration_count```, ```route_duration``` en ```route_count``` kunnen worden gevarieerd zoals gewenst door de gebruiker. 

Ook kan er worden gesleuteld aan de file **code/algorithms/import_data.py** om de code te runnen onder de setting Holland of de setting Nationaal. Om de code te runnen onder de setting Holland, insert **data/StationsHolland.csv** en **data/ConnectiesHolland.csv** in lines 8 en 21 van **code/algorithms/import_data.py** respectievelijk. Om de code te runnen onder de setting Nationaal **insert data/StationsNationaal.csv** en **data/ConnectiesNationaal.csv** in lines 8 en 21 van **code/algorithms/import_data.py** respectievelijk.

### Resultaten

Resultaten van het gebruik van run.py komen tevoorschijn in de vorm van plots als pop-ups, en/of output in de vorm van tekst te vinden in **code/results** en/of output te zien in de terminal.

### Structuur

De hierop volgende lijst beschrijft de belangrijkste mappen en files in het project, en waar je ze kan vinden:

 - **/code**: bevat alle code van dit project
    - **/code/algorithms**: bevat de code voor algoritmes
    - **/code/classes**: bevat de twee benodigde classes voor deze case
- **/data**: bevat de verschillende databestanden die nodig zijn.
- **/results**: bevat csv bestanden waarin output van de algorithmen te vinden


## Auteur

- Ali Najib
