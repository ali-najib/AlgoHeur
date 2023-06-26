# AlgoHeur Project, by Ali Najib

Deze case gaat over het maken van de lijnvoering. Meer specifiek: over de lijnvoering van intercitytreinen. Dat betekent dat je binnen een gegeven tijdsframe een aantal trajecten uitzet. Een traject is een route van sporen en stations waarover treinen heen en weer rijden. Een traject mag niet langer zijn dan het opgegeven tijdsframe.

## Aan de slag
 Vereisten:
Python 3.8.9

### User Interface

Het gebruik van deze applicatie gaat via de file run.py. Alle relevante code-lines te runnen voor een gebruiker staan in die file.
Om een van de code-lines te runnen, verwijder de hashtag voor de desbetreffende codeline en run de file run.py. In Python3 gaat het runnen van de file als

```
python3 run.py
```

Merk op dat de variabelen ```iteration_count```, ```route_duration``` en ```route_count``` kunnen worden gevarieerd zoals gewenst door de gebruiker. 
\\
\\
Ook kan er worden gesleuteld
aan de file **code/algorithms/import_data.py** om de code te runnen onder de setting Holland of de setting Nationaal. Om de code te runnen onder de setting Holland,
insert **data/StationsHolland.csv** en **data/ConnectiesHolland.csv** in lines 8 en 21 van **code/algorithms/import_data.py** respectievelijk. Om de code te runnen onder de setting Nationaal
**insert data/StationsNationaal.csv** en **data/ConnectiesNationaal.csv** in lines 8 en 21 van **code/algorithms/import_data.py** respectievelijk.

### Resultaten
Resultaten van het gebruik van run.py komen tevoorschijn in de vorm van plots als pop-ups, en/of output in de vorm van tekst te vinden in **code/results** en/of output te zien in de terminal.


## Auteur

Ali Najib
