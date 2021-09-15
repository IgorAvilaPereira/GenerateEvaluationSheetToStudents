# import tkinter as  # for Python 3 version
from tkinter import *
from tkinter import messagebox
from negocio import PlanilhaODS
from persistencia import AlunoDAO

class Janela:
	def __init__(self):
		self.top = Tk()
		self.scrollbar = Scrollbar(self.top, orient="vertical")		
		self.label = Label(self.top, text="Qtde:")
		v = StringVar(self.top, value='5')
		self.entry = Entry(self.top, bd = 5, textvariable=v)
		self.button = Button(self.top, text="Gerar", command=self.gerar)
		self.label.pack()
		self.entry.pack()
		self.button.pack()	
		self.top.mainloop()

	def gerar(self):	
		qtde = self.entry.get()
		alunoDAO = AlunoDAO()
		vetAluno = alunoDAO.listarCSV("students.csv")	
		planilha = PlanilhaODS()				
		if qtde is None or len(qtde) == 0:        
			planilha.gerar(vetAluno)
		else:
			qtde = int(qtde)	
			planilha.gerar(vetAluno, int(qtde))
		messagebox.showinfo("Gerar Planilha", "Planilha Gerada com Sucesso!")

if __name__ == '__main__':
    janela = Janela()