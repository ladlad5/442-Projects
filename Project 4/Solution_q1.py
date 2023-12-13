
class CPT:
    def __init__(self, name, table, variables, parents=None, children=None):
        self.name = name
        self.parents = parents
        self.table = table
        self.children = children
        self.variables = variables
ExpectedPoss = {"john": [True, False], "mary": [True, False], "alarm": [True, False], "burglary": [True, False], "earthquake": [True ,False]}   
def assign(assigned, tba, poss):
    assignments = []
    if len(tba) == 0:
        assignments.append(assigned)
        return [tuple(assigned.values())]
    else:
        for p in poss[tba[0]]:
            assignments += assign(dict(list(assigned.items()) + list({tba[0]: p}.items())), tba[1:], poss)
    return(assignments)

poss = { "A": [True, False], "B": [1, 2, 3], "C": ["c"]} #test input/output for assign()
expected = [{'A': True, 'B': 1, 'C': 'c'}, {'A': True, 'B': 2, 'C': 'c'}, {'A': True, 'B': 3, 'C': 'c'}, {'A': False, 'B': 1, 'C': 'c'}, {'A': False, 'B': 2, 'C': 'c'}, {'A': False, 'B': 3, 'C': 'c'}]
#assert expected == assign({}, list(poss.keys()), poss), assign({}, list(poss.keys()), poss)


def makeFactor(var, evidence, factors):
    factor = var
    factors.append(factor)
    return factors

def sumOut(var, factors):
    pass

def pointWiseProd(var, factors):
    #make an expectedposs subdictionary from the master using variable names from factors
    subExpectedPoss = {}
    factorNames = []
    '''for x in factors:
        for factor in factors:
            factorNames.append(factor.name)
            for h in factor.variables:
                if h in ExpectedPoss and h not in subExpectedPoss:
                    subExpectedPoss[h] = ExpectedPoss[h]'''
    for factor in factors:
        factorNames.append(factor.name)
        for h in factor.variables:
            if h in ExpectedPoss and h not in subExpectedPoss:
                subExpectedPoss[h] = ExpectedPoss[h]
    pointWiseAssignment = assign({}, list(subExpectedPoss.keys()), subExpectedPoss)
    varOrder = list(subExpectedPoss.keys())
    newCPT = {}
    for assignment in pointWiseAssignment:
        #make a dictionary with key of the variable name and a value of the truth table assertion(true/false)
        auxDic = {}
        for x in varOrder:
            auxDic[x] = assignment[varOrder.index(x)]
        probProduct = 1
        for factor in factors:
            lookupTup = []
            for variable in factor.variables:
                lookupTup.append(auxDic[variable])
            lookupTup = tuple(lookupTup)
            #with lookupTup find the desired row in the CPT table
            probProduct *= factor.table[lookupTup]
        newCPT[assignment + (True,)] = probProduct
        newCPT[assignment + (False,)] = 1 - probProduct
    newName = "*"
    newName = newName.join(factorNames)
    return CPT(newName,
               newCPT,varOrder + [newName], factors[0].parents,factors[0].children)# create new CPT
        
            

    pass
pointWiseExample = [
    CPT("john", {
        (True,True): 0.9,
        (True, False): 0.1,
        (False,True): 0.05,
        (False, False): 0.95
    },["alarm", "john"], ["alarm"]),
    CPT("mary", {
        (True, True): 0.7,
        (True, False): 0.3,
        (False, True): 0.01,
        (False, False): 0.99
    },["alarm", "mary"], ["alarm"]),
]
PWExpectedPoss = {"john": [True, False], "mary": [True, False], "alarm": [True, False]}
PWExpectedAssignments = assign({}, list(PWExpectedPoss.keys()), PWExpectedPoss)
#print(PWExpectedAssignments)

PWExpected = CPT("john*mary",{
    (True, True, True): 0.9*0.7, (True, True, False): 0.05*0.01, (True, False, True): 0.9*0.3, (True, False, False):0.05*0.99, 
    (False, True, True): 0.1*0.7, (False, True, False): 0.95*0.01, (False, False, True):0.1*0.3, (False, False, False):0.95*0.99
}, ["john", "mary", "alarm", "john*mary"])
print(pointWiseProd(None, pointWiseExample).table)

def varElim(X, e, bn):
    factors = []
    for var in bn:
        factors = makeFactor(bn[var], e, bn)
        if (not var.name == query or not var.name in e):
            factors = sumOut(bn[var], factors)
    pass




bayesNet = { #Manually ordered for this test case
    "john": CPT("john", {
        (True,True): 0.9,
        (True, False): 0.1,
        (False,True): 0.05,
        (False, False): 0.95
    },["alarm", "john"], ["alarm"]),
    "mary": CPT("mary", {
        (True, True): 0.7,
        (True, False): 0.3,
        (False, True): 0.01,
        (False, False): 0.99
    },["alarm", "mary"], ["alarm"]),
    "alarm": CPT("alarm", {
        (True, True, True): 0.95,
        (True, True, False): 0.05,
        (True, False, True): 0.94,
        (True, False, False): 0.06,
        (False, True, True): 0.29,
        (False, True, False): 0.71,
        (False, False, True): 0.001,
        (False, False, False): 0.999,
    },["burglary", "earthquake", "alarm"],["burglary", "earthquake"], ["john", "mary"]),
    "burglary": CPT("burglary", {
        (True,): 0.001,
        (False,): 0.999
    },["burglary"],None,["alarm"]),
    "earthquake": CPT("earthquake",{
        (True,): 0.002,
        (False,): 0.998
    },["earthquake"],None,["alarm"])
}
query = "burglary"
evidence = {
    "john": True
}
#varElim(query, evidence, bayesNet)