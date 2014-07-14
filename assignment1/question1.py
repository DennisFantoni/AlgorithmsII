__author__ = 'dennis'




def read_stuff():
    text_file = open("/files/ferie/coursera/assignment_1_edges.txt", "r")
    lines = text_file.readlines()
    print lines
    print len(lines)
    text_file.close()
    firstline=True
    for line in lines:
        if firstline:
            firstline=False
        else:
            lineitems=line.split(" ")
            src = int(lineitems[0])
            dst = int(lineitems[1])
            weight = int(lineitems[2])
            edges[src].append((dst,weight))
            edges[dst].append((src,weight))

# item 0 never used, items 1 to and including 500 are used
vert_connected=[False for i in range(501)]

# item 0 never used, 1 to and including 500 are lists of tuples with connected vertices to vertice[n]
edges=[[] for i in range (501)]

crossing=[]

edges_used=[]

read_stuff()

total_treecost=0

def include_vertex(vertex,edge,edgeweight):
    edges_used.append((vertex,edge,edgeweight))
    vert_connected[vertex]=True
    for i in xrange(len(crossing)-1,-1,-1):
        if crossing[i][0]==vertex or crossing[i][1]==vertex:
            del crossing[i]
    for vert in edges[vertex]:
        if vert_connected[vert[0]]==False:
            crossing.append((vertex,vert[0],vert[1]))


vert_connected[1]=True
for e in edges[1]:
    crossing.append((e[0],1,e[1]))


while len(crossing)>0:
    minweight = 9999999999
    for c in crossing:
        if c[2] < minweight:
            minweight=c[2]
            mincrossing = c
    #process the minimum weight one
    total_treecost+=minweight
    if vert_connected[c[0]]:
        include_vertex(mincrossing[1],mincrossing[0],mincrossing[2])
    else:
        include_vertex(mincrossing[0],mincrossing[1],mincrossing[2])
    print("crossing %d  vertices found %d current cost %d" % (len(crossing),len(edges_used), total_treecost))


print("test")