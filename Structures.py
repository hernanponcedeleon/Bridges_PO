from Exceptions import *
import subprocess
from Functions import*

def diff_events(events):

    for (x,y) in events:
        for (w,z) in events:
            if (x,y)!=(w,z) and (x==w and y!=z):
                return False

    return True

def events(s):

    list_of_events=[]
    for (x,y) in s["events"]:
        if not x in list_of_events:
            list_of_events.append(x)

    return list_of_events

def label(a,s,elements):

    if a in [e for (e,lab_e) in elements]:
        for (x,y) in elements:
            if x==a:
                return y

    else:
        print(a, "not in ",[e for (e,lab_e) in elements])
        raise not_Found

def n_events(s):

    return len(s["events"])

def neg_rest(l,count):

    string=""
    for it in range(len(l)):
        if it!=count:
            string=string+"("+l[it]+")'"

    return string

def minimize(s):

    new_conds=[]
    for (x,cond) in s["cond"]:
        if cond=="0" or cond=="1":
            new_conds.append((x,cond))
        else:    
            command=["java","-cp","/Users/zeta96/Documents/Projects/CPOG2LES/Pyhton/Minimize.jar","MinimizedTable",cond]

            proc = subprocess.Popen(command, stdout=subprocess.PIPE)
            output = proc.stdout.read()
            op_cond = str(output).split('Minimized:')[1][8:-3]
            new_conds.append((x,op_cond))

    s["cond"]=new_conds

    res_f=s["res_f"]
    command=["java","-cp","/Users/zeta96/Documents/Projects/CPOG2LES/Pyhton/Minimize.jar","MinimizedTable",res_f]

    proc = subprocess.Popen(command, stdout=subprocess.PIPE)
    output = proc.stdout.read()
    op_cond = str(output).split('Minimized:')[1][8:-3]
    s["res_f"]=op_cond

    return s

def cond(e,s,elements):

    for (x,y) in s["cond"]:
        if x==e:
            return y

    if e in elements:
        return "1"
    else:
        return "0"

def set_cond(e,s,cond):

        for (x,y) in s["cond"]:
            if x==e:
                s["cond"].remove((x,y))
                s["cond"].append((x,cond))

        return s

def logic_reduction(s,elements):

    for x in elements:
        x_cond=cond(x,s,elements)
        new_cond="(" + s["res_f"] + ")' + (" + x_cond + ")"
        s=set_cond(x,s,new_cond)

    return s

def are_opposite(x,y,s,events):
    s_events=[x for (x,lab_x) in events]
    cond_x=cond(x,s,s_events)
    cond_y=cond(y,s,s_events)

    # we need to check if they are opposite but considering the restriction function
#    new_cond="("+s["res_f"] + ")' + ((" + cond_x + ")'+(" + cond_y + ")')"
    new_cond="(" + cond_x + ")'+(" + cond_y + ")'"

    command=["java","-cp","/Users/zeta96/Documents/Projects/CPOG2LES/Pyhton/Minimize.jar","MinimizedTable",new_cond]

    proc = subprocess.Popen(command, stdout=subprocess.PIPE)
    output = proc.stdout.read()
    op_cond = str(output).split('Minimized:')[1][8:-3]
    
    return op_cond=="1"
