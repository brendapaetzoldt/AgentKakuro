import re
import time
import tabuleiros
from resolucoes import *
from utils import *

class Kakuro(CSP):
    def __init__(self, tabuleiro):
        self.tabuleiro = tabuleiro
        self.tamanhoLinha = len(tabuleiro)
        self.tamanhoColuna = len(tabuleiro[0])
        self.vars = self.getVar()
        self.dominios = self.getDominio()
        self.vizinhos = self.getVizinhos()
        self.soma = self.getSoma()
        self.restricoes = self.getRestricoes
        CSP.__init__(self, self.vars, self.dominios, self.vizinhos, self.restricoes)

    def getVar(self):
        vars = []
        for i, linha in enumerate(self.tabuleiro):
            for j, cell in enumerate(linha):
                if cell == 'W':
                    vars.append('x' + '_' + str(i) + '_' + str(j))
        return vars

    def getDominio(self):
        dominios = {}
        for var in self.vars:
            dominios[var] = []
            for i in range(1,10):
                dominios[var].append(i)
        return dominios

    def getVizinhos(self):
        vizinhos = {}
        for var in self.vars:
            vizinhos[var] = []
            linha = int(re.search('_(.*)_', var).group(1))
            coluna = int(var.rsplit('_', 1)[-1])
            for i in range(self.tamanhoColuna):
                if i < coluna - 1 or i > coluna + 1:
                    continue
                if isinstance(self.tabuleiro[linha][i], str):
                    if self.tabuleiro[linha][i] == 'W':
                        varVizinho = 'x' + '_' + str(linha) + '_' + str(i)
                        if varVizinho in self.vars and varVizinho != var:
                            vizinhos[var].append(varVizinho)
            for i in range(self.tamanhoLinha):
                if i < linha -1 or i > linha + 1:
                    continue
                if isinstance(self.tabuleiro[i][coluna], str):
                    if self.tabuleiro[i][coluna] == 'W':
                        varVizinho = 'x' + '_' + str(i) + '_' + str(coluna)
                        if varVizinho in self.vars and varVizinho != var:
                            vizinhos[var].append(varVizinho)
        return vizinhos

    def getRestricoes(self, A, a, B, b):
        if a == b:
            return False
        assignment = self.infer_assignment()
        for var in self.vizinhos[A]:
            if var in assignment:
                if assignment[var] == a:
                    return False
        for var in self.vizinhos[B]:
            if var in assignment:
                if assignment[var] == b:
                    return False
        for soma in self.soma:
            if (A in soma[1]) and (B in soma[1]):
                somaVizinhos = 0
                atribuirVizinhos = 0
                for var in soma[1]:
                    if var in assignment:
                        if (var != A) and (var != B):
                            somaVizinhos += assignment[var]
                            atribuirVizinhos += 1
                somaVizinhos += a + b
                atribuirVizinhos += 2
                if (len(soma[1]) > atribuirVizinhos) and (somaVizinhos >= soma[0]):
                    return False
                if (len(soma[1]) == atribuirVizinhos) and (somaVizinhos != soma[0]):
                    return False

        for soma in self.soma:
            if (A in soma[1]) and (B not in soma[1]):
                somaVizinhos = 0
                atribuirVizinhos = 0
                for var in soma[1]:
                    if var in assignment:
                        if var != A:
                            somaVizinhos += assignment[var]
                            atribuirVizinhos += 1
                somaVizinhos += a
                atribuirVizinhos += 1
                if (len(soma[1]) > atribuirVizinhos) and (somaVizinhos >= soma[0]):
                    return False
                if (len(soma[1]) == atribuirVizinhos) and (somaVizinhos != soma[0]):
                    return False

        for soma in self.soma:
            if (A not in soma[1]) and (B in soma[1]):
                somaVizinhos = 0
                atribuirVizinhos = 0
                for var in soma[1]:
                    if var in assignment:
                        if var != B:
                            somaVizinhos += assignment[var]
                            atribuirVizinhos += 1
                somaVizinhos += b
                atribuirVizinhos += 1
                if (len(soma[1]) > atribuirVizinhos) and (somaVizinhos >= soma[0]):
                    return False
                if (len(soma[1]) == atribuirVizinhos) and (somaVizinhos != soma[0]):
                    return False
        return True

    def getSoma(self):
        soma = []
        for i, linha in enumerate(self.tabuleiro):
            for j, cell in enumerate(linha):
                if (cell != 'W' and cell != 'B'):
                    if (cell[0] != ''):
                        x = []
                        for k in range(i + 1, self.tamanhoLinha):
                            if (self.tabuleiro[k][j] != 'W'):
                                break
                            x.append('x' + '_' + str(k) + '_' + str(j))
                        soma.append((cell[0], x))
                    if (cell[1] != ''):
                        x = []
                        for k in range(j + 1, len(self.tabuleiro[i])):
                            if (self.tabuleiro[i][k] != 'W'):
                                break
                            x.append('x' + '_' + str(i) + '_' + str(k))
                        soma.append((cell[1], x))
        return soma

    def BT(self):
        start = time.time()
        result = backtrack(self)
        end = time.time()
        return (result, end - start)

    def BT_MRV(self):
        start = time.time()
        result = backtrack(self, valsNAtribuidas=minValRestantes)
        end = time.time()
        return (result, end - start)

    def grid(self, grid):
        for i in range(self.tamanhoColuna):
            for j in range(self.tamanhoColuna):
                if isinstance(self.tabuleiro[i][j], list):
                    if grid[i][j][0] == '':
                        print('B\{}'.format(grid[i][j][1]).ljust(4), end='\t')
                    elif grid[i][j][1] == '':
                        print('{}\B'.format(grid[i][j][0]).ljust(4), end='\t')
                    else:
                        print('{}\{}'.format(grid[i][j][0], grid[i][j][1]).ljust(4), end='\t')
                else:
                    print(grid[i][j].ljust(4), end='\t')
            print()

    def aSolucao(self, grid, solucao, tempo, assigns):
        if solucao != None:
            for var in self.vars:
                linha = int(re.search('_(.*)_', var).group(1))
                coluna = int(var.rsplit('_', 1)[-1])
                value = solucao[var]
                grid[linha][coluna] = str(value)
            self.grid(grid)
            print("Quantidade de atribuições/assigns: {}".format(assigns))
            print("Tempo decorrido para a solução: {:.4f} segundos".format(tempo))
        else:
            print("Não foi possível encontrar uma solução")

if __name__ == "__main__":
    tabuleirosKakuro = []
    for item in vars(tabuleiros).keys():
        if not item.startswith("__"):
            tabuleirosKakuro.append((item,vars(tabuleiros)[item]))
    for tamanhoTabuleiro, tabuleiro in tabuleirosKakuro:
        print("\n____________________________Tabuleiro {}_______________________________".format(tamanhoTabuleiro))
        kakuro = Kakuro(tabuleiro)
        print("\n> Backtracking")
        kakuro.aSolucao(kakuro.tabuleiro, *kakuro.BT(), kakuro.nassigns)
        print("\n> Backtracking e Valores Mínimos Rrestantes (MRV)")
        kakuro.aSolucao(kakuro.tabuleiro, *kakuro.BT_MRV(), kakuro.nassigns)
        print()
