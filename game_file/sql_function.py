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
        id_question = (id_question,)
        self.cursor.execute('SELECT * FROM hh_quizz WHERE id = ?', id_question)
        self.question_tmp = self.cursor.fetchone()

    def read_answer(self, id_question):
        id_question = (id_question,)
        self.cursor.execute('SELECT * FROM hh_answer WHERE id_question = ?', id_question)
        self.anwser_tmp = self.cursor.fetchall()


    def read_score(self):
            self.cursor.execute('SELECT * FROM hh_score')
            self.score_tmp = self.cursor.fetchall()