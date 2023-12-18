from math import sqrt


def fct_liste_mot_question(question: str):
    """
    permet de renvoyer sous forme de liste les mots de la questions
    :param question: str
    :return: list
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


def fct_mot_question_present_dans_IDF(IDF: dict, motquestion: list):
    """
    On fait un trie pour garder seulement les mots présents dans IDF
    :param IDF: dict
    :param motquestion: list
    :return: list
    """
    mot_present = []
    for mot in motquestion:
        if mot in IDF.keys():
            mot_present.append(mot)
    return mot_present


def fct_TFIDF_question(mot_question_present: list, IDF: dict):
    """
    Calcul le TFIDF de chaque mot de la question
    :param mot_question_present: list
    :param IDF: dict
    :return: dict
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


def produit_scalaire(TF_IDFquest: dict, TF_IDFtot: dict):
    """
    Permet de calculer le produit scalaire de deux vecteurs
    :param TF_IDFquest: dict
    :param TF_IDFtot: dict
    :return: float
    """
    p_scalaire = 0
    for mot in TF_IDFquest.keys():
        p_scalaire += TF_IDFquest[mot] * TF_IDFtot[mot]
    return p_scalaire


def norme_vect(TF_IDF: dict):
    """
    Permet de calculer la norme d'un vecteur donné
    :param TF_IDF: dict
    :return: float
    """
    norme = 0
    for mot in TF_IDF.keys():
        norme += TF_IDF[mot]
    return sqrt(norme)


def similarite_vect(TF_IDFquest: dict, TF_IDFtot: dict, files: list, files_names: list):
    """
    Permet de renvoyer le document le plus similaire à la question posée
    :param TF_IDFquest: dict
    :param TF_IDFtot: dict
    :param files: list
    :param files_names: list
    :return: str
    """
    max_similarite_president = 0
    name_president_max = None
    mot_le_plus_important = fct_mot_question_plus_important(TF_IDFquest)
    for i in range(len(files)):
        if norme_vect(TF_IDFquest) != 0 and TF_IDFtot[files[i]][mot_le_plus_important] != 0:
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
    :param TFIDF_question: dict
    :return: str
    """
    maxi = 0
    mot_plus_important = ""
    for key in TFIDF_question.keys():
        if TFIDF_question[key] > maxi:
            maxi = TFIDF_question[key]
            mot_plus_important = key
    return mot_plus_important


def fct_debut_reponse(question, TFIDF_question):
    """
    permet d'initiliser le début de la réponse en fonction du type de question posé
    :param question: str
    :param TFIDF_question: dict
    :return: str
    """
    question_starters = {
        "comment": "Après analyse, ",
        "pourquoi": "Car, ",
        "peux-tu": "Oui, bien sûr!",
        "quelle": "En effet, ",
        "quel": "En effet, ",
        "que": "Cette question est très intéressante, "
    }
    mot = ""
    trouve = False
    for char in question:

        if char != " " and not trouve:
            if 64 < ord(char) < 91:
                mot += chr(ord(char) + 32)
            else:
                mot += char
        else:
            trouve = True
    if mot in question_starters.keys():
        if mot in TFIDF_question.keys():
            TFIDF_question[mot] = 0
        return question_starters[mot]
    else:
        return ""


def fct_reponse(mot_important: str, file: str, debut_reponse: str):
    """

    :param mot_important: str
    :param file: str
    :param debut_reponse: str
    :return: str
    """
    if file != None:
        with open("speeches/" + file, "r", encoding='utf-8') as f:
            mot = ""
            phrase = ""
            trouve = False
            phrasetrouve = False
            phrase_reponse = ""
            for line in f:
                for char in line:
                    if char != " " and char != "." and char != "?" and char != "!" and char != "\n" and char != "," and char != ":":
                        mot += char
                    else:
                        if char == "\n":
                            phrase += mot + ""
                        else:
                            phrase += mot + char
                        if len(mot) > 0:
                            motcorrige = ""
                            for i in range(len(mot)):
                                if 64 < ord(mot[i]) < 91:
                                    motcorrige += chr(ord(mot[i]) + 32)
                                else:
                                    motcorrige += mot[i]
                            if motcorrige == mot_important and not trouve:
                                trouve = True

                            mot = ""
                        if char == "." or char == "?" or char == "!":
                            if trouve and not phrasetrouve:
                                phrase_reponse = debut_reponse + phrase

                                phrasetrouve = True

                            phrase = ""
        return phrase_reponse
