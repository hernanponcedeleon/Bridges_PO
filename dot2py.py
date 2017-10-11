from LES import *

def get_events(dot_name):

  dot_file = open('/Users/ponceh1/Documents/Projects/CPOG2LES/Examples/dot/' + dot_name + '.dot','r')
  events=[]

  for line in dot_file:
    if "->" in line:
      f_ev_name=(line.split("\t")[0]).split(" ->")[0][2:]
      s_ev_name=(line.split("-> ")[1]).split(" [")[0].split(";")[0]
        
      if not f_ev_name in events:
        events.append((f_ev_name,f_ev_name))

      if not s_ev_name in events:
        events.append((s_ev_name,s_ev_name))

    #events_labels=zip(events,events)

  return events

def get_cau(dot_name):

  dot_file = open('/Users/ponceh1/Documents/Projects/CPOG2LES/Examples/dot/' + dot_name + '.dot','r')
  cau=[]

  for line in dot_file:
    if "->" in line:
      f_ev_name=(line.split("\t")[0]).split(" ->")[0][2:]
      s_ev_name=((line.split("-> ")[1]).split(" [")[0]).split(";")[0]
      if not (f_ev_name,s_ev_name) in cau:
        cau.append((f_ev_name,s_ev_name))

  return cau

def get_conf(dot_name):

  dot_file = open('/Users/ponceh1/Documents/Projects/CPOG2LES/Examples/dot/' + dot_name + '.dot','r')
  conf=[]

  for line in dot_file:
    if "dashed" in line:
      f_ev_name=(line.split("\t")[0]).split(" ->")[0][2:]
      s_ev_name=(line.split("-> ")[1]).split(" [")[0]
      if not (f_ev_name,s_ev_name) in conf:
        conf.append((f_ev_name,s_ev_name))

  return conf

def dot2les(dot_name):

  return les(get_events(dot_name),get_cau(dot_name),get_conf(dot_name))
