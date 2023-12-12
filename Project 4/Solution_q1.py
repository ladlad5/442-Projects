class CPT:
    def __init__(self, name, table, parents=None, children=None):
        self.name = name
        self.parents = parents
        self.table = table
        self.children = children
    

def varElim(X, e, bn):
    factors = []
    for var in bn:
        pass

example = {
    "john": CPT("john", {
        (True,): 0.9,
        (False,): 0.05,
    }, ["alarm"]),
    "mary": CPT("mary", {
        (True, True): 0.7,
        (False, True): 0.01,
    }, ["alarm"])
}
expectedPointwiseProd = CPT("factor1", {
    (True, True, True): 0.7*0.9,
    (True, True, False): 0.01*0.05
},["john", "mary", "alarm"])