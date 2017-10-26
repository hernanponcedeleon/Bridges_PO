import sys

from py2dot import *
from Algorithms import *
import time
import math

ARM1 = lpo([ ("pciu","PCIU"),
             ("ifu","IFU"),
             ("alu","ALU"),
             ("mau","MAU"),
             ("pciu2","PCIU/2"),
             ("ifu2","IFU/2")
            ],

           [("pciu","ifu"),("ifu","alu"),("alu","mau"),("mau","pciu2"),("pciu2","ifu2")]

           ) 

ARM2 = lpo([ ("pciu","PCIU"),
             ("ifu","IFU"),
             ("alu","ALU"),
             ("mau","MAU"),
             ("ifu2","IFU/2")
            ],

           [("pciu","ifu"),("ifu","alu"),("alu","mau"),("mau","ifu2")]

           )

ARM3 = lpo([ ("pciu","PCIU"),
             ("pciu2","PCIU/2"),
             ("ifu","IFU")
            ],

           [("pciu","pciu2"),("pciu2","ifu")]

           ) 

ARM4 = lpo([ ("pciu","PCIU"),
             ("ifu","IFU"),
             ("alu","ALU"),
             ("ifu2","IFU/2")
            ],

           [("pciu","ifu"),("ifu","alu"),("alu","ifu2")]

           )

ARM5 = lpo([ ("ifu","IFU"),
             ("alu","ALU"),
             ("mau","MAU"),
            ],

           [("alu","mau"),("mau","ifu")]

           ) 


ARM6 = lpo([ ("pciu","PCIU"),
             ("ifu","IFU"),
             ("alu","ALU"),
             ("pciu2","PCIU/2"),
             ("ifu2","IFU/2")
            ],

           [("pciu","ifu"),("ifu","alu"),("ifu","pciu2"),("pciu2","ifu2"),("alu","ifu2")]

           ) 

ARM7 = lpo([ ("pciu","PCIU"),
             ("ifu","IFU"),
             ("alu","ALU"),
             ("mau","MAU"),
            ],

           [("pciu","ifu"),("alu","mau")]

           ) 

ARM8 = lpo([ ("ifu","IFU"),
             ("mau","MAU"),
           ],

           [("mau","ifu")]

           ) 

ARM9 = lpo([ ("pciu","PCIU"),
             ("ifu","IFU"),
             ("mau","MAU"),
            ],

           [("pciu","ifu")]

           ) 

ARM10 = lpo([ ("pciu","PCIU"),
              ("ifu","IFU"),
              ("alu","ALU"),
            ],

           [("pciu","ifu")]

           ) 

ARM11 = lpo([ ("ifu","IFU"),
              ("alu","ALU"),
            ],

           [("alu","ifu")]

           ) 

A = lpo([("pciu","PCIU"),
         ("ifu","IFU"),
         ("alu","ALU"),
         ("mau","MAU"),
         ("alu2","ALU/2"),
         ("mau2","MAU/2")
        ],

        [("pciu","ifu"),("alu","mau"),("mau","alu2"),("alu2","ifu"),("alu2","mau2")]

        )

B = lpo([("pciu","PCIU"),
         ("ifu","IFU"),
         ("alu","ALU"),
         ("mau","MAU"),
         ("alu2","ALU/2"),
         ("mau2","MAU/2"),
         ("pciu2","PCIU/2"),
         ("ifu2","IFU/2")
        ],
         
        [("pciu","ifu"),("ifu","pciu2"),("pciu2","ifu2"),("ifu","alu"),("alu","ifu2"),("alu","mau"),("mau","alu2"),("alu2","mau2")]

        )

C = lpo([("pciu","PCIU"),
         ("ifu","IFU"),
         ("alu","ALU"),
         ("mau","MAU"),
         ("pciu2","PCIU/2"),
         ("ifu2","IFU/2")
        ],
         
        [("pciu","ifu"),("ifu","pciu2"),("pciu2","ifu2"),("ifu","alu"),("alu","ifu2"),("alu","mau")]

        )

D = lpo([("pciu","PCIU"),
         ("ifu","IFU"),
         ("alu","ALU"),
         ("mau","MAU"),
         ("alu2","ALU/2"),
         ("mau2","MAU/2"),
         ("alu3","ALU/3"),
         ("mau3","MAU/3"),
         ("alu4","ALU/4"),
         ("mau4","MAU/4")
        ],
         
        [("pciu","ifu"),("alu","mau"),("mau","alu2"),("alu2","mau2"),("mau2","alu3"),("alu3","ifu"),("alu3","mau3"),("mau3","alu4"),("alu4","mau4")]

        )

E = lpo([("pciu","PCIU"),
         ("ifu","IFU"),
         ("alu","ALU"),
         ("mau","MAU"),
         ("alu2","ALU/2"),
         ("mau2","MAU/2"),
         ("pciu2","PCIU/2"),
         ("ifu2","IFU/2")
        ],
         
        [("pciu","ifu"),("ifu","pciu2"),("pciu2","ifu2"),("alu","mau"),("mau","alu2"),("alu2","mau2"),("ifu","alu2"),("alu2","ifu2")]

        )

F = lpo([("pciu","PCIU"),
         ("ifu","IFU"),
         ("alu","ALU"),
         ("mau","MAU"),
         ("alu2","ALU/2"),
         ("mau2","MAU/2"),
         ("pciu2","PCIU/2"),
         ("ifu2","IFU/2"),
         ("alu3","ALU/3"),
         ("mau3","MAU/3")
        ],
         
        [("pciu","ifu"),("ifu","pciu2"),("pciu2","ifu2"),("alu","mau"),("mau","alu2"),("alu2","mau2"),("ifu","alu2"),("alu2","ifu2"),("mau2","alu3"),("alu3","mau3")]

        )

G = lpo([("pciu","PCIU"),
         ("ifu","IFU"),
         ("alu","ALU"),
         ("mau","MAU"),
         ("alu2","ALU/2"),
         ("mau2","MAU/2"),
         ("alu3","ALU/3"),
         ("mau3","MAU/3"),
         ("alu4","ALU/4"),
         ("mau4","MAU/4")
        ],
         
        [("pciu","ifu"),("alu","mau"),("mau","alu2"),("alu2","mau2"),("mau2","alu3"),("alu4","ifu"),("alu3","mau3"),("mau3","alu4"),("alu4","mau4")]

        )

I = lpo([("pciu","PCIU"),
         ("ifu","IFU"),
         ("alu","ALU")
        ],

        [("pciu","ifu")]

        )

J = lpo([("pciu","PCIU"),
         ("ifu","IFU"),
         ("alu","ALU"),
         ("mau","MAU"),
         ("alu2","ALU/2"),
         ("mau2","MAU/2"),
         ("pciu2","PCIU/2"),
         ("ifu2","IFU/2"),
         ("pciu3","PCIU/3"),
         ("ifu3","IFU/3")
        ],
         
        [("pciu","ifu"),("ifu","alu"),("alu","mau"),("mau","alu2"),("alu2","mau2"),("ifu","pciu2"),("pciu2","ifu2"),("ifu2","pciu3"),("pciu3","ifu3"),("ifu2","alu2"),("alu2","ifu3")]

        )

K = lpo([("pciu","PCIU"),
         ("ifu","IFU"),
         ("alu","ALU"),
         ("mau","MAU"),
         ("alu2","ALU/2"),
         ("mau2","MAU/2"),
         ("pciu2","PCIU/2"),
         ("ifu2","IFU/2"),
         ("alu3","ALU/3"),
         ("mau3","MAU/3")
        ],
         
        [("pciu","ifu"),("alu","mau"),("mau","alu2"),("alu2","mau2"),("ifu","pciu2"),("pciu2","ifu2"),("mau2","alu3"),("alu3","mau3"),("ifu","alu3"),("alu3","ifu2")]

        )

L = lpo([("pciu","PCIU"),
         ("ifu","IFU"),
         ("alu","ALU"),
         ("mau","MAU"),
         ("alu2","ALU/2"),
         ("pciu2","PCIU/2"),
         ("ifu2","IFU/2"),
         ("pciu3","PCIU/3"),
         ("ifu3","IFU/3")
        ],
         
        [("pciu","ifu"),("ifu","pciu2"),("pciu2","ifu2"),("ifu2","pciu3"),("ifu2","alu2"),("pciu3","ifu3"),("ifu","alu"),("alu","alu2"),("alu2","mau")]

        )

M = lpo([("pciu","PCIU"),
         ("ifu","IFU"),
         ("alu","ALU"),
         ("mau","MAU"),
         ("alu2","ALU/2"),
         ("pciu2","PCIU/2"),
         ("ifu2","IFU/2"),
         ("mau2","MAU/2"),
         ("sidu","SIDU")
        ],
         
        [("pciu","ifu"),("ifu","pciu2"),("pciu2","ifu2"),("ifu","alu"),("alu","ifu2"),("alu","mau"),("mau","alu2"),("alu2","mau2"),("sidu","alu2")]

        )

N = lpo([("pciu","PCIU"),
         ("ifu","IFU"),
         ("alu","ALU"),
         ("mau","MAU"),
         ("alu2","ALU/2"),
         ("mau2","MAU/2"),
         ("pciu2","PCIU/2"),
         ("ifu2","IFU/2"),
         ("sidu","SIDU")
        ],
         
        [("pciu","ifu"),("ifu","pciu2"),("pciu2","ifu2"),("alu","mau"),("mau","alu2"),("alu2","mau2"),("ifu","alu2"),("alu2","ifu2"),("mau","sidu")]

        )

O = lpo([("pciu","PCIU"),
         ("ifu","IFU"),
         ("alu","ALU"),
         ("mau","MAU"),
         ("alu2","ALU/2"),
         ("mau2","MAU/2"),
         ("alu3","ALU/3"),
         ("mau3","MAU/3"),
         ("alu4","ALU/4"),
         ("mau4","MAU/4")
        ],
         
        [("pciu","ifu"),("alu","mau"),("mau","alu2"),("alu2","mau2"),("mau2","alu3"),("alu3","mau3"),("mau3","alu4"),("alu4","mau4")]

        )


P = lpo([("pciu","PCIU"),
         ("ifu","IFU"),
         ("alu","ALU"),
         ("mau","MAU"),
         ("alu2","ALU/2"),
         ("mau2","MAU/2"),
         ("alu3","ALU/3"),
         ("mau3","MAU/3"),
         ("alu4","ALU/4"),
         ("mau4","MAU/4"),
         ("alu5","ALU/5"),
         ("mau5","MAU/5")
        ],
         
        [("pciu","ifu"),("alu","mau"),("mau","alu2"),("alu2","mau2"),("mau2","alu3"),("alu3","mau3"),("mau3","alu4"),("alu4","mau4"),("mau4","alu5"),("alu5","mau5")]

        )

Q = lpo([("pciu","PCIU"),
         ("ifu","IFU"),
         ("alu","ALU"),
         ("mau","MAU"),
         ("alu2","ALU/2"),
         ("mau2","MAU/2"),
         ("alu3","ALU/3"),
         ("mau3","MAU/3"),
         ("alu4","ALU/4"),
         ("mau4","MAU/4"),
         ("pciu2","PCIU/2"),
         ("ifu2","IFU/2")
        ],
         
        [("pciu","ifu"),("ifu","pciu2"),("pciu2","ifu2"),("ifu","alu2"),("alu","mau"),("mau","alu2"),("alu2","mau2"),("mau2","alu3"),("alu3","mau3"),("mau3","alu4"),("alu4","mau4"),("alu4","ifu2")]

        )

R = lpo([("pciu","PCIU"),
         ("ifu","IFU"),
         ("alu","ALU"),
         ("mau","MAU"),
         ("pciu2","PCIU/2"),
         ("ifu2","IFU/2"),
         ("alu2","ALU/2")
        ],
         
        [("pciu","ifu"),("ifu","pciu2"),("pciu2","ifu2"),("ifu","alu"),("alu","ifu2"),("alu","mau"),("mau","alu2")]

        )

S = lpo([("pciu","PCIU"),
         ("ifu","IFU"),
         ("alu","ALU"),
         ("mau","MAU"),
         ("sidu","SIDU")
        ],
         
        [("pciu","ifu"),("sidu","alu"),("alu","mau")]

        )


T = lpo([("pciu","PCIU"),
         ("ifu","IFU"),
         ("alu","ALU"),
         ("mau","MAU"),
         ("sidu","SIDU"),
         ("alu2","ALU/2")
        ],
         
        [("pciu","ifu"),("mau","alu2"),("alu","mau"),("mau","sidu")]

        )

U = lpo([("pciu","PCIU"),
         ("ifu","IFU"),
         ("alu","ALU"),
         ("ifu2","IFU/2"),
        ],
         
        [("pciu","ifu"),("ifu","alu"),("alu","ifu2")]

        )

V = lpo([("pciu","PCIU"),
         ("ifu","IFU"),
        ],
         
        [("pciu","ifu")]

        )

W = lpo([("alu","ALU"),
         ("mau","MAU"),
         ("alu2","ALU/2"),
         ("mau2","MAU/2"),
         ("alu3","ALU/3"),
         ("ifu","IFU")
        ],
         
        [("alu","mau"),("mau","alu2"),("alu2","mau2"),("mau2","alu3"),("alu3","ifu")]

        )

X = lpo([("alu","ALU"),
         ("mau","MAU"),
         ("alu2","ALU/2"),
         ("ifu","IFU"),
         ("ifu2","IFU/2"),
         ("sidu","SIDU"),
         ("pciu","PCIU")
        ],
         
        [("pciu","ifu"),("ifu","alu2"),("sidu","alu"),("alu","mau"),("mau","alu2"),("alu2","ifu2")]

        )

Y = lpo([("alu","ALU"),
         ("mau","MAU"),
         ("alu2","ALU/2"),
         ("ifu","IFU"),
         ("sidu","SIDU")
        ],
         
        [("alu","mau"),("mau","alu2"),("alu2","ifu"),("mau","sidu")]

        )


def main(count, limit):
    count_init = count

    print("INTEL benchmarks")
    print("")

    while count <= limit:
        sce=[A,B,C,D,E,F,G,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y][:count]
        sce_les=les_from_scenarios(sce)
        print("Number of partial orders: %s" %count)
        print("Complexity of set of LPOs: %s" %(len(sce_les["events"])+len(sce_les["cau"])))
        op_les=optimize(sce_les)
        print("Complexity of LES: %s" %(len(op_les["events"])+len(op_les["cau"])+len(op_les["conf"])))
        print("")

        count=count+1

    count = count_init
    print("ARM benchmarks")
    print("")

    while count <= limit:
        sce=[ARM1,ARM2,ARM3,ARM4,ARM5,ARM6,ARM7,ARM8,ARM9,ARM10,ARM11][:count]
        print("Number of partial orders: %s" %count)
        print("Complexity of set of LPOs: %s" %(len(sce_les["events"])+len(sce_les["cau"])))
        op_les=optimize(sce_les)
        print("Complexity of LES: %s" %(len(op_les["events"])+len(op_les["cau"])+len(op_les["conf"])))
        print("")

        count=count+1

    print("done")
                
if __name__ == "__main__" :
    main(9, 11)
