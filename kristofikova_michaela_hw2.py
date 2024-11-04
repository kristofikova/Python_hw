# Načtení knihovny pandas a json
import pandas as pd
import json

# Načtení souboru netflix_titles.tsv
titles = pd.read_csv("netflix_titles.tsv",sep = '\t')

# Vytvoření slovníku s konkrétními sloupci
netflix_list = []

# definice pro určení dekády pro konkrétní rok
def year_to_decade(year):
    decade = (year // 10) * 10
    return decade

# procházení DF pomocí for cyklu
for i in range(len(titles)):
    # Vytvoření prvního klíče a hodnot slovníku - title
    title = titles["PRIMARYTITLE"].iloc[i]
    
    # Vytvoření druhého klíče a hodnot slovníku - directors
    if pd.notnull(titles["DIRECTOR"].iloc[i]):
        directors = [director.strip() for director in titles["DIRECTOR"].iloc[i].split(",")]
    else:
        directors = []

    # Vytvoření třetího klíče a hodnot slovníku - cast
    if pd.notnull(titles["CAST"].iloc[i]):
        cast = [cast.strip() for cast in titles["CAST"].iloc[i].split(",")]
    else:
        cast = []
    
    # Vytvoření čtvrtého klíče a hodnot slovníku - genres
    if pd.notnull(titles["GENRES"].iloc[i]):
        genres = titles["GENRES"].iloc[i].split(",")
    else:
        genres = []

    # Vytvoření pátého klíče a hodnot slovníku - decade
    if pd.notnull(titles["STARTYEAR"].iloc[i]):
        start_year = int(titles["STARTYEAR"].iloc[i])
        decade = year_to_decade(start_year)
    else:
        start_year = None

# Vytvoření slovníku
    dictionary = {
        "title": title,
        "directors": directors,
        'cast': cast,
        'genres': genres,
        'decade': decade,
    }

# přidání slovníku do seznamu
    netflix_list.append(dictionary)

# uložení souboru do Json formátu
with open("hw22_output.json","w") as json_file:
    json.dump(netflix_list,json_file,ensure_ascii=False,indent=4)