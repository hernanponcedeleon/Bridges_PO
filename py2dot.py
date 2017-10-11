from LPO import *
from CLES import *
from CPOG import *

def convert_lpo(lpo,dot_name):

    dot_file = open('/Users/zeta96/Documents/Projects/CPOG2LES/Examples/dot/' + dot_name + '.dot','w')

    dot_file.write("digraph lpo { \n")

    for (x,label) in lpo["events"]:

        dot_file.write("\t" + x + "[label=\"" + label + "\"];\n")

    for (x,y) in lpo["cau"]:
        
        dot_file.write("\t" + x + " -> " + y + ";\n")

    dot_file.write("\t}")
    
    dot_file.close()

def convert_les(les,dot_name):

    vertices=[a for (a,b) in les["events"]]
    elem=union(les["cau"],vertices)

    dot_file = open('/Users/zeta96/Documents/Projects/CPOG2LES/Examples/dot/' + dot_name + '.dot','w')

    dot_file.write("digraph les { \n")

    for (x,label) in les["events"]:

#        if cond(x,les,elem)=="1":
#            dot_file.write("\t" + x + "[label=\"" + x + "\"];\n")
#        else:
#            dot_file.write("\t" + x + "[label=\"" + x + ":" + cond(x,les,elem) + "\"];\n")

        dot_file.write("\t" + x + "[label=\"" + label + "\"];\n")

    for (x,y) in les["cau"]:
        
        dot_file.write("\t" + x + " -> " + y + ";\n")

    for (x,y) in les["conf"]:

        dot_file.write("\t" + x + " -> " + y + "[style=dashed, dir=none] ;\n")

    dot_file.write("\t}")
    
    dot_file.close()

def convert_cpog(cpog,dot_name):

    vertices=[a for (a,b) in cpog["ver"]]
    elem=union(cpog["ed"],vertices)

    dot_file = open('/Users/zeta96/Documents/Projects/CPOG2LES/Examples/dot/' + dot_name + '.dot','w')

    dot_file.write("digraph les { \n")

    for (x,lab_x) in cpog["ver"]:
        if cond(x,cpog,elem)=="1":
            dot_file.write("\t" + x + "[label=\"" + lab_x + "\"];\n")
        else:
            dot_file.write("\t" + x + "[label=\"" + lab_x + ":" + cond(x,cpog,elem) + "\"];\n")

    for (x,y) in cpog["ed"]:
        if cond((x,y),cpog,elem)=="1":
            dot_file.write("\t" + x + " -> " + y + ";\n")
        else:       
            dot_file.write("\t" + x + " -> " + y + " [label=\"" + cond((x,y),cpog,elem) + "\"];\n")

    dot_file.write("\t}")
    
    dot_file.close()

def convert_cles(cles,dot_name):

    dot_file = open('/Users/zeta96/Documents/Projects/CPOG2LES/Examples/dot/' + dot_name + '.dot','w')

    dot_file.write("digraph les { \n")

    for (x,label) in cles["events"]:
        if same_cond_father(x,cles) or cond_event(x,cles)=="1":
            dot_file.write("\t" + x + "[label=\"" + label + "\"];\n")

        else:
            dot_file.write("\t" + x + "[label=\"" + label + " - " + cond_event(x,cles) + "\"];\n")

    for (x,y) in cles["cau"]:
        
        dot_file.write("\t" + x + " -> " + y + ";\n")

    for (x,y) in cles["conf"]:

        dot_file.write("\t" + x + " -> " + y + "[style=dashed, dir=none] ;\n")

    dot_file.write("\t}")
    
    dot_file.close()

def convert_cles_old(cles,dot_name):

    dot_file = open('/Users/zeta96/Documents/Projects/CPOG2LES/Examples/dot/' + dot_name + '.dot','w')

    dot_file.write("digraph les { \n")

    for (x,label) in cles["events"]:
        dot_file.write("\t" + x + "[label=\"" + label + " / " + cond_event(x,cles) + "\"];\n")

    for (x,y) in cles["cau"]:
        
        dot_file.write("\t" + x + " -> " + y + ";\n")

    for (x,y) in cles["conf"]:

        dot_file.write("\t" + x + " -> " + y + "[style=dashed, dir=none] ;\n")

    dot_file.write("\t}")
    
    dot_file.close()
