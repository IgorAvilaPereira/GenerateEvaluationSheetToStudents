# import psycopg2
import csv
from negocio import Aluno

class AlunoDAO:
    def __init__(self):
        pass
    def listarCSV(self, nome_arquivo):
        vet = []
        with open(nome_arquivo) as csvfile:
            spamreader = csv.reader(csvfile, delimiter=';')        
            for row in spamreader:                
                vet.append(Aluno(row[0], row[1]))
        return vet