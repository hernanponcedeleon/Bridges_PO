from Structures import *

def is_symmetric(r):

    for (a,b) in r:
        if not (b,a) in r:
            return False

    return True

def is_irreflexive(r):

    for (a,b) in r:
        if a == b:
            return False

    return True

def is_transitive(r):

    for (a,b) in r:
        for (c,d) in r:
            if b == c:
               if not (a,d) in r:
                   return False
            else:
                continue

    return True

def is_po(r):

    return is_irreflexive(r) and not is_symmetric(r) and is_transitive(r)

def conf_inh_cau(conf,leq):

        for (a,b) in leq:
            for (c,d) in conf:
                if a==c and not (b,d) in conf:
                    return False

        return True

def is_function(f):

    # f is given as a list of pairs (x,f(x))

    for (a,b) in f:
        for (c,d) in f:
            if a==c and b!=d:
                return False

    return True

def acyclic(r):

    trans_closure=[]
    for x in r:
        trans_closure.append(x)

    for (x,y) in trans_closure:
        for (w,z) in trans_closure:
            if (x,y)!=(w,z) and y == w and not (x,z) in trans_closure:
                trans_closure.append((x,z))

    events =[]
    for (x,y) in trans_closure:
        if x not in events:
            events.append(x)
        if y not in events:
            events.append(y)

    for x in events:
        if (x,x) in trans_closure:
            return False

    return True

def relation_over_events(relation,events):

    list_of_events=[]
    for (x,y) in events:
        if not x in events:
            list_of_events.append(x)

    relation_events=[]
    for (x,y) in relation:
        if not x in relation_events:
            relation_events.append(x)
        if not y in relation_events:
            relation_events.append(y)

    for x in relation_events:
        if not x in list_of_events:
            return False

    return True

def function_over_events(function,events):

    list_of_events=[]
    for (x,y) in events:
        if not x in events:
            list_of_events.append(x)

    function_events=[]
    for (x,y) in function:
        if not x in function_events:
            function_events.append(x)
        
    for x in list_of_events:
        if not x in function_events:
            return False

    return True

def trans_closure(r):

    res=r

    for (x,y) in r:
        for (w,z) in r:
            if (x,y)!=(w,z) and y==w and not (x,z) in res:
                res.append((x,z))

    return res

def add_inheritance(r1,r2):

    untreated=[]
    for x in r1:
        untreated.append(x)

    res=[]
    for x in untreated:
        res.append(x)
        untreated.remove(x)

    while untreated != []:
        for (x,y) in untreated:
            for (w,z) in r2:
                if x==w and not (y,z) in res:
                    res.append((y,z))
                    untreated.append((y,z))
                if y==w and not (x,z) in res:
                    res.append((x,z))
                    untreated.append((x,z))
                    
            untreated.remove((x,y))

    return res

def add_reflexivity(r):

    res=r
    
    for (x,y) in r:
        if not (y,x) in res:
            res.append((y,x))

    return res

def times(e,f):

    res=[]
    for x in e:
        for y in f:
            res.append((x,y))

    return res

def transitive_closure_aux(r):

    for (x,y) in r:
        for (a,b) in r:
            if x!=a and y!=b and y==a:
                if not (x,b) in r:
                    r.append((x,b))

    return r

def transitive_closure(r):

    tra_clo=transitive_closure_aux(r)
    
    if r == tra_clo:
        return r

    else:
        return (transitive_closure(tra_clo))
    
