from LES import *
from Exceptions import *
import subprocess

def cles(events,cau,conf,cond,res_f):

    # CHECK IS-LES & THAT THE EVENTS IN COND ARE THOSE OS EVENTS
    
        res_cles ={}
        res_cles["events"]=events
        res_cles["cau"]=cau
        res_cles["conf"]=conf
        res_cles["cond"]=cond
        res_cles["res_f"]=res_f

        return res_cles

def struc_size(cles):

        return len(cles["events"])+len(cles["cau"])+len(cles["conf"])

        
def cond_event(e,cles):

    for (x,y) in cles["cond"]:
        if x==e:
            return y

def cond_cles(cles):

    cond_list=[]
    for (x,y) in cles["cond"]:
        if y not in cond_list:
            cond_list.append(y)

    return cond_list

def var_in_cond(cond):

    variables="abcdefghijklmnopqrstuv"
    count=0
    for x in cond:
        if x in variables:
            count=count+1

    return count

def set_cond_event(e,cles,cond):

        for (x,y) in cles["cond"]:
                if x==e:
                        cles["cond"].remove((x,y))
                        cles["cond"].append((x,cond))
        return cles

def fathers(e,cles):

        fathers=[]
        for (x,y) in cles["cau"]:
                if y==e:
                        fathers.append(x)

        return fathers

def same_cond_father(e,cles):

        if fathers(e,cles)==[]:
                return False

        else:
                flag=True
                for fat in fathers(e,cles):
                        if cond_event(fat,cles)!=cond_event(e,cles):
                                flag=False

                        else:
                                flag=True

                return flag


def cles2lpo(cles,assignement):

    new_lpo=lpo([],[])
    plain_events=[]

    for e in events(cles):
        cond="("+cond_event(e,cles)+")*("+assignement+")"
        command=["java","-cp","/Users/zeta96/Documents/Projects/CPOG2LES/Pyhton/Minimize.jar","MinimizedTable",cond]

        proc = subprocess.Popen(command, stdout=subprocess.PIPE)
        output = proc.stdout.read()
        op_cond = str(output).split('Minimized:')[1][8:-3]
        
        cles=set_cond_event(e,cles,op_cond)

    for (x,y) in cles["events"]:
        if cond_event(x,cles)==assignement:
            new_lpo["events"].append((x,y))
            plain_events.append(x)

    for (x,y) in cles["cau"]:
        if x in plain_events and y in plain_events:
            new_lpo["cau"].append((x,y))

    return new_lpo

def cles_from_scenarios(scenarios,fk):

    try:
        
        for lpo in scenarios:
            if not is_lpo(lpo):
                raise not_LPO

        # we only need as many fk as scenarios
        fk=fk[:len(scenarios)]

        # we rename the events of each LPO so we can copy them in the LES
        renamed_scenarios=[]
        counter=1
        for lpo in scenarios:
            renamed_scenarios.append(rename_lpo("lpo"+str(counter)+"_",lpo))
            counter=counter+1

        # events and causality are the same, each scenario is label by an unique condition
        new_cles=cles([],[],[],[],[])
        all_minimals=[]
        count=0
        for lpo in renamed_scenarios:
            new_cles["events"].extend(lpo["events"])
            new_cles["cau"].extend(lpo["cau"])
            for (x,y) in lpo["events"]:
                new_cles["cond"].append((x,fk[count]+"*"+neg_rest(fk,count)))
            count=count+1
            all_minimals.append(minimals(lpo))
            
        # the only (direct) conflicts are between the minimal events of each LPO
        new_cles["conf"].extend(mix_zip(all_minimals))

        res_f="0"
        for x in fk:
                res_f=res_f+"+"+x
        new_cles["res_f"]=res_f

        return new_cles
        
    except not_LPO:
        print("one of the scenarios is not an lpo")


def merge(a,b,cles):

    new_cles={}

    new_event=a+b
    new_cles["events"]=[i for i in cles["events"] if i[0]!=a and i[0]!=b]
    if not (new_event,label(a,cles)) in new_cles["events"]:
        new_cles["events"].append((new_event,label(a,cles)))

    new_cles["cau"]=[(x,y) for (x,y) in cles["cau"] if x!=a and x!=b and y!=a and y!=b]
    for (x,y) in cles["cau"]:
        if (x==a or x==b) and not (new_event,y) in new_cles["cau"]:
            new_cles["cau"].append((new_event,y))

        if (y==a or y==b) and not (x,new_event) in new_cles["cau"]:
            new_cles["cau"].append((x,new_event))

    cles["conf"].remove((a,b))
    new_cles["conf"]=[(x,y) for (x,y) in cles["conf"] if x!=a and x!=b and y!=a and y!=b]
    for (x,y) in cles["conf"]:
        if x==a and ((b,y) in cles["conf"] or (y,b) in cles["conf"]) and not (new_event,y) in new_cles["conf"]:
            new_cles["conf"].append((new_event,y))
        if x==b and ((a,y) in cles["conf"] or (y,a) in cles["conf"]) and not (new_event,y) in new_cles["conf"]:
            new_cles["conf"].append((new_event,y))
        if y==a and ((b,x) in cles["conf"] or (x,b) in cles["conf"]) and not (new_event,x) in new_cles["conf"]:
            new_cles["conf"].append((new_event,x))
        if y==b and ((a,x) in cles["conf"] or (x,a) in cles["conf"]) and not (new_event,x) in new_cles["conf"]:
            new_cles["conf"].append((new_event,x))

        future_a=[]
        future_b=[]
        for (x,y) in cles["cau"]:
            if x == a:
                future_a.append(y)
            if x == b:
                future_b.append(y)

        for fa in future_a:
            for fb in future_b:
                if not are_in_conflict(fa,fb,new_cles) and not (fa,fb) in new_cles["conf"]:
                    new_cles["conf"].append((fa,fb))

    new_cles["cond"]=[i for i in cles["cond"] if i[0]!=a and i[0]!=b]
    new_cles["cond"].append((new_event,cond_event(a,cles)+"+"+cond_event(b,cles)))
    new_cles["res_f"]=cles["res_f"]
    
    return new_cles

def merge_optimize(cles):

        for (x,y) in cles["conf"]:
           if label(x,cles) == label(y,cles) and pred(x,cles) == pred(y,cles):
                cles=merge(x,y,cles)
                # necessary to avoid considering conflict that do not exists any more
                # due to the merge
                return merge_optimize(cles)

        return cles


def cles_minimize(cles):

        for e in events(cles):
                cond=cond_event(e,cles)
                command='java -cp /Users/zeta96/Documents/Projects/CPOG2LES/Pyhton/Minimize.jar MinimizedTable '+cond
        
                proc = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
                output = proc.stdout.read()
                op_cond = str(output).split('Minimized:')[1][8:-3]

                cles=set_cond_event(e,cles,op_cond)

        return cles

def log_optimize(cles):

        for x in events(cles):
                cles=set_cond_event(x,cles,"("+cles["res_f"]+")'+"+cond_event(x,cles))

        return cles
