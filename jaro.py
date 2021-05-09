import numpy as np
import json

mapk = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ], ])
def gett(obj,pos):
    pos=pos
    with open("maplyobj.json") as fr:
        data = json.load(fr)
        for a in range(0, len(data)):
            if data[a]["ob"]==obj:
                p=data[a]["terrain"]
                get_to(p,pos)
def get_to(a1,a2):
    global mapk
    a=a2[0]
    b=a2[1]
    c = a1
    x=a
    y=b
    x1=0
    x2=0
    print(c)
    mapk[a][b] = c[0][0]
    mapk[a][b + 1] = c[0][1]
    mapk[a][b + 2] = c[0][2]
    mapk[a+1][b] = c[1][0]
    mapk[a+1][b + 1] = c[1][1]
    mapk[a+1][b + 2] = c[1][2]
    return mapk


with open("maplypos.json") as f:
        data = json.load(f)
        for a in range(0, len(data)):
            t=data[a]["ob"]
            p=data[a]["pos"]
            gett(t,p)

print( mapk)

#    mapk[a][b]= c[0][0]
 #   mapk[a][b + 1] = c[0][1]
  #  mapk[a][b + 2] = c[0][2]
   # mapk[a+1][b] = c[1][0]
#    mapk[a+1][b + 1] = c[1][1]
 #   mapk[a+1][b + 2] = c[1][2]