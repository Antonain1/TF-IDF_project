from math import *


def president_names_fichier(L, A):
    for i in range(len(L)):
        A.append(L[i][11:-4])


def dico_mot_presidents(L):
    """
    crée un dictionnaire de dictionnaire contenant les noms des présidents contenus dans speeches
    :param L: liste
    :return: dico
    """
    dico = {}
    for i in range(len(L)):
        dico[L[i]] = {}
    return dico


def TF(occurence, files, presidentnum):
    for i in range(len(files)):
        #nombredemot = 0
        with open("cleaned/" + files[i], "r", encoding='utf-8') as f:
            mot = ""
            for line in f:
                for char in line:
                    if char != " " and char != "\n":
                        mot += char
                    else:
                        if mot in occurence[presidentnum[i]]:
                            occurence[presidentnum[i]][mot] += 1
                            #nombredemot+=1

                        else:
                            occurence[presidentnum[i]][mot] = 1
                            #nombredemot+=1

                        mot = ""
        for key in occurence[presidentnum[i]].keys():
            if key == '':
                del occurence[presidentnum[i]][key]
                #nombredemot -= 1
                break
        """
        for key in occurence[presidentnum[i]].keys():
            occurence[presidentnum[i]][key] = occurence[presidentnum[i]][key] /nombredemot
        """
    return occurence


def IDF(occurence):
    IDFdict = {}
    for key in occurence:
        for mot in occurence[key].keys():
            if mot not in IDFdict:
                IDFdict[mot] = 1
            else:
                IDFdict[mot] += 1
    for key in IDFdict.keys():
        IDFdict[key] = log((8 / IDFdict[key]), 10)
    return IDFdict


def TF_IDF(TF, IDF):
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