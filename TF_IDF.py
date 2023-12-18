from math import *


def president_names_fichier(L: list, A: list):
    """
    permet d'obtenir une liste des noms des présidents
    :param L: list
    :param A: list
    :return: /
    """
    for i in range(len(L)):
        A.append(L[i][11:-4])


def dico_mot_presidents(L: list):
    """
    crée un dictionnaire de dictionnaire contenant les noms des présidents contenus dans speeches
    :param L: list
    :return: dict
    """
    dico = {}
    for i in range(len(L)):
        dico[L[i]] = {}
    return dico


def TF(occurrence: dict, files: list, presidentnum: list):
    """
    TF par récurrence
    :param occurrence: dict
    :param files: list
    :param presidentnum: list
    :return: dict
    """
    for i in range(len(files)):
        with open("cleaned/" + files[i], "r", encoding='utf-8') as f:
            mot = ""
            for line in f:
                for char in line:
                    if char != " " and char != "\n":
                        mot += char
                    else:
                        if mot in occurrence[presidentnum[i]]:
                            occurrence[presidentnum[i]][mot] += 1

                        else:
                            occurrence[presidentnum[i]][mot] = 1

                        mot = ""
        for key in occurrence[presidentnum[i]].keys():
            if key == '':
                del occurrence[presidentnum[i]][key]
                break

    return occurrence


def IDF(occurrence: dict):
    """
    permet de renvoyer l'IDF de chaque mot en se basant sur la formule donnée
    :param occurrence: dict
    :return: dict
    """
    IDFdict = {}
    for key in occurrence:
        for mot in occurrence[key].keys():
            if mot not in IDFdict:
                IDFdict[mot] = 1
            else:
                IDFdict[mot] += 1
    for key in IDFdict.keys():
        IDFdict[key] = log((8 / IDFdict[key]), 10)
    return IDFdict


def TF_IDF(TF: dict, IDF: dict):
    """
    permet de faire le TF-IDF en utilisant TF et IDF
    :param TF: dict
    :param IDF: dict
    :return: dict
    """
    TFIDF = TF
    TFIDFtriee = TF
    for key in TF:
        for mot in IDF.keys():
            trouve = False
            for val in TF[key].keys():
                if mot == val:
                    trouve = True
                    break
            if trouve:
                TFIDF[key][mot] = TF[key][val] * IDF[mot]

            else:
                TFIDF[key][mot] = 0
    # Trie de TFIDF
    for key in TFIDF:
        sorted_tfkeys = sorted(TFIDF[key].keys())
        sorted_TFIDF = {}
        for mot in sorted_tfkeys:
            sorted_TFIDF[mot] = TFIDF[key][mot]
        TFIDFtriee[key] = sorted_TFIDF
    return TFIDFtriee
