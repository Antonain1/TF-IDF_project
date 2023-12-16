from math import sqrt


def fct_liste_mot_question(question):
    question_corrigé = ""
    for char in question:

        if 64 < ord(char) < 91:
            question_corrigé += chr(ord(char) + 32)
        elif char == ":" or char == "." or char == "!" or char == "?" or char == "," or char == ";" or char == chr(
                34) or char == "-" or char == "'":
            question_corrigé += " "
        else:
            question_corrigé += char
    liste_mot_question = question_corrigé.split(" ")
    liste_mot_question2 = []
    for mot in liste_mot_question:
        if mot != "":
            liste_mot_question2.append(mot)
    return liste_mot_question2


def fct_mot_question_present_dans_IDF(IDF, motquestion):
    mot_present = []
    for mot in motquestion:
        if mot in IDF.keys():
            mot_present.append(mot)
    return mot_present


def fct_TFIDF_question(mot_question_present, IDF):
    TFquestion = {}
    TFIDFquestion = {}
    for mot in mot_question_present:
        if mot in TFquestion:
            TFquestion[mot] += 1
        else:
            TFquestion[mot] = 1
    for key in TFquestion.keys():
        TFIDFquestion[key] = TFquestion[key] * IDF[key]
    return TFIDFquestion


def produit_scalaire(TF_IDFquest, TF_IDFtot):
    p_scalaire = 0
    for mot in TF_IDFquest.keys():
        p_scalaire += TF_IDFquest[mot] * TF_IDFtot[mot]
    return p_scalaire


def norme_vect(TF_IDF):
    norme = 0
    for mot in TF_IDF.keys():
        norme += TF_IDF[mot]
    return sqrt(norme)


def similarite_vect(TF_IDFquest, TF_IDFtot, files, files_names):
    max_similarite_president = 0
    name_president_max = None
    for i in range(len(files)):
        if norme_vect(TF_IDFquest) != 0:
            similarite_president = produit_scalaire(TF_IDFquest, TF_IDFtot[files[i]]) / (
                        norme_vect(TF_IDFquest) * norme_vect(TF_IDFtot[files[i]]))
            if similarite_president > max_similarite_president:
                max_similarite_president = similarite_president
                name_president_max = files_names[i]
    if max_similarite_president == 0:
        print("aucune similarité")
    return name_president_max


def fct_mot_question_plus_important(TFIDF_question):
    max = 0
    mot_plus_important = ""
    for key in TFIDF_question.keys():
        if TFIDF_question[key] > max:
            max = TFIDF_question[key]
            mot_plus_important = key
    return mot_plus_important


def fct_reponse(mot_important, file):
    with open("speeches/" +file, "r") as f:
        mot = ""
        phrase = ""
        trouve=False
        phrasetrouve = False
        phrase_reponse = ""
        for line in f:
            for char in line:
                if char != " " and char != "." and char != "?" and char != "!" and char != "\n":
                    mot += char
                else:
                    phrase += mot + " "
                    if mot == mot_important and trouve==False:
                        trouve = True

                    mot = ""
                    if char == "." or char == "?" or char == "!":
                        if trouve == True and phrasetrouve==False:

                            phrase_reponse = phrase

                            phrasetrouve = True

                        phrase = ""
    return phrase_reponse