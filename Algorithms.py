from CPOG import *
from LES import *
##from dot2py import *

def les2lpo(les,csolver):

    plain_events=[]
    for (x,y) in les["events"]:
        plain_events.append(x)
        
    i=0
    while i < len(les["conf"]):
        if les["conf"][i][int(neg(csolver[i]))] in plain_events:
           plain_events.remove(les["conf"][i][int(neg(csolver[i]))])
        i=i+1

    plain_events2=[]
    for x in plain_events:
        add_it=True
        for y in pred(x,les):
            if not y in plain_events:
                add_it=False
                break

        if add_it:
            plain_events2.append(x)

    events=[]
    for (x,y) in les["events"]:
        if x in plain_events2:
            events.append((x,y))

    causality=[]
    for (x,y) in les["cau"]:
        if x in plain_events2 and y in plain_events2:
            causality.append((x,y))

    return lpo(events,causality)

def les2cpog(les):
    
    variables="abcdefghijklmnopqrstuv"

    cpog={}

    cpog["ver"]=[]
    for x in les["events"]:
        cpog["ver"].append(x)

    cpog["ed"]=[]
    for x in les["cau"]:
        cpog["ed"].append(x)

    cpog["cond"]=[]
    for x in cpog["ed"]:
        cpog["cond"].append((x,"1"))
    for (x,lab_x) in cpog["ver"]:
        cpog["cond"].append((x,"1"))

    cpog["res_f"]=les["res_f"]

    # for every event in conflict and its future, we update their conditions       
    count=0
    for (x,y) in les["conf"]:    
        current_cond_x=cond(x,cpog,cpog["ver"])
        new_cond_x="(" + current_cond_x + ")(" + variables[count] + ")"
        set_cond(x,cpog,new_cond_x)

        for z in fut(x,les):
            current_cond_z=cond(z,cpog,cpog["ver"])
            new_cond_z="(" + current_cond_z + ")(" + variables[count] + ")"
            set_cond(z,cpog,new_cond_z)

        current_cond_y=cond(y,cpog,cpog["ver"])
        new_cond_y="(" + current_cond_y + ")(" + variables[count] + ")'"
        set_cond(y,cpog,new_cond_y)

        for z in fut(y,les):
            current_cond_z=cond(z,cpog,cpog["ver"])
            new_cond_z="(" + current_cond_z + ")(" + variables[count] + ")'"
            set_cond(z,cpog,new_cond_z)

        count=count+1

    # an arc is only there if both events are, but as every event contain the condition of its past, we only need the target of the arc
    for (x,y) in cpog["ed"]:
        cond_y=cond(y,cpog,cpog["ver"])
        set_cond((x,y),cpog,cond_y)
    
    # we merge events equally labeled
    cpog=cpog_merge_events(cpog,les["events"])
    
    return cpog

def cpog2les(cpog,new_events,les={},name_count=0):
    print("rec call")

    new_les={}
    for key in les.keys():
        new_les[key]=les[key]

    ver_cpog=[x for (x,lab_x) in cpog["ver"]]

    if new_les=={}:
        new_les["events"]=new_events
        new_les["cau"]=[]
        # a,b,c need to be in conflict at the beggining
        new_les["conf"]=[]

        new_les["res_f"]=cpog["res_f"]

        # we use conditions in a LES to check if they are opposite and they should be in conflict
        new_les["cond"]=[]
        for (x,lab_x) in cpog["ver"]:
            new_les["cond"].append((x,"1"))
        for (x,y) in cpog["ed"]:
            cond_y=cond(y,new_les,[e for (e,lab_e) in new_les["events"]])
            cond_arc=cond((x,y),cpog,cpog["ed"])
            new_cond_y="(" + cond_y + ")(" + cond_arc + ")"
            set_cond(y,new_les,new_cond_y)
            print("setting ",y,new_cond_y)
    
        for (x,lab_x) in new_les["events"]:
           for (y,lab_y) in new_les["events"]:
            if x!=y and are_opposite(x,y,new_les,new_les["events"]) and (not are_in_conflict(x,y,new_les)):
                new_les["conf"].append((x,y))
           
##    news=[]
##    lab_les={}
##    for (x,lab_x) in new_events:
##        lab_les[lab_x]=x
##    for (x,y) in cpog["ed"]:
##        lab_x=label(x,cpog,cpog["ver"])
##        lab_y=label(y,cpog,cpog["ver"])
##        # the new labels are in the origin of one arc
##        if lab_x in lab_les.keys():
##            past_x=pred(lab_les[lab_x],new_les)
##            labels_past_x=[]
##            for e in past_x:
##                labels_past_x.append(label(e,les,les["events"]))
##            new_event="ev"+str(name_count)
##            # if the label of the source is not already in the past, I add it
##            if not (new_event,lab_y) in new_les["events"] and not lab_y in labels_past_x:
##                name_count=name_count+1
##                new_les["events"].append((new_event,lab_y))
##                news.append((new_event,lab_y))
##                if not (x,new_event) in new_les["cau"]:
##                    new_les["cau"].append((lab_les[lab_x],new_event))
##
##                new_cond=cond((x,y),cpog,cpog["ed"])
###                new_cond="(" + cond((x,y),cpog,cpog["ed"]) + ")(" + cond(y,,ver_cpog) + ")"
##                new_les["cond"].append((new_event,new_cond))
##                
##                for (ev,lab_ev) in new_les["events"]:
##                    print(new_event)
##                    print(cond(new_event,new_les,new_les["events"]))
##                    print(ev)
##                    print(cond(ev,new_les,new_les["events"]))
##                    if new_event!=ev and are_opposite(new_event,ev,new_les,new_les["events"]) and (not are_in_conflict(new_event,ev,new_les)):
##                        new_les["conf"].append((new_event,ev))
##                        print("new conf ",new_event,ev)
##
##    if news==[]:
##        return new_les
##    else:
##        return cpog2les(cpog,news,new_les,name_count)
