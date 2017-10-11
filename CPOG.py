from Functions import *
from LES import *
from Structures import *
from Exceptions import *
import math


def cpog(vertices,edges,condition,res_f):

    res={}
    res["ver"]=vertices
    res["ed"]=edges
    res["cond"]=condition
    res["res_f"]=res_f

    return res

def cpog_addition(g1,g2):

    add={}
    
    add["ver"]=union(g1["ver"],g2["ver"])
    
    add["ed"]=union(g1["ed"],g2["ed"])

    add["res_f"]="("+g1["res_f"]+")+("+g2["res_f"]+")"

    add["cond"]=[]
    elem1=union([a for (a,b) in g1["ver"]],g1["ed"])
    elem2=union([a for (a,b) in g2["ver"]],g2["ed"])
    elem=union([a for (a,b) in add["ver"]],add["ed"])
    for x in elem:
        add["cond"].append((x,"("+g1["res_f"]+")*("+g2["res_f"]+")'*"+cond(x,g1,elem1)+"+""("+g1["res_f"]+")'*("+g2["res_f"]+")*"+cond(x,g2,elem2)))

    return add

def cpog_scalar_mult(g,k):

    mult=g
    mult["res_f"]=k+"*"+g["res_f"]

    return mult

def cpog_from_scenarios(scenarios):

    # we need to add the transitive closure of cau for having the proper conditions
    old_cau=[]
    for sce in scenarios:
        old_cau.extend(sce["cau"])
        # we don't consider transitive closure if we want to apply cpog2les
#        sce["cau"]=transitive_closure(sce["cau"])
    
    count=1
    limit=len(scenarios)
    bits=int(math.log(limit,2)+.99)
    fk=bin_conditions(bits)

    cpog=cpog_scalar_mult(lpo2cpog(scenarios[0]),fk[0])

    while count < limit:
        sce=lpo2cpog(scenarios[count])
        k_sce=cpog_scalar_mult(sce,fk[count])
        cpog=cpog_addition(cpog,k_sce)
        count=count+1

    # we remove the transitive closure
    new_arcs=[]
    for arc in cpog["ed"]:
        if arc in old_cau and not arc in new_arcs:
            new_arcs.append(arc)
    cpog["ed"]=new_arcs
    
    return cpog

def cpog_merge_events(cpog,labels=[]):

    for (x,lab_x) in cpog["ver"]:
        for (y,lab_y) in cpog["ver"]:
            if x!=y and lab_x==lab_y:
                cpog=cpog_merge(x,y,cpog)
                cpog=cpog_merge_events(cpog,labels)
                break
        break
    
    return cpog

def cpog_merge(x,y,cpog):

    new_cpog={}
    new_ver=x+y
    new_lab=apply(cpog["ver"],x)
    
    new_cpog["ver"]=[(a,b) for (a,b) in cpog["ver"] if a!=x and a!=y]
    new_cpog["ver"].append((new_ver,new_lab))
    new_cpog["ed"]=[(a,b) for (a,b) in cpog["ed"] if a!=x and a!= y and b!= x and b!=y]
    new_cpog["cond"]=[(a,b) for (a,b) in cpog["cond"] if a!=x and a!= y]

    vertices=[a for (a,b) in cpog["ver"]]
    new_ver_cond="(" + cond(x,cpog,vertices) + ") + (" + cond(y,cpog,vertices) + ")"
    new_cpog["cond"].append((new_ver,new_ver_cond))
    
    for (a,b) in cpog["ed"]:
        cond_arc=cond((a,b),cpog,cpog["ed"])
        if x==a or y==a:
            if not (new_ver,b) in new_cpog["ed"]:
                new_cpog["ed"].append((new_ver,b))
                new_cpog["cond"].append(((new_ver,b),cond_arc))
            else:
                new_arc_cond="(" + cond((new_ver,b),new_cpog,new_cpog["ed"]) + ")+(" + cond_arc + ")"
                set_cond((new_ver,b),new_cpog,new_arc_cond)
 
        if x==b or y==b:
            if not (a,new_ver) in new_cpog["ed"]:
                new_cpog["ed"].append((a,new_ver))
                new_cpog["cond"].append(((a,new_ver),cond_arc))
            else:
                new_arc_cond="(" + cond((a,new_ver),new_cpog,new_cpog["ed"]) + ")+(" + cond_arc + ")"
                set_cond((a,new_ver),new_cpog,new_arc_cond)
                
    new_cpog["res_f"]=cpog["res_f"]

    return new_cpog

def lpo2cpog(les):

    cpog={}

    cpog["ver"]=[]
    for x in les["events"]:
        cpog["ver"].append(x)

    cpog["ed"]=[]
    for e in les["cau"]:
        cpog["ed"].append(e)

    cpog["res_f"]="1"
    cpog["cond"]=[]

    return cpog

def implicit_arc_reduction(cpog):

    vertices=[a for (a,b) in cpog["ver"]]
    for (x,y) in cpog["ed"]:
        cond_x=cond(x,cpog,vertices)
        cond_y=cond(y,cpog,vertices)
        cond_arc=cond((x,y),cpog,cpog["ed"])
        new_cond="(" + cond_x + ")' + (" + cond_arc + ")"
        new_cond="(" + cond_y + ")' + (" + new_cond + ")"
        cpog=set_cond((x,y),cpog,new_cond)

    return cpog
