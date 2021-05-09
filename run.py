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
    x1=0
    y1=0
    x=a
    y=b

    for row in range(len(a2)):
        y=b
        y1=0
        x += 1
        for col in range(len(a1)+1):
            if mapk[x][y] == 0 and c[x1][y1]==0:
                pass
            elif mapk[x][y] == 1 and c[x1][y1] == 0:
                pass
            elif mapk[x][y] == 1 and c[x1][y1] >=2:
                pass
            elif mapk[x][y] >= 2:
                pass
            else:
                mapk[x][y] = c[x1][y1]
            y += 1
            y1+=1
        x1 += 1




    return mapk

def do_map():
    with open("maplypos.json") as f:
            data = json.load(f)
            for a in range(0, len(data)):
                t=data[a]["ob"]
                p=data[a]["pos"]
                gett(t,p)
    print(mapk)
    return mapk

