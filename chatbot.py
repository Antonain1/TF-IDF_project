from math import sqrt


def fct_liste_mot_question(question):
    """
    permet de renvoyer sous forme de liste les mots de la questions
    :param question:
    :return:
    """
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
    """
    On fait un trie pour garder seulement les mots présents dans IDF
    :param IDF:
    :param motquestion:
    :return:
    """
    mot_present = []
    for mot in motquestion:
        if mot in IDF.keys():
            mot_present.append(mot)
    return mot_present


def fct_TFIDF_question(mot_question_present, IDF):
    """
    Calcul le TFIDF de chaque mot de la question
    :param mot_question_present:
    :param IDF:
    :return:
    """
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
    """
    Permet de calculer le produit scalaire de deux vecteurs
    :param TF_IDFquest:
    :param TF_IDFtot:
    :return:
    """
    p_scalaire = 0
    for mot in TF_IDFquest.keys():
        p_scalaire += TF_IDFquest[mot] * TF_IDFtot[mot]
    return p_scalaire


def norme_vect(TF_IDF):
    """
    Permet de calculer la norme d'un vecteur donné
    :param TF_IDF:
    :return:
    """
    norme = 0
    for mot in TF_IDF.keys():
        norme += TF_IDF[mot]
    return sqrt(norme)


def similarite_vect(TF_IDFquest, TF_IDFtot, files, files_names):
    """
    Permet de renvoyer le document le plus similaire à la question posée
    :param TF_IDFquest:
    :param TF_IDFtot:
    :param files:
    :param files_names:
    :return:
    """
    max_similarite_president = 0
    name_president_max = None
    mot_le_plus_important = fct_mot_question_plus_important(TF_IDFquest)
    for i in range(len(files)):
        if norme_vect(TF_IDFquest) != 0 and mot_le_plus_important in TF_IDFtot[files[i]].keys():
            similarite_president = produit_scalaire(TF_IDFquest, TF_IDFtot[files[i]]) / (
                        norme_vect(TF_IDFquest) * norme_vect(TF_IDFtot[files[i]]))
            if similarite_president > max_similarite_president:
                max_similarite_president = similarite_president
                name_president_max = files_names[i]
    if max_similarite_president == 0:
        print("aucune similarité")
    return name_president_max


def fct_mot_question_plus_important(TFIDF_question):
    """
    Permet de savoir quel est le mot le plus important dans la question
    :param TFIDF_question:
    :return:
    """
    maxi = 0
    mot_plus_important = ""
    for key in TFIDF_question.keys():
        if TFIDF_question[key] > maxi:
            maxi = TFIDF_question[key]
            mot_plus_important = key
    return mot_plus_important


def fct_reponse(mot_important: str, file: str):
    """
    Permet de renvoyer un phrase réponse à la question posée
    :param mot_important:
    :param file:
    :return:
    """
    with open("speeches/" + file, "r", encoding='utf-8') as f:
        mot = ""
        phrase = ""
        trouve = False
        phrasetrouve = False
        phrase_reponse = ""
        for line in f:
            for char in line:
                if char != " " and char != "." and char != "?" and char != "!" and char != "\n":
                    mot += char
                else:
                    phrase += mot + " "
                    if len(mot) > 1 :
                        if ((mot[0] == chr(ord(mot_important[0]) - 32) and mot[1:] == mot_important[1:]) or mot == mot_important) and not trouve:
                            trouve = True

                        mot = ""
                    if char == "." or char == "?" or char == "!":
                        if trouve and not phrasetrouve:

                            phrase_reponse = phrase

                            phrasetrouve = True

                        phrase = ""
    return phrase_reponse