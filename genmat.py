import random

def genmat(s1):
    q = []
    j = 0
    while j < 300:
        q.append(s1[j])
        j = j + 3
    sa1 = list(filter(lambda x: x == 1, q))
    a1  = len(sa1)
    st1 = list(filter(lambda x: x == 2, q))
    t1  = len(st1)
    sc1 = list(filter(lambda x: x == 3, q))
    c1  = len(sc1)
    sg1 = list(filter(lambda x: x == 4, q))
    g1  = len(sg1)
    q = []
    j = 1
    while j < 300:
        q.append(s1[j])
        j = j + 3
    sa2 = list(filter(lambda x: x == 1, q))
    a2  = len(sa2)
    st2 = list(filter(lambda x: x == 2, q))
    t2  = len(st2)
    sc2 = list(filter(lambda x: x == 3, q))
    c2  = len(sc2)
    sg2 = list(filter(lambda x: x ==4, q))
    g2  = len(sg2)
    q = []
    j = 2
    while j < 300:
        q.append(s1[j])
        j = j + 3
    sa3 = list(filter(lambda x: x == 1, q))
    a3  = len(sa3)
    st3 = list(filter(lambda x: x == 2, q))
    t3  = len(st3)
    sc3 = list(filter(lambda x: x == 3, q))
    c3  = len(sc3)
    sg3 = list(filter(lambda x: x == 4, q))
    g3  = len(sg3)
    matrix = [a1,t1,c1,g1,a2,t2,c2,g2,a3,t3,c3,g3]
    return matrix
    
    