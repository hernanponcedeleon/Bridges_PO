# it takes a list of lists and return a list of pairs with the combinations of its elemens
# i.e. mix_zip([[a],[l,m][x,y,z]]) =
# [(a,l),(a,m),(a,x),(a,y),(a,z),(l,x),(l,y),(l,z),(m,x),(m,y),(m,z)]

def mix_zip(list_list):

    res=[]

    if len(list_list)==2:
        res = zip(list_list[0], list_list[1])
        
    else:
        for x_list in list_list[1:]:
            res.extend(zip(list_list[0],x_list))

        res.extend(mix_zip(list_list[1:]))

    return res

    
def zip(l1,l2):

    res=[]
    for x in l1:
        for y in l2:
            res.append((x,y))

    return res

def map(f,l):

    res=[]
    for x in l:
        res.append(f(x))

    return res

def bin_conditions(limit):

    neg_var=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","r","s","t","u","v"]
    var=["a'","b'","c'","d'","e'","f'","g'","h'","i'","j'","k'","l'","m'","n'","o'","p'","r'","s'","t'","u'","v'"]

    if limit==1:
        res = [var[0],neg_var[0]]

    else:
        bin_ant=bin_conditions(limit-1)
        res=[]
    
        for x in bin_ant:
            res.append(var[limit-1] + "*" + x)
            res.append(neg_var[limit-1] + "*" + x)

        
    return res

def build_csolver(n):

    if n==1:
        res=["0","1"]

    else:
        ant=build_csolver(n-1)
        res=[]

        for x in ant:
            res.append("0"+x)
            res.append("1"+x)

    return res

def neg(n):

    if n=="1":
        return "0"
    else:
        return "1"

def union(l1,l2):

    res=[]
    for x in l1:
        if not x in res:
            res.append(x)
    for x in l2:
        if not x in res:
            res.append(x)

    return res

def apply(f,e):

    for (x,fx) in f:
        if x==e:
            return fx

def key_of_value(val,d):

    for key in d.keys():
        if d[key]==val:
            return key
