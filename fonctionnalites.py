from math import *


def motsDisParTous(IDF: dict):
    """
    permet de renvoyer tous les mots dis par tous les présidents dans une liste
    :param IDF: dict
    :return: list
    """
    present_partout = []
    for key in IDF.keys():
        if IDF[key] == 0:
            present_partout.append(key)
    return present_partout


def moyenne(TFIDF: dict):
    """
    permet de faire la moyenne de tous les TF-IDF
    :param TFIDF: dict
    :return: dict
    """
    TFIDFmoyen = {}
    for mot in TFIDF["Chirac1"].keys():
        moyenne = 0
        for key in TFIDF.keys():
            moyenne += TFIDF[key][mot] / 8
        TFIDFmoyen[mot] = moyenne
    return TFIDFmoyen


def plusimportant(TFIDFmoyen: dict):
    """
    renvoie le mot du plus important au moins important
    :param TFIDFmoyen: dict
    :return: dict
    """
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


# Cette fonction avait pour but de renvoyer le mot le plus important au mot le plus important. Mais après changement il n'a plus aucune utilité.


"""
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
"""


def chiracSaidIt(TF: dict, mot_dit_par_tous: list):
    """
    renvoit les mots qu'a le plus dit Chirac avec leur occurrence
    :param TF: dict
    :param mot_dit_par_tous: list
    :return: dict
    """
    Chirac_decroissant = {}
    Chirac = {}
    for mot in TF["Chirac1"]:
        if mot not in mot_dit_par_tous:
            Chirac[mot] = TF["Chirac1"][mot]
    for mot in TF["Chirac2"]:
        if mot not in mot_dit_par_tous:
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


def mot_nation(TFIDF: dict):
    """
    Repère qui a dit le mot "nation" et le range dans une liste
    Affiche celui qui l'a le plus répété
    :param TFIDF: dict
    :return: list
    """
    present = []
    recurrence = 0
    for key in TFIDF.keys():
        for key2 in TFIDF[key].keys():
            if key2 == "nation" and TFIDF[key][key2] != 0:
                present.append(key)
                if TFIDF[key][key2] >= recurrence:
                    recurrence = TFIDF[key][key2]
                    president = key
    print("le président qui a répété le plus de fois le mot 'nation' est", president)
    return present


def ecologie(TFIDF: dict):
    """
    Repère qui a parlé de l'écologie et le range dans une liste
    :param TFIDF: dict
    :return: list
    """
    champ_lexical_ecologie = ["écologiste", "environnement", "écologique", "écologisme", "biodiversité", "pollution",
                              "climat", "écologie", "développement durable", "recyclage", "biomasse", "nature",
                              "végétale", "climatique"]
    listecologie = []
    for key in TFIDF.keys():
        for key2 in TFIDF[key].keys():
            if key2 in champ_lexical_ecologie and TFIDF[key][key2] != 0:
                if key not in listecologie:
                    listecologie.append(key)
    return listecologie


def mot_evoque_pas_par_tous(IDF: dict):
    """
    permet d'avoir la liste des mots pas dis par tous les présidents
    :param IDF: dict
    :return: list
    """
    present_pas_partout = []
    for key in IDF.keys():
        if IDF[key] != 0:
            present_pas_partout.append(key)
    return present_pas_partout
