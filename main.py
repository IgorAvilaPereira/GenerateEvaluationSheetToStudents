import sys
from negocio import PlanilhaODS
from persistencia import AlunoDAO

if __name__ == '__main__':
    alunoDAO = AlunoDAO()        
    vetAluno = alunoDAO.listarCSV("students.csv")        
    qtde = None
    if len(sys.argv) > 1:   
        qtde = sys.argv[1]        
    planilha = PlanilhaODS()    
    if qtde is None:        
        planilha.gerar(vetAluno)
    else:
        planilha.gerar(vetAluno, int(qtde))