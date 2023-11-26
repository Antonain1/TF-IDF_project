from math import *

def moyenne(TFIDF):
    TFIDFmoyen = {}
    for mot in TFIDF["Chirac1"].keys():
        moyenne = 0
        for key in TFIDF.keys():
            moyenne += TFIDF[key][mot] / 8
        TFIDFmoyen[mot] = moyenne
    return TFIDFmoyen


def plusimportant(TFIDFmoyen):
    max = 0.1
    maxdejatrouvee = []
    TFIDFmoyendecroissant = {}
    while max != 0:
        max = 0
        for value in TFIDFmoyen.values():
            if max <= value and value not in maxdejatrouvee:
                max = value
        for key in TFIDFmoyen.keys():
            if max == TFIDFmoyen[key]:
                TFIDFmoyendecroissant[key] = TFIDFmoyen[key]
        maxdejatrouvee.append(max)
    return TFIDFmoyendecroissant


def moinsimportant(TFIDFmoyen):
    max = 0.1
    maxdejatrouvee = []
    TFIDFmoyencroissant = {}
    while max != 1000:
        max = 1000
        for value in TFIDFmoyen.values():
            if max >= value and value not in maxdejatrouvee:
                max = value
        for key in TFIDFmoyen.keys():
            if max == TFIDFmoyen[key]:
                TFIDFmoyencroissant[key] = TFIDFmoyen[key]
        maxdejatrouvee.append(max)
    return TFIDFmoyencroissant


def chiracSaidIt(TF):
    """
    renvoit les mots qu'a le plus dit Chirac avec leur occurence
    :param TF: dictionnaire de dictionnaire
    :return: Chirac_decroissant
    """
    Chirac_decroissant = {}
    Chirac = TF["Chirac1"]
    for mot in TF["Chirac2"]:
        if mot in Chirac:
            Chirac[mot] += TF["Chirac2"][mot]
        else:
            Chirac[mot] = TF["Chirac2"][mot]
# trie par ordre décroissant de récurrence des mots utilisés par Chirac
    maxdejatrouvee = []
    max = 0.1
    while max != 0:
        max = 0
        for value in Chirac.values():
            if max <= value and value not in maxdejatrouvee:
                max = value
        for key in Chirac.keys():
            if max == Chirac[key]:
                Chirac_decroissant[key] = Chirac[key]
        maxdejatrouvee.append(max)
    return Chirac_decroissant


def mot_nation(TFIDF):
    """
    Repère qui a dit le mot "nation" et le range dans une liste
    Affiche celui qui l'a le plus répété
    :param TFIDF: dictionnaire de dictionnaire
    :return: present
    """
    present = []
    recurrence = 0
    for key in TFIDF.keys() :
        for key2 in TFIDF[key].keys() :
            if key2 == "nation" and TFIDF[key][key2] != 0:
                present.append(key)
                if TFIDF[key][key2] >= recurrence:
                    recurrence = TFIDF[key][key2]
                    president = key
    print("le président qui a répété le plus de fois le mot 'nation' est", president)
    return present

def ecologie(TFIDF):
    """
    Repère qui a parlé de l'écologie et le range dans une liste
    :param TFIDF: dictionnaire de dictionnaire
    :return: listecologie
    """
    champ_lexical_ecologie = ["écologiste","environnement","écologique","écologisme","biodiversité","pollution","climat","écologie","développement durable","recyclage","biomasse","nature","végétale","climatique"]
    listecologie = []
    for key in TFIDF.keys() :
        for key2 in TFIDF[key].keys() :
            if key2 in champ_lexical_ecologie and TFIDF[key][key2] != 0:
                if key not in listecologie :
                    listecologie.append(key)
    return listecologie




def motsDisParTous(IDF):
    """
    permet de renvoyer tous les mots dis par tous les présidents dans une liste
    :param IDF: dictionnaire
    :return:
    """
    present_partout = []
    for key in IDF.keys():
        if IDF[key] == log(2, 10):
            present_partout.append(key)
    return present_partout



