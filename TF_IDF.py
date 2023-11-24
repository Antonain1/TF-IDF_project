from math import *
def president_names_fichier(L, A):
    for i in range(len(L)):
        A.append(L[i][11:-4])


def TF(occurence, files, presidentnum):
    for i in range(len(files)):
        with open("cleaned/" + files[i], "r", encoding='utf-8') as f:
            mot = ""
            for line in f:
                for char in line:
                    if char != " " and char != "\n":
                        mot += char
                    else:
                        if mot in occurence[presidentnum[i]]:
                            occurence[presidentnum[i]][mot] += 1

                        else:
                            occurence[presidentnum[i]][mot] = 1

                        mot = ""
        for key in occurence[presidentnum[i]].keys() :
            if key == '' :
                del occurence[presidentnum[i]][key]
                break


def IDF(occurence) :
    IDFdict = {}
    for key in occurence :
        for mot in occurence[key].keys() :
            if mot not in IDFdict :
                IDFdict[mot] = 1
            else :
                IDFdict[mot] += 1
    for key in IDFdict.keys() :
        IDFdict[key] = log ((8/IDFdict[key])+1,10)
    return IDFdict

def TF_IDF(TF,IDF,name_dict) :
    TFIDF = name_dict
    for key in TF:
        for mot in IDF.keys() :
            trouve = False
            for val in TF[key].keys():
                if mot == val :
                    trouve = True
                    break
            if trouve == True :
                TFIDF[key][mot] = TF[key][val] * IDF[mot]

            else :
                TFIDF[key][mot] = 0
    return TFIDF