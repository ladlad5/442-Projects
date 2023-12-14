from collections import defaultdict
class CPT:
    def __init__(self, name, table, variables, parents=None, children=None):
        self.name = name
        self.parents = parents
        self.table = table
        self.children = children
        self.variables = variables
ExpectedPoss = {"john": [True, False], "mary": [True, False], "alarm": [True, False], "burglary": [True, False], "earthquake": [True ,False]}   
ExpectedPoss = defaultdict(lambda: [True, False])
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


def makeFactor(var, evidence, factors, hidden,query):
    if var.name in evidence:
        varIndex = var.variables.index(var.name)
        newDict = {}
        for entry in var.table:
            if entry[1] == evidence[var.name]:
                newDict[(entry[0],)] = var.table[entry]
        factor = CPT(var.name, newDict, [var.variables[0]], var.parents, var.children)
    else:
        factor = var
        if var.name != query:
            hidden.append(var.name)
    normalize(factor)
    factors.append(factor)
    return factors, hidden
    #return factors

def sumOut(var, factors, last=False):
    containingFactors = []
    notContainingFactors = []
    for factor in factors:
        if var in factor.variables:
            containingFactors.append(factor)
        else:
            notContainingFactors.append(factor)
    if not last:
        factor = pointWiseProd(None, containingFactors)
    varIndex = factor.variables.index(var)
    newTotal = defaultdict(int)
    for row in factor.table:
        newrow = tuple(list(row[0:varIndex]) + list(row[varIndex+1:]))
        newTotal[newrow] += factor.table[row]
    #newFactor = CPT(factor.name, dict(newTotal), factor.variables[0:varIndex] + factor.variables[varIndex+1:], factor.parents, factor.children)
    newFactor = CPT(factor.name, dict(newTotal), [x for x in factor.variables if x != var], factor.parents, factor.children)
    if not last:
        normalize(newFactor)
    notContainingFactors.append(newFactor)
    return notContainingFactors
    pass

def pointWiseProd(var, factors, last=False):
    #make an expectedposs subdictionary from the master using variable names from factors
    subExpectedPoss = {}
    factorNames = []
    if last:
        factors[1].variables.pop(1)
    for factor in factors:
        factorNames.append(factor.name)
        for h in factor.variables:
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
                if '*' not in variable or last:
                    lookupTup.append(auxDic[variable])
            lookupTup = tuple(lookupTup)
            #with lookupTup find the desired row in the CPT table
            probProduct *= factor.table[lookupTup]
        newCPT[assignment] = probProduct
        #newCPT[assignment + (True,)] = probProduct
       # newCPT[assignment + (False,)] = 1 - probProduct
    newName = "*"
    newName = newName.join(factorNames)
    return CPT(newName,
               newCPT,varOrder + [newName], factors[0].parents,factors[0].children)# create new CPT
        
            
def normalize(factor):
    total = sum(list(factor.table.values()))
    for condition in factor.table:
        factor.table[condition] /= total
    return factor
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
#PWExpectedAssignments = assign({}, list(PWExpectedPoss.keys()), PWExpectedPoss)
#print(PWExpectedAssignments)

PWExpected = CPT("john*mary",{
    (True, True, True): 0.9*0.7, (True, True, False): 0.05*0.01, (True, False, True): 0.9*0.3, (True, False, False):0.05*0.99, 
    (False, True, True): 0.1*0.7, (False, True, False): 0.95*0.01, (False, False, True):0.1*0.3, (False, False, False):0.95*0.99
}, ["john", "mary", "alarm", "john*mary"])
#test = pointWiseProd(None, pointWiseExample)
#print(test.table)
#print(sumOut("alarm", test).table)



def varElim(X, e, bn):
    factors = []
    hidden = []
    for var in bn:
        factors, hidden = makeFactor(bn[var], e, factors, hidden, X)
    hiddenVar = True
    for var in hidden: 
        factors = sumOut(var, factors)
    last = pointWiseProd(None, factors, True)
    last = sumOut("burglary", [last], True)
    return last




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
    "earthquake": CPT("earthquake",{
        (True,): 0.002,
        (False,): 0.998
    },["earthquake"],None,["alarm"]),
    "burglary": CPT("burglary", {
        (True,): 0.001,
        (False,): 0.999
    },["burglary"],None,["alarm"])
}
query = "burglary"
evidence = {
    "john": True
}
test = varElim(query, evidence, bayesNet)
print(f'Probability of a burglary given john called: {test[0].table}')