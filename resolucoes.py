from utils import argMin, soma, primeira

class CSP():
    def __init__(self, var, dominio, vizinhos, restricao):
        var = var or list(dominio.keys())
        self.var = var
        self.dominio = dominio
        self.vizinhos = vizinhos
        self.restricao = restricao
        self.initial = ()
        self.domatual = None
        self.nassigns = 0

    def assign(self, var, val, assignment):
        assignment[var] = val
        self.nassigns += 1

    def unassign(self, var, assignment):
        if var in assignment:
            del assignment[var]

    def nconflitos(self, var, val, assignment):
        def conflito(var2):
            return (var2 in assignment and
                    not self.restricao(var, val, var2, assignment[var2]))
        return soma(conflito(v) for v in self.vizinhos[var])
  
    def testeobjetivo(self, estado):
        assignment = dict(estado)
        return (len(assignment) == len(self.var)
                and all(self.nconflitos(var, assignment[var], assignment) == 0
                        for var in self.var))

    def spoda(self):
        if self.domatual is None:
            self.domatual = {v: list(self.dominio[v]) for v in self.var}

    def suposicao(self, var, value):
        self.spoda()
        removedor = [(var, a) for a in self.domatual[var] if a != value]
        self.domatual[var] = [value]
        return removedor

    def poda(self, var, value, removedor):
        self.domatual[var].remove(value)
        if removedor is not None:
            removedor.append((var, value))

    def escolhas(self, var):
        return (self.domatual or self.dominio)[var]

    def infer_assignment(self):
        self.spoda()
        return {v: self.domatual[v][0]
                for v in self.var if 1 == len(self.domatual[v])}

    def restaura(self, removedor):
        for B, b in removedor:
            self.domatual[B].append(b)

def arcConsistencyAlgorithm3(csp, fila=None, removedor=None):
    if fila is None:
        fila = [(XX, Xk) for XX in csp.var for Xk in csp.vizinhos[XX]]
    csp.spoda()
    while fila:
        (XX, XY) = fila.pop()
        if verificarRemocao(csp, XX, XY, removedor):
            if not csp.domatual[XX]:
                return False
            for Xk in csp.vizinhos[XX]:
                if Xk != XX:
                    fila.append((Xk, XX))
    return True

def verificarRemocao(csp, XX, XY, removedor):
    verificada = False
    for x in csp.domatual[XX][:]:
        if all(not csp.restricao(XX, x, XY, y) for y in csp.domatual[XY]):
            csp.poda(XX, x, removedor)
            verificada = True
    return verificada

def varNAtribuida(assignment, csp):
    return primeira([var for var in csp.var if var not in assignment])

def minValRestantes(assignment, csp):
    return argMin(
        [v for v in csp.var if v not in assignment],
        key=lambda var: numVal(csp, var, assignment))

def numVal(csp, var, assignment):
        return soma(csp.nconflitos(var, val, assignment) == 0
                     for val in csp.dominio[var])

def domVals(var, assignment, csp):
    return csp.escolhas(var)

def inferencia(csp, var, value, assignment, removedor):
    return True

def verificacao(csp, var, value, assignment, removedor):
    "Prune neighbor values inconsistent with var=value."
    for B in csp.vizinhos[var]:
        if B not in assignment:
            for b in csp.domatual[B][:]:
                if not csp.restricao(var, value, B, b):
                    csp.poda(B, b, removedor)
            if not csp.domatual[B]:
                return False
    return True

def MaintainArcConsistency(csp, var, value, assignment, removedor):
    return arcConsistencyAlgorithm3(csp, [(X, var) for X in csp.vizinhos[var]], removedor)

def backtrack(csp,
                        valsNAtribuidas=varNAtribuida,
                        OrdemDomVals=domVals,
                        aInferencia=inferencia):
   
    def backtrack(assignment):
        if len(assignment) == len(csp.var):
            return assignment
        var = valsNAtribuidas(assignment, csp)
        for value in OrdemDomVals(var, assignment, csp):
            if 0 == csp.nconflitos(var, value, assignment):
                csp.assign(var, value, assignment)
                removedor = csp.suposicao(var, value)
                if aInferencia(csp, var, value, assignment, removedor):
                    resultado = backtrack(assignment)
                    if resultado is not None:
                        return resultado
                csp.restaura(removedor)
        csp.unassign(var, assignment)
        return None

    resultado = backtrack({})
    assert resultado is None or csp.testeobjetivo(resultado)
    return resultado
