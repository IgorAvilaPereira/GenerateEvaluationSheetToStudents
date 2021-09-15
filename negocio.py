from ezodf import newdoc, Paragraph, Heading, Sheet
import os
from pathlib import Path

class Aluno:
    def __init__(self, matricula, nome):
        self.matricula = matricula
        self.nome = nome  

class PlanilhaODS:
    def __init__(self):
        pass
    def gerar(self, vetAluno, qtde = 5):
        alfabeto = []
        c = 0
        d = 0
        for i in range(ord('A'), ord('Z')+1):
            alfabeto.insert(c, chr(i))
            for j in range(ord('A'), ord('Z')+1):
                d += 1
                alfabeto.insert(c+d, chr(i)+chr(j))
                for k in range(ord('A'), ord('Z')+1):
                    alfabeto.append(chr(i)+chr(j)+chr(k))
            c += 1
        if Path("planilha_avaliacao.ods").is_file():
            os.remove("planilha_avaliacao.ods")
        ods = newdoc(doctype='ods', filename='planilha_avaliacao.ods')
        sheet = Sheet('Alunos', size=(100, 100))
        ods.sheets += sheet
        sheet['A1'].set_value("Matricula")
        sheet['B1'].set_value("Nome")       
        j = 2
        while (j < qtde+2):
            sheet[0,j].set_value("Requisito"+str(j-1))               
            j = j + 1
        sheet[0, j].set_value("Total")        
        i = 1    
        for aluno in vetAluno:                     
            sheet[i,0].set_value(aluno.matricula)
            sheet[i,1].set_value(aluno.nome)
            j = 2
            while (j < qtde+2):
                sheet[i,j].set_value(0)
                j = j + 1
            sheet[i, j].formula = "of:=SUM(C"+str(i+1)+":"+alfabeto[j-1]+str(i+1)+")"
            i = i + 1        
        ods.save()
        # os.system("libreoffice planilha_avaliacao.ods")