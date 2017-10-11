# a partial order is a set of events together with the causality relation
# we only store information about direct causality

from Exceptions import*
from Relations import *
from Structures import *

def lpo(E,causality):

    lpo={}
    lpo["events"]=E
    lpo["cau"]=causality
    
    return lpo

def is_lpo(lpo):

    try:
        if not (list(lpo.keys())==["cau","events"] or list(lpo.keys())==["events","cau"]):
            raise not_LPO
        
        if not acyclic(lpo["cau"]):
            raise not_Partial_Order

        if not diff_events(lpo["events"]):
            raise not_Set_of_Events

        if not relation_over_events(lpo["cau"],lpo["events"]):
            raise extra_Event
    

        return True

    except not_LPO:
        print("there are more than events and causality")

    except not_Partial_Order:
        print("causality is not acyclic")

    except not_Set_of_Events:
        print("some event is defined twice with different labels")

    except extra_Event:
        print("some event in causality is not specified")

    return

# it renames all the events (and its appearances in causality) of the LPO
# adding "string" ath the beggining fo the name
def rename_lpo(string,target_lpo):

    new_lpo=lpo([],[])

    for x in target_lpo["events"]:
        new_lpo["events"].append((string + x[0],x[1]))
        
    for x in target_lpo["cau"]:
        new_lpo["cau"].append((string + x[0], string + x[1]))

    return new_lpo

# it returns the minimal (w.r.t <) elements of the LPO
def minimals(lpo):

    is_min={}
    for x in lpo["events"]:
        is_min[x[0]]=True

    for (x,y) in lpo["cau"]:
        is_min[y]=False

    res=[i for i in is_min.keys() if is_min[i]]
    
    return res

