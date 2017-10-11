import sys

from py2dot import *
from Algorithms import *
import time
import math

lpo1 = lpo([ ("0","0"),
            ("00","00"),
            ("000","000"),
            ("0000","0000"),
            ],
           
           [("0","00"),("00","000"),("000","0000")]
           
           )

lpo2 = lpo([ ("0","0"),
            ("00","00"),
            ("000","000"),
            ("0001","0001"),
            ],
           
           [("0","00"),("00","000"),("000","0001")]
           
           )

lpo3 = lpo([ ("0","0"),
            ("00","00"),
            ("001","001"),
            ("0010","0010"),
            ],
           
           [("0","00"),("00","001"),("001","0010")]
           
           )

lpo4 = lpo([ ("0","0"),
            ("00","00"),
            ("001","001"),
            ("0011","0011"),
            ],
           
           [("0","00"),("00","001"),("001","0011")]
           
           )

lpo5 = lpo([ ("0","0"),
            ("01","01"),
            ("010","010"),
            ("0100","0100"),
            ],
           
           [("0","01"),("01","010"),("010","0100")]
           
           )

lpo6 = lpo([ ("0","0"),
            ("01","01"),
            ("010","010"),
            ("0101","0101"),
            ],
           
           [("0","01"),("01","010"),("010","0101")]
           
           )

lpo7 = lpo([ ("0","0"),
            ("01","01"),
            ("011","011"),
            ("0110","0110"),
            ],
           
           [("0","01"),("01","011"),("011","0110")]
           
           )

lpo8 = lpo([ ("0","0"),
            ("01","01"),
            ("011","011"),
            ("0111","0111"),
            ],
           
           [("0","01"),("01","011"),("011","0111")]
           
           )

def decThree(high):

    lpoDic = {}
    name = ""
    events = []
    for i in range(2**high):
        for j in range(2**high):
            if i % 2:
                next = "1"
            else:
                next = "0"
        name = name + next
        events.append((name, name))
        print events

    lpoDic[i] = lpo([], [])

    print lpoDic

def main():

    print("Dec Three")
    print("")

    sce=[lpo1,lpo2,lpo3,lpo4,lpo5,lpo6,lpo7,lpo8]
    sce_les=les_from_scenarios(sce)
    print("Number of partial orders: 8")
    print("Complexity of set of LPOs: %s" %(len(sce_les["events"])+len(sce_les["cau"])))
    op_les=optimize(sce_les)
    print("Complexity of LES: %s" %(len(op_les["events"])+len(op_les["cau"])+len(op_les["conf"])))
    print("")

    decThree(3)
          
if __name__ == "__main__" :
    main()
