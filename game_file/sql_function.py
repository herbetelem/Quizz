# coding : utf-8

# import de la librairie
import sqlite3

# * Fonction pour recuperer depuis la bdd

class SQL_request:
    
    def __init__(self):
        # * connection a la bdd
        self.connection = sqlite3.connect("quizz.db")
        # * instance du curseur
        self.cursor = self.connection.cursor()

    def read_question(self, id_question):
        # * je definit quelle id de question je vais chercher
        id_question = (id_question,)
        # * je créer la requete
        self.cursor.execute('SELECT * FROM hh_quizz WHERE id = ?', id_question)
        # * je formate en tuple ma reponse
        self.question_tmp = self.cursor.fetchone()

    def read_answer(self, id_question):
        # * je definit quelle id de question je vais chercher
        id_question = (id_question,)
        # * je créer la requete
        self.cursor.execute('SELECT * FROM hh_answer WHERE id_question = ?', id_question)
        # * je formate en tuple mes reponses
        self.anwser_tmp = self.cursor.fetchall()


    def read_score(self):
        # * je créer la requete
        self.cursor.execute('SELECT * FROM hh_score ORDER BY score DESC')
        # * je formate en tuple mes reponses
        self.score_tmp = self.cursor.fetchall()