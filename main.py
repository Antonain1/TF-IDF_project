from fonction_de_base import *
from TF_IDF import *



president = []
president_avec_numero = []

# création du dictionnaire contenant les noms et prenoms des presidents
dictionnaire_nom_president = {
    "Giscard dEstaing": "Valéry",
    "Hollande": "François",
    "Macron": "Emmanuel",
    "Chirac": "Jacques",
    "Mitterrand": "François",
    "Sarkozy": "Nicolas"
}

# création du dictionnaire contenant les noms et prenoms des presidents
occurence_president = {
    "Chirac1": {},
    "Chirac2": {},
    "Giscard dEstaing": {},
    "Hollande": {},
    "Macron": {},
    "Mitterrand1": {},
    "Mitterrand2": {},
    "Sarkozy": {}
}
occurence_president_copie = occurence_president
if __name__ == '__main__':
    directory = "./speeches"
    files_names = list_of_files(directory, "txt")
    copie(files_names)
    president_names(files_names, president)
    print(president)
    president_names_fichier(files_names,president_avec_numero)
    TF(occurence_president,files_names,president_avec_numero)
    #print (occurence_president)
    IDFdict = IDF(occurence_president)
    #print(IDFdict)
    TFIDF = TF_IDF(occurence_president,IDFdict,occurence_president_copie)
    print(TFIDF)
