# Events are of the form (e,l) where e is the event and l its label
# a labeled event structures is then a set E together with the causality relation and the conflict relation

from Exceptions import *
from Relations import *
from Structures import *
from LPO import *
from Functions import *
from py2dot import *

def les(E,causality,conflict):

    # E is a list of pairs representing the events and its labels
    # we only store information about direct causality and conflcit
    # conflicts (a,b) and (b,a) are represented by only one pair

    les={}
    les["events"]=E
    les["cau"]=causality
    les["conf"]=conflict

    return les

def is_les(les):

    try:
        if not acyclic(les["cau"]):
            raise not_Partial_Order

        if not diff_events(les["events"]):
            raise not_Set_of_Events

        if not relation_over_events(les["cau"],les["events"]):
            raise extra_Event

        if not relation_over_events(les["conf"],les["events"]):
            raise extra_Event

        return True

    except not_Partial_Order:
        print("causality is not acyclic")

    except not_Set_of_Events:
        print("some event is defined twice with different labels")

    except extra_Event:
        print("some event in causality or conflict is not specified")

    return


# it checks if events "a" and "b" are in conflict (also considering those that
# are inherited)
def are_in_conflict(a,b,les):

#    all_conflict=add_reflexivity(add_inheritance(les["conf"],les["cau"]))
#    return (a,b) in all_conflict or (b,a) in all_conflict

    all_conflicts=[]
    for x in les["conf"]:
        all_conflicts.append(x)

    fut_e1=[]
    fut_e2=[]
    for (e1,e2) in les ["conf"]:
        fut_e1=[e1]+[e for e in fut(e1,les) if e in [a for (a,b) in les["events"]]]
        fut_e2=[e2]+[e for e in fut(e2,les) if e in [a for (a,b) in les["events"]]]
        
        for x in fut_e1:
            for y in fut_e2:
                if x!=y and not (x,y) in all_conflicts:
                    all_conflicts.append((x,y))

    return (a,b) in all_conflicts or (b,a) in all_conflicts

# computes the concurrency relation of a LES
# dirrently as how we store causality or conflict, both pairs are stored (co is symmetric)
def concurrency(les):

    plain_events=[i[0] for i in les["events"]]
    co=times(plain_events,plain_events)
    all_causality=trans_closure(les["cau"])
    all_conflict=add_reflexivity(add_inheritance(les["conf"],les["cau"]))

    # removes autoconcurrency
    for (x,y) in co:
        if x==y:
            co.remove((x,y))

    # removes all pairs that are causally dependant
    for (x,y) in all_causality:
        co.remove((x,y))
        co.remove((y,x))

    #removes all conflicting pairs
    for x in all_conflict:
        if x in co:
            co.remove(x)
        
    return co

# computes the events that are concurrent to event "e"
def co_events(e,les):

    res=[]
    for (x,y) in concurrency(les):
        if e==x and not y in res:
            res.append(y)

    return res

# computes the causal predecessors of event e
def pred(e,les):

    smallers=[]
    for (x,y) in les["cau"]:
        if y == e and not x in smallers:
            smallers.append(x)

    res=[]

    res.extend(smallers)

    for x in smallers:
        res.extend(pred(x,les))

    return res

# it returns the events and the arcs in the future of a given events
def fut(e,les):

    big_ev=[]
    big_arcs=[]
    for (x,y) in les["cau"]:
        if x == e and not y in big_ev:
            big_ev.append(y)
 #       if x==e and not (x,y) in big_arcs:
#            big_arcs.append((x,y))

    res=[]
    for x in big_ev:
        res.extend(fut(x,les))

#    res=res + big_ev + big_arcs
    res=res + big_ev

    return res

# merge(a,b,les) merges two events with the same label,
# and update the causality/conflict information
def merge_les(a,b,les):
                
    new_event=a+b
    
    # both events should have the same label and be in conflict
    mg_les={}
    mg_les["events"]=[i for i in les["events"] if i[0]!=a and i[0]!=b]
    mg_les["events"].append((new_event,label(a,les,les["events"])))

    # update causalities
    mg_les["cau"]=[i for i in les["cau"] if i[0]!=a and i[0]!= b and i[1]!=a and i[1]!=b]

    for (x,y) in les["cau"]:

        # if a < x or b < x for some x, we add ab < x
        if x == a or x == b:
            if not (new_event,y) in mg_les["cau"]:
                mg_les["cau"].append((new_event,y))

        # if x < a or x < b for some x, we add x < ab
        if y == a or y == b:
            if not (x,new_event) in mg_les["cau"]:
                mg_les["cau"].append((x,new_event))

    # update conflicts
    mg_les["conf"]=[i for i in les["conf"] if not(i[0]==a or i[1]==b or i[1]==a or i[0]==b)]

    # if a # x and b # x for some x, we add ab # x 
    for (x,y) in les["conf"]:
        if x==a and b!=y:
            if (are_in_conflict(b,y,les)) or ((b,y) in les["conf"]) or ((y,b) in les["conf"]):
                if (not are_in_conflict(new_event,y,mg_les)) and (not (new_event,y) in les["conf"]):
                    mg_les["conf"].append((new_event,y))
                    continue
            else:
                mg_les["conf"]=resolve_conf_co_conf_events(a,y,les,mg_les)
                continue

        elif x==b and a!=y:
            if (are_in_conflict(a,y,les)) or ((a,y) in les["conf"]) or ((a,y) in les["conf"]):
                if (not are_in_conflict(new_event,y,mg_les)) and (not (new_event,y) in les["conf"]):
                    mg_les["conf"].append((new_event,y))
                    continue
            else:
                mg_les["conf"]=resolve_conf_co_conf_events(b,y,les,mg_les)
                continue

        elif x!=a and b==y:
            if (are_in_conflict(a,x,les)) or ((a,x) in les["conf"]) or ((x,a) in les["conf"]):
                if (not are_in_conflict(new_event,x,mg_les)) and (not (new_event,x) in les["conf"]):
                    mg_les["conf"].append((new_event,x))
                    continue
            else:
                mg_les["conf"]=resolve_conf_co_conf_events(b,x,les,mg_les)
                continue

        elif x!=b and a==y:
            
            if (are_in_conflict(b,x,les)) or ((b,x) in les["conf"]) or ((x,b) in les["conf"]):
                if (not are_in_conflict(new_event,x,mg_les)) and not ((new_event,x) in les["conf"]):
                    mg_les["conf"].append((new_event,x))
                    continue
            else:
                mg_les["conf"]=resolve_conf_co_conf_events(a,x,les,mg_les)
                continue

    # we add the inherited conflicts
    future_a, future_b = [],[]

    for (x,y) in les["cau"]:
        if x == a:
            future_a.append(y)
        if x == b:
            future_b.append(y)

    for x in future_a:
        for y in future_b:
            if not are_in_conflict(x,y,mg_les):
                mg_les["conf"].append((x,y))

    # if a conflict is more than once, we remove it
    final_conf=[]
    for conf in mg_les["conf"]:
        if not conf in final_conf:
            final_conf.append(conf)
    mg_les["conf"]=final_conf
    
    return mg_les

def resolve_conf_co_conf_events(a,b,les,mg_les):

    new_conf=mg_les["conf"]
    for (x,y) in les["cau"]:
        if x==a and not are_in_conflict(b,y,mg_les):
            new_conf.append((b,y))

    return new_conf


# optimize takes a LES and optimize it merging events in conflict with the same label
def optimize(les):

    try:
        if not is_les(les):
            raise not_LES

        for (x,y) in les["conf"]:
            if label(x,les,les["events"]) == label(y,les,les["events"]) and pred(x,les) == pred(y,les):               
                les=merge_les(x,y,les)
                # necessary to avoid considering conflict that do not exists any more
                # due to the merge
                return optimize(les)
    
        return les

    except not_LES:
        print("not a LES")

# it takes a list of scenarios (LPOs) and build a LES having them as its configurations
# it is not optiomal: it just "glue" them together putting its minimal elements in conflict
def les_from_scenarios(scenarios):

    try:
        
        for lpo in scenarios:
            if not is_lpo(lpo):
                raise not_LPO

        # we rename the events of each LPO so we can copy them in the LES
        renamed_scenarios=[]
        counter=1
        for lpo in scenarios:
            renamed_scenarios.append(rename_lpo("lpo"+str(counter)+"_",lpo))
            counter=counter+1

        # events and causality are the same
        new_les={}
        new_les["events"]=[]
        new_les["cau"]=[]
        new_les["conf"]=[]
        
        all_minimals=[]
        for lpo in renamed_scenarios:
            new_les["events"].extend(lpo["events"])
            new_les["cau"].extend(lpo["cau"])
            all_minimals.append(minimals(lpo))
            
        # the only (direct) conflicts are between the minimal events of each LPO
        new_les["conf"].extend(mix_zip(all_minimals))

        return new_les
        
    except not_LPO:
        print("one of the scenarios is not an lpo")


def conf_each_events(les):
    
    variables="abcdefghijklmnopqrstuv"

    events={}
    for (x,lab_x) in les["events"]:
        conf_x=[]
        count=0
        for (e1,e2) in les["conf"]:
            if x==e1:
                conf_x.append((e2,variables[count]))
            elif x==e2:
                conf_x.append((e1,variables[count]+"'"))
            count=count+1

        events[x]=conf_x

    return events

def maximals(les):

    is_max={}
    for x in les["events"]:
        is_max[x[0]]=True

    for (x,y) in les["cau"]:
        is_max[x]=False

    res=[i for i in is_max.keys() if is_max[i]]
    
    return res

def res_f_synthesis(les):

    ev=conf_each_events(les)

    solver={}
    for x in [e for (e,lab_e) in les["events"]]:
        solver[x]="1"

    for e in ev.keys():
        for var_ev in ev[e]:
            solver[e]="(" + solver[e] + ")(" + var_ev[1] +")"

    solver_past={}
    for e in solver.keys():
        solver_past[e]="1"
        for z in pred(e,les):
            solver_past[e]="(" + solver_past[e] + ")(" + solver[z] + ")"

    res_f="1"
    for (e1,e2) in les["conf"]:
        res_f="(" + res_f + ")((" + solver_past[e1] +")'+(" + solver[e1] + "))+((" + solver_past[e2] +")'+(" + solver[e2] + "))"

    print(res_f)
        
    command=["java","-cp","/Users/zeta96/Documents/Projects/CPOG2LES/Pyhton/Minimize.jar","MinimizedTable",res_f]
    proc = subprocess.Popen(command, stdout=subprocess.PIPE)
    output = proc.stdout.read()
    res_f = str(output).split('Minimized:')[1][8:-3]

    return res_f
